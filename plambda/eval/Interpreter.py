""" The Interpreter.
"""

import importlib
import types
import inspect
import os
from collections.abc import (MutableMapping, Mapping)

from functools import partial

from ..util.Util import (isString, string2error)

from .Code import Atom

from .SymbolTable import SymbolTable

from .PLambdaException import PLambdaException

from .Environment import Environment

from .Globals import pythonGlobals

from ..visitor.Parser import parseFromFile, parseFromString

from .State import State


def plookup(leaf):
    """Looks up the symbol in the Python environment.

    This is a hack at present, as a means of looking up global functions.
    This is why we bail if the value is not callable.
    """
    assert isinstance(leaf, Atom)

    try:
        val = eval(leaf.string)
        if callable(val):
            return (True, val)
    except NameError:
        pass
    return (False, None)


class Interpreter:

    def __init__(self):
        self.definitions = {}
        self.modules = {}
        self.uid2object = {}
        self.object2uid = {}


    def evaluateString(self, string):
        """Parses and evaluates a string as plambda expression.
        """
        code = parseFromString(string)
        retval = None
        for c in code:
            retval = self.evaluate(c)
        return retval

    def evaluate(self, exp):
        """Evaluates an Sexpression, StringLiteral, or Atom.
        """
        return self.eval(exp, Environment())

    def eval(self, exp, env):
        state = State(self, exp, env)
        while not state.isDone():
            state.step()
        #iam: we raise the uncaught exception. not sure why we need to differ from jlambda
        if state.k.excep is not None:
            raise state.k.excep  # pylint: disable-msg=E0702
        return state.val



    def lookup(self, leaf, env):
        """See if the identifier is bound in the extended environment.

        First see if it referencing a thing in a module. Then, failing that
        look if it has a value in the current lexical environment. As a last
        resort see if it has a global definition, either in our global environment
        or in Python's. If it has a value in Python's global environment and that
        vaue is callable it retruns that. Otherwise it raises a PLambdaException.
        """

        assert isinstance(leaf, Atom)

        name = leaf.string
        path = name.split('.')

        (ok, value) = self.mlookup(path, leaf)
        if ok:
            return (ok, value)
        (ok, value) = env.lookup(leaf)
        if ok:
            return (ok, value)
        (ok, value) = self.glookup(path, leaf)
        if ok:
            return (ok, value)
        (ok, value) = plookup(leaf)
        if ok:
            return (ok, value)
        return (False, PLambdaException(f'Unbound variable: {repr(leaf)}'))


    def getmodule(self, path):
        """Finds the longest prefix of path that is in the modules dictionary.

        If finds a prefix returns (mod, path_remainder), else (None, path).
        """
        index = len(path)
        remainder = []
        current = None
        mod = None
        while index != 0:
            current = '.'.join(path[0:index])
            mod = self.modules.get(current)
            if mod is not None:
                break
            index -= 1
            remainder.insert(0, path[index])
        if mod is not None:
            return (mod, remainder)
        return (None, path)

    def getobject(self, obj, path):
        """Follows the path from object.

        Follows the path down into the obj, which should be a class or module,
        and if what lies at the end is x returns (True, x), else, if the path
        makes no sense at some stage, returns (False, None).
        """
        if path == []:
            return (True, obj)
        if obj is None:
            return (False, None)
        if inspect.ismodule(obj):
            d = obj.__dict__
            k = path[0]
            if k in d:
                return self.getobject(obj.__dict__.get(k), path[1:])
            return (False, None)
        if hasattr(obj, path[0]):
            nobj = getattr(obj, path[0])
        else:
            return (False, None)
        return self.getobject(nobj, path[1:])


    def mlookup(self, path, leaf):
        """Just a quick 'n dirty hack at this point.
        """
        assert isinstance(leaf, Atom)

        (mod, remainder) = self.getmodule(path)

        return self.getobject(mod, remainder)

    def glookup(self, path, leaf):
        """Looks up the symbol in the PLambda definitions."""
        assert isinstance(leaf, Atom)

        ok = False

        if len(path) > 1:
            key = path[0]
            val = self.definitions.get(key)
            if val is not None:
                (ok, val) = self.getobject(val, path[1:])
        else:
            key = leaf.string
            ok = key in self.definitions
            if ok:
                val = self.definitions[key]

        if ok:
            return (True, val)
        return (False, None)


    def callInvoke(self, obj, methodname, vals, location):

        methods = inspect.getmembers(obj, callable)

        if not methods:
            return (False, PLambdaException(f'Object not invokable: {obj} {location}'))

        method = None

        if not isString(methodname):
            return (False, PLambdaException(f'Method name not a string: {methodname} {location}'))


        for (name, value) in methods:
            if name == methodname:
                method = value
                break

        if method is None:
            return (False, PLambdaException(f'No such method: {methodname} {location}'))

        # Ugliness under python's hood:
        # Cannot get the argspec of a builtin
        # http://stackoverflow.com/questions/3276635/how-to-get-the-number-of-args-of-a-built-in-function-in-python
        # http://stackoverflow.com/questions/990016/how-to-find-out-the-arity-of-a-method-in-python
        #
        # Can avoid using inspect for simple cases:
        #        def arity(obj, method):
        #          return getattr(obj.__class__, method).func_code.co_argcount - 1 # remove self
        #
        if not isinstance(method, types.BuiltinFunctionType):

            # 05/08/20 flipped inspect.getargspec(method) to
            # inspect.getfullargspec(method) without having a clue what I was doing.
            # but the doc said: "Deprecated since version 3.0: Use
            # getfullargspec() for an updated API that is usually a drop-in replacement,
            # but also correctly handles function annotations and keyword-only parameters."

            argspec = inspect.getfullargspec(method)
            # string2error(f'argspec({method}) =  {argspec}')
            # if it is an object we have to *not* count 'self',
            # but if it is a class we need to pass all the args!
            offset = 0
            # if the thing has vargargs (e.g. decorators for example, then we better just try to apply)
            if (not inspect.ismodule(obj)) and (not inspect.isclass(obj)) and  argspec.varargs is None:
                offset = 1
                ndefaults = len(argspec.defaults)  if argspec.defaults else 0
                nargs = len(argspec.args) - offset
                nvals = len(vals)
                # my guess is that we will need to revisit this. what do we
                # do when some of the defaults are used but not others?
                if (nvals < nargs - ndefaults) or  (nargs < nvals):
                    msg = f'Arity of {methodname} args {vals} does not match the argspec: {argspec.args[offset:]}. defaults: {argspec.defaults} varargs: {argspec.varargs}'
                    return (False, PLambdaException(msg))

        retval = None

        try:
            retval = method(*vals)
            return (True, retval)
        except Exception as e:
            return (False, PLambdaException(f'invoke {location} threw {str(e)}'))


    def callCallable(self, fun, vals, _):
        retval = None
        assert callable(fun)
        try:
            retval = fun(*vals)
            return (True, retval)
        except Exception as e:
            return (False, e)


    def callBinaryOp(self, op, val0, val1, location):
        retval = None
        try:
            if  op is SymbolTable.PLUS:
                retval = val0 + val1
            elif op is SymbolTable.TIMES:
                retval = val0 * val1
            elif op is SymbolTable.DIVIDE:
                retval = val0 / val1
            elif op is SymbolTable.MODULO:
                retval = val0 % val1
            elif op is SymbolTable.GT:
                retval = val0 < val1
            elif op is SymbolTable.LT:
                retval = val0 > val1
            elif op is SymbolTable.GET:
                retval = self.evalGet(val0, val1, location)
            elif op is SymbolTable.GEQ:
                retval = val0 >= val1
            elif op is SymbolTable.LEQ:
                retval = val0 <= val1
            elif op is SymbolTable.EQUALS:
                retval = val0 == val1
            elif op is SymbolTable.IN:
                retval = val0 in val1
            elif op is SymbolTable.EQ:
                retval = val0 is val1
            elif op is SymbolTable.IS:
                retval = val0 is val1
            elif op is SymbolTable.NEQ:
                retval = val0 != val1
            elif op is SymbolTable.SETUID:
                retval = self.setUID(val0, val1, location)
            else:
                return (False, PLambdaException(f'Unrecognized binary operation: {op} {location}'))
        except Exception as e:
            return (False, PLambdaException(f'callTernaryOp {op} {location} threw {str(e)}'))
        return (True, retval)


    def evalGet(self, val0, val1, location):
        if isinstance(val0, (list, tuple)) and isinstance(val1, int):
            return val0[val1]
        if isinstance(val0, Mapping):
            return val0.get(val1)
        raise PLambdaException(f'Bad args to \"get\": {val0} {val1} {location}')

    def unsetUID(self, val0):
        if val0 in self.object2uid:
            uid = self.object2uid[val0]
            self.object2uid.pop(val0)
            self.uid2object.pop(uid)
            return True
        return False


    def setUID(self, val0, val1, location):
        if val0 is None:
            raise PLambdaException(f'setuid {str(location)}: first argument cannot be None.')
        if val1 is None:
            return self.unsetUID(val0)
        if not isString(val1):
            raise PLambdaException(f'setuid {str(location)}: val1 not a string.')
        if val1 in self.uid2object or val0 in self.object2uid:
            raise PLambdaException(f'setuid {str(location)}: redefiniton')
        self.object2uid[val0] = val1
        self.uid2object[val1] = val0
        return True

    def evalKWApply(self, val0, val1, val2, loc):
        if not callable(val0):
            raise PLambdaException(f'kwapply {str(loc)}: 1st argument not callable')
        if not isinstance(val1, list):
            raise PLambdaException(f'kwapply {str(loc)}: 2nd argument not a list')
        if not isinstance(val2, dict):
            raise PLambdaException(f'kwapply {str(loc)}: 3rd argument not a dict')
        return  val0(*val1, **val2)


    def evalModify(self, val0, val1, val2, loc):
        #be brave until we need to back down...
        if isinstance(val0, MutableMapping):
            val0[val1] = val2
        elif isinstance(val0, list):
            l0 = len(val0)
            if isinstance(val1, int) and -l0 < val1 < l0:
                val0[val1] = val2
            else:
                raise PLambdaException(f'modify {str(loc)}: bad index to modify of list')
        else:
            raise PLambdaException(f'modify {str(loc)}: unhandled case')




    def callTernaryOp(self, op, val0, val1, val2, location):
        retval = None
        try:
            if  op in (SymbolTable.UPDATE, SymbolTable.SUPDATE, SymbolTable.SETATTR):
                setattr(val0, val1, val2)
                retval = None
            elif op is SymbolTable.KWAPPLY:
                retval = self.evalKWApply(val0, val1, val2, location)
            elif op is SymbolTable.MODIFY:
                self.evalModify(val0, val1, val2, location)
            else:
                return (False, PLambdaException(f'Unrecognized ternary operation: {op} {location}'))
        except Exception as e:
            return (False, PLambdaException(f'callTernaryOp {op} {location} threw {str(e)}'))
        return (True, retval)



    def callGetAttr(self, vals, location):
        retval = None
        try:
            retval = getattr(*vals)
            return (True, retval)
        except Exception as e:
            return (False, PLambdaException(f'callGetAttr {location} threw {str(e)}'))



    def evalPrimitiveDataOp(self, sexp, _):
        (a0, a1) = sexp.spine
        assert isinstance(a0, Atom)
        assert isinstance(a1, Atom)
        op = a0.string
        data = a1.string
        try:
            if op is SymbolTable.INT:
                return int(data)
            if op is SymbolTable.FLOAT:
                return float(data)
            return data.lower() == 'true'
        except Exception as e:
            string2error(f'evalPrimitiveDataOp: {str(e)} {a0.location}')
            return 0 if op is not SymbolTable.FLOAT else 0.0


    def importmod(self, val):
        try:

            if isString(val):
                module = importlib.import_module(val)
                if module is not None:
                    self.modules[val] = module
                    return True
                string2error(f'Module {val} not found')
            return False

        except ImportError as ie:
            print(ie)
            return False


    def evalGlobal(self, val, _):
        return pythonGlobals.get(val, None)

    def callUnaryOp(self, op, val, location):
        """Calls the unary op with argument val.

           It returns (True, op(val) if everything is OK, otherwise
        it returns (False, Exception).
        """
        retval = None
        try:
            if  op is SymbolTable.LOAD:
                if isString(val):
                    retval = self.load(val)
                else:
                    retval = False
            elif op is SymbolTable.IMPORT:
                retval = self.importmod(val)
            elif op is SymbolTable.ISNONE:
                retval = val is None
            elif op is SymbolTable.ISINT:
                retval = isinstance(val, int)
            elif op is SymbolTable.ISFLOAT:
                retval = isinstance(val, float)
            elif op is SymbolTable.ISOBJECT:
                retval = val is not None
            elif op is SymbolTable.GLOBAL:
                retval = self.evalGlobal(val, location)
            elif op is SymbolTable.THROW:
                return (False, val)
            elif op is SymbolTable.FETCH:
                if val in self.uid2object:
                    retval = self.uid2object[val]
                else:
                    retval = None
            elif op is SymbolTable.GETUID:
                if val in self.object2uid:
                    retval = self.object2uid[val]
                else:
                    retval = None
            elif op is SymbolTable.NOT:
                retval = not val #True if val is False else False
            else:
                return (False, PLambdaException(f'Unrecognized unary op {op} {location}'))
        except Exception as e:
            return (False, PLambdaException(f'callUnaryOp {op} {location} threw {str(e)}'))

        return (True, retval)

    def load(self, filename):
        if isString(filename) and os.path.exists(filename):
            codelist = parseFromFile(filename)
            for c in codelist:
                self.evaluate(c)
            return True
        if isString(filename) and not os.path.exists(filename):
            string2error(f'\nThe file "{filename}" was not found.')
        return False


    def showDefinitions(self, sb=None):
        """Either writes the definitions out to stderr, or the optional StringBuffer passed in.
        """
        func = sb.append if sb else partial(string2error, newline=False)
        for key, value in self.definitions.items():
            func(f'{key}  -->  {value}\n')
        return sb

    def showUIDs(self, sb=None):
        """Either writes the UIDs out to stderr, or the optional StringBuffer passed in.
        """
        func = sb.append if sb else partial(string2error, newline=False)
        for key, value in self.uid2object.items():
            func(f'{key}  -->  {value}\n')
        return sb
