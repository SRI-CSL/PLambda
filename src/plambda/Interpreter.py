from Code import SExpression, Atom, Syntax




class Interpreter(object):

    def __init__(self):
        self.definitions = {}


    def evaluate(self, exp):
        if isinstance(exp, Atom):
            self.lookup(exp)
        elif isinstance(exp, SExpression):
            self.evalSExpression(exp)
        else:
            raise Exception("huh?")
        return True

    def lookup(self, leaf):
        pass


    def evalSExpression(self, sexp):
        code = sexp.code
        if code == Syntax.SEQ:
            print 'SEQ: coming soon to an interpreter near you!'
        elif code == Syntax.LET:
            print 'LET: coming soon to an interpreter near you!'
        elif code == Syntax.DEFINE:
            print 'DEFINE: coming soon to an interpreter near you!'
        elif code == Syntax.LAMBDA:
            print 'LAMBDA: coming soon to an interpreter near you!'
        elif code == Syntax.INVOKE:
            print 'INVOKE: coming soon to an interpreter near you!'
        elif code == Syntax.APPLY:
            print 'APPLY: coming soon to an interpreter near you!'
        elif code == Syntax.PRIMITIVE_DATA_OP :
            print 'PRIMITIVE_DATA_OP : coming soon to an interpreter near you!'
        elif code == Syntax.UNARY_OP:
            print 'UNARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.BINARY_OP:
            print 'BINARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.TERNARY_OP:
            print 'TERNARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.AMBI1_OP:
            print ': coming soon to an interpreter near you!'
        elif code == Syntax.AMBI2_OP:
            print 'AMBI2_OP: coming soon to an interpreter near you!'
        elif code == Syntax.N_ARY_OP:
            print 'N_ARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.TRY:
            print 'TRY: coming soon to an interpreter near you!'
        elif code == Syntax.FOR:
            print 'FOR: coming soon to an interpreter near you!'
        elif code == Syntax.QUOTE:
            print 'QUOTE: coming soon to an interpreter near you!'
        else:
            raise Exception("huh?")

