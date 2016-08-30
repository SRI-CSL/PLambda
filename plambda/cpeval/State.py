from ..eval.Code import SExpression, Atom, StringLiteral, Syntax

from ..eval.Closure import Closure

from ..eval.SymbolTable import SymbolTable

from .Continuation import TopCont, IfCont, SeqCont, UnaryOpCont, BinaryOpCont, TernaryOpCont

EVAL     = 0
CONTINUE = 1
RETURN   = 2
DONE     = 3



class State(object):

    def __init__(self, interpreter, exp, env):
        self.interpreter = interpreter
        self.tag = EVAL
        self.val = None
        self.exp = exp
        self.env = env
        self.k = TopCont()


    def isDone(self):
        return self.tag is DONE


    def step(self):

        if self.tag is EVAL:

            if  self.exp is None:
                self.val = None
            elif isinstance(self.exp, StringLiteral):
                self.val = self.exp.string
            elif isinstance(self.exp, Atom):
                self.val = self.lookup(exp, env)
            elif isinstance(self.exp, SExpression):


                code = self.exp.code
                opexp = self.exp.spine[0]

                assert isinstance(opexp, Atom)
                op = opexp.string

                if code is Syntax.SEQ:
                    self.k = SeqCont(self.exp, self.exp.spine[1:], self.env, self.k);
                    self.tag = CONTINUE;
                    return 
                elif code is Syntax.LET:
                    pass
                elif code is Syntax.DEFINE:
                    pass
                elif code is Syntax.LAMBDA:
                    spine = self.exp.spine
                    self.val = Closure(self, spine[1], spine[2], self.env, spine[0].location)
                    self.tag = RETURN
                    return
                elif code is Syntax.INVOKE:                    
                    pass
                elif code is Syntax.APPLY:
                    pass
                elif code is Syntax.PRIMITIVE_DATA_OP:
                    self.val = self.interpreter.evalPrimitiveDataOp(self.exp, self.env)
                    self.tag = RETURN
                    return
                elif code is Syntax.UNARY_OP:
                    self.k = UnaryOpCont(self.exp, self.exp.spine[1:], self.env, self.k);
                    self.tag = CONTINUE;
                    return 
                elif code is Syntax.BINARY_OP:                    
                    self.k = BinaryOpCont(self.exp, self.exp.spine[1:], self.env, self.k);
                    self.tag = CONTINUE;
                    return 
                elif code is Syntax.TERNARY_OP:
                    self.k = TernaryOpCont(self.exp, self.exp.spine[1:], self.env, self.k);
                    self.tag = CONTINUE;
                    return 
                elif code is Syntax.AMBI1_OP:
                    pass
                elif code is Syntax.AMBI2_OP:
                    if op is SymbolTable.IF:
                        self.k = IfCont(self.exp, self.exp.spine[1:], self.env, self.k);
                        self.tag = CONTINUE;
                        return 
                    elif op is SymbolTable.GETATTR:
                        pass
                    else:
                        pass
                elif code is Syntax.N_ARY_OP:                    
                    pass
                elif code is Syntax.TRY:
                    pass
                elif code is Syntax.FOR:
                    pass
                elif code is Syntax.QUOTE:
                    pass
                elif code is Syntax.CATCH:
                    pass
                else:
                   raise PLambdaException("Unhandled form in State.step")
                #FIXME: we are done when this can be removed, as so can the above returns ...
                self.val = self.interpreter.evalSExpression(self.exp, self.env)
            else:
                self.val = self.exp

            self.tag = RETURN

            
        elif self.tag is CONTINUE:
            self.k.cont(self)
        elif self.tag is RETURN:
            self.k.ret(self)
        elif self.tag is DONE:
            pass
        else:
            pass

        return
