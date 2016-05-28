import importlib

import types

import inspect

import collections

from src.util.Util import isString, isInteger

from Code import SExpression, Atom, StringLiteral, Syntax

from SymbolTable import SymbolTable

from PLambdaException import PLambdaException

from Environment import Environment

from Closure import Closure

from src.visitor.Parser import parseFromFile

"""
Current bugs:

(int None)
(boolean None)
(float None)

(apply print "foo")

Things to add:

isfunction

some -1's in Visitor should be improved now that everything has a location.

patch the builtin problem as much as possible

named arguments need to be addressed at some point

"""



class Interpreter(object):

    def __init__(self):
        self.definitions = {}
        self.modules = {}


    def evaluate(self, exp):
        return self.eval(exp, Environment())

    def eval(self, exp, env):
        if isinstance(exp, StringLiteral):
            return exp.string
        if isinstance(exp, Atom):
            return self.lookup(exp, env)
        elif isinstance(exp, SExpression):
            return self.evalSExpression(exp, env)
        else:
            raise PLambdaException("huh?")

    def lookup(self, leaf, env):
        """See if the identifier is bound in the extended environment.

        First see if it referencing a thing in a module. Then, failing that
        look if it has a value in the current lexical environment. As a last
        resort see if it is a global definition, either in our global environment
        or in Python's. Otherwise raise a PLambdaException.
        """

        assert(isinstance(leaf,Atom))

        (ok, value) = self.mlookup(leaf)
        if ok:
            return value
        (ok, value) = env.lookup(leaf)
        if ok:
            return value
        (ok, value) = self.glookup(leaf)
        if ok:
            return value
        (ok, value) = self.plookup(leaf)
        if ok:
            return value
        raise PLambdaException('Unbound variable: {0}'.format(repr(leaf)))

        
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
        else:
            return (None, path)

    def getobject(self, obj, path):
        """Follows the path from object.

        Follows the path down into the obj, which should be a class or module,
        and if what lies at the end is x returns (True, x), else, if the path
        makes no sense at some stage, returns (False, None).
        """
        if obj is None:
            return (False, None)
        if path == []:
            return (True, obj)
        elif inspect.ismodule(obj):
            return self.getobject(obj.__dict__.get(path[0]), path[1:])
        else:
            return self.getobject(obj[path[0]], path[1:])
        
        
    def mlookup(self, leaf):
        """Just a quick 'n dirty hack at this point.
        """
        assert(isinstance(leaf, Atom))

        name = leaf.string
        path = name.split('.')

        (mod, remainder) = self.getmodule(path)

        return self.getobject(mod, remainder)

    def glookup(self, leaf):
        assert(isinstance(leaf, Atom))

        key = leaf.string
        
        if key in self.definitions:
            return (True, self.definitions[key])
        else:
            return (False, None)

    def plookup(self, leaf):
        try:
            val = eval(leaf.string)
            return (True, val)
        except NameError:
            return (False, None)

    def evalSeq(self, sexp, env):
        tail = sexp.spine[1:]
        retval = None
        for s in tail:
            retval = self.eval(s, env)
        return retval

    def evalInvoke(self, sexp, env):
        objexp = sexp.spine[1]
        obj = self.eval(objexp, env)

        methods = inspect.getmembers(obj, callable)

        if not methods:
            fmsg = 'Object not invokable: {0} evaluated to {1}'
            emsg = fmsg.format(repr(objexp), obj)
            raise PLambdaException(emsg)

        methodexp = sexp.spine[2]
        methodname  = self.eval(methodexp, env)
        method = None
        
        if not isString(methodname):
            fmsg = 'Method name not a string: {0} evaluated to {1}'
            emsg = fmsg.format(repr(methodexp), methodname)
            raise PLambdaException(fmsg)

        
        for (name, value) in methods:
            if name == methodname:
                method = value
                break

        if method is None:
            emsg = 'No such method: {0}'.format(repr(methodname))
            raise PLambdaException(emsg)
        
        args = sexp.spine[3:]

        # print 'type({0}): '.format(methodname), type(method),  types.BuiltinFunctionType
        # Ugliness under python's hood. Cannot get the argspec of a builtin
        # http://stackoverflow.com/questions/3276635/how-to-get-the-number-of-args-of-a-built-in-function-in-python
        if type(method) !=  types.BuiltinFunctionType:
            argspec = inspect.getargspec(method)
            # if it is an object we have to *not* count 'self',
            # but if it is a class we need to pass all the args!
            offset = 0
            if not inspect.ismodule(obj) and not inspect.isclass(obj):
                offset = 1
        
                if len(argspec.args) - offset  != len(args): 
                    fmsg = 'Arity of {0} args {1} does not match the argspec: {2}'
                    emsg = fmsg.format(methodname, args, argspec.args[offset:])
                    raise PLambdaException(emsg)
        
        
        vals = []
        for a in args:
            vals.append(self.eval(a, env))
        
        return method(*vals)


    def evalDefine(self, sexp, env):
        identifier = sexp.spine[1]
        
        assert(isinstance(identifier, Atom))
        
        val = None

        if len(sexp.spine) == 3:
            val = self.eval(sexp.spine[2], env)
        else:
            val = Closure(self, sexp.spine[2], sexp.spine[3], env, sexp.spine[0].location)

        self.definitions[identifier.string] = val
        return identifier
    

    def evalLet(self, sexp, env):
        nenv = Environment(env)
        bindings = sexp.spine[1].spine
        body = sexp.spine[2]

        for bpair in bindings:
            var = bpair.spine[0]
            assert(isinstance(var, Atom))
            nenv.extend(var, self.eval(bpair.spine[1], nenv))

        return self.eval(body, nenv)
        
    def evalApply(self, sexp, env):
        funexp  = sexp.spine[1]
        argexps = sexp.spine[2:]

        fun = self.eval(funexp, env)

        if not isinstance(fun, Closure) and not callable(fun):
            fmsg = 'Cannot apply {0} which evaluated to {1}'
            emsg = fmsg.format(funexp, fun)
            raise PLambdaException(emsg)

        vals = []
        for arg in argexps:
            vals.append(self.eval(arg, env))

        #TODO: some arity checking would be nice
        if isinstance(fun, Closure):
            return fun.applyClosure(*vals)
        else:
            return fun(*vals)


    def evalFor(self, sexp, env):
        identifier = sexp.spine[1]
        rangeexp = sexp.spine[2]
        body = sexp.spine[3]

        rangeval = self.eval(rangeexp, env)

        if isInteger(rangeval):
            rangeval = range(0, rangeval)  #FIXME: not very efficient for big integers
            
        if isinstance(rangeval, collections.Iterable):
            retval = None
            for v in rangeval:
                nenv = Environment(env)
                retval = self.eval(body, nenv.extend(identifier, v))
            return retval
        else:
            fmsg = 'Range is not iterable: {0} evaluated to {1}'
            emsg = fmsg.format(rangeexp, rangeval)
            raise PLambdaException(emsg)
        
                               
    def evalSExpression(self, sexp, env):
        code = sexp.code
        if code is Syntax.SEQ:
            return self.evalSeq(sexp, env)
        elif code is Syntax.LET:
            return self.evalLet(sexp, env)
        elif code is Syntax.DEFINE:
            return self.evalDefine(sexp, env)
        elif code is Syntax.LAMBDA:
            spine = sexp.spine
            return Closure(self, spine[1], spine[2], env, spine[0].location)
        elif code is Syntax.INVOKE:
            return self.evalInvoke(sexp, env)
        elif code is Syntax.APPLY:
            return self.evalApply(sexp, env)
        elif code is Syntax.PRIMITIVE_DATA_OP :
            return self.evalPrimitiveDataOp(sexp, env)
        elif code is Syntax.UNARY_OP:
            return self.evalUnaryOp(sexp, env)
        elif code is Syntax.BINARY_OP:
            print 'BINARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.TERNARY_OP:
            print 'TERNARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.AMBI1_OP:
            print 'AMBI1_OP: coming soon to an interpreter near you!'
        elif code is Syntax.AMBI2_OP:
            print 'AMBI2_OP: coming soon to an interpreter near you!'
        elif code is Syntax.N_ARY_OP:
            print 'N_ARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.TRY:
            print 'TRY: coming soon to an interpreter near you!'
        elif code is Syntax.FOR:
            return self.evalFor(sexp, env)
        elif code is Syntax.QUOTE:
            print 'QUOTE: coming soon to an interpreter near you!'
        else:
            raise PLambdaException("huh?")

    def evalPrimitiveDataOp(self, sexp, env):
        (a0, a1) = sexp.spine
        assert isinstance(a0, Atom)
        assert isinstance(a1, Atom)
        op = a0.string
        data = a1.string
        if op is SymbolTable.INT:
            return int(data)
        elif op is SymbolTable.FLOAT:
            return float(data)
        else:
            return True if data.lower() == 'true' else False


    def importmod(self, val):
        if isString(val):
            module = importlib.import_module(val)
            if module is not None:
                self.modules[val] = module
                return True
            else:
                sys.stderr.write('Module {0} not found'.format(val))
        return False

    
    def evalUnaryOp(self, sexp, env):
        (uop, arg) =  sexp.spine
        assert isinstance(uop, Atom)
        op = uop.string
        val = self.eval(arg, env)
        if  op is SymbolTable.LOAD:
            if isString(val):
                return self.load(val)
            else:
                return False
        elif op is SymbolTable.IMPORT:
            return self.importmod(val)
        elif op is SymbolTable.ISNONE:
            return val is None
        elif op is SymbolTable.ISOBJECT:
            return inspect.isobject(val)
        elif op is SymbolTable.QUOTE:
            print 'UNARY_OP {0}: coming soon to an interpreter near you!'.format(op)
            pass
        elif op is SymbolTable.THROW:
            print 'UNARY_OP {0}: coming soon to an interpreter near you!'.format(op)
            pass
        elif op is SymbolTable.NOT:
            return True if val is False else False
        else:
            raise Exception("huh?")
        return True


    def load(self, filename):
        if isString(filename):
            codelist = parseFromFile(filename)
            for c in codelist:
                self.evaluate(c)
            return True
        return False

        
    def showDefinitions(self):
        for key, value in self.definitions.iteritems():
            print '{0}  -->  {1}'.format(key, value)
