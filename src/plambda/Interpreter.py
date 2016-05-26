import importlib


from src.util.Util import isString

from Code import SExpression, Atom, StringLiteral, Syntax
from SymbolTable import SymbolTable
from PLambdaException import PLambdaException

"""
Current bugs:

(int None)
(boolean None)
(float None)

"""



class Interpreter(object):

    def __init__(self):
        self.definitions = {}
        self.modules = {}


    def evaluate(self, exp):
        return self.eval(exp, None)

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
        """See if the indentifier is bound in the extended environment.

        First see if it referencing a thing in a module. Then, failing that
        look if it has a value in the current lexical environment. As a last
        resort see if it is a global definition. Otherwise raise a 
        PLambdaException.
        """
        (ok, value) = self.mlookup(leaf)
        if ok:
            return value
        (ok, value) = self.elookup(leaf, env)
        if ok:
            return value
        (ok, value) = self.glookup(leaf)
        if ok:
            return value
        raise PLambdaException('Unbound variable: {0}'.format(leaf))

    def mlookup(self, leaf):
        return (False, None)

    def elookup(self, leaf, env):
        return (False, None)

    def glookup(self, leaf):
        return (False, None)
                               

    def evalSExpression(self, sexp, env):
        code = sexp.code
        if code is Syntax.SEQ:
            print 'SEQ: coming soon to an interpreter near you!'
        elif code is Syntax.LET:
            print 'LET: coming soon to an interpreter near you!'
        elif code is Syntax.DEFINE:
            print 'DEFINE: coming soon to an interpreter near you!'
        elif code is Syntax.LAMBDA:
            print 'LAMBDA: coming soon to an interpreter near you!'
        elif code is Syntax.INVOKE:
            print 'INVOKE: coming soon to an interpreter near you!'
        elif code is Syntax.APPLY:
            print 'APPLY: coming soon to an interpreter near you!'
        elif code is Syntax.PRIMITIVE_DATA_OP :
            return self.evalPrimitiveDataOp(sexp, env)
        elif code is Syntax.UNARY_OP:
            return self.evalUnaryOp(sexp, env)
            print 'UNARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.BINARY_OP:
            print 'BINARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.TERNARY_OP:
            print 'TERNARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.AMBI1_OP:
            print ': coming soon to an interpreter near you!'
        elif code is Syntax.AMBI2_OP:
            print 'AMBI2_OP: coming soon to an interpreter near you!'
        elif code is Syntax.N_ARY_OP:
            print 'N_ARY_OP: coming soon to an interpreter near you!'
        elif code is Syntax.TRY:
            print 'TRY: coming soon to an interpreter near you!'
        elif code is Syntax.FOR:
            print 'FOR: coming soon to an interpreter near you!'
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
            pass
        elif op is SymbolTable.IMPORT:
            return self.importmod(val)
        elif op is SymbolTable.ISNONE:
            pass
        elif op is SymbolTable.ISOBJECT:
            pass
        elif op is SymbolTable.QUOTE:
            pass
        elif op is SymbolTable.THROW:
            pass
        elif op is SymbolTable.NOT:
            return True if val is False else False
        else:
            raise Exception("huh?")
        print 'UNARY_OP {0}: coming soon to an interpreter near you!'.format(op)
        return True
