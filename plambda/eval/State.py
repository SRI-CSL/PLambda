from .Code import SExpression, Atom, StringLiteral, Syntax

from .Closure import Closure

from .SymbolTable import SymbolTable

from .Continuation import ( TopCont, IfCont, SeqCont, DefineCont, TryCont, LetCont, ForCont,
                            UnaryOpCont, BinaryOpCont, TernaryOpCont, Ambi1OpCont,
                            ConcatCont, MkCont,
                            AndCont, OrCont,
                            ApplyCont, InvokeCont, GetAttrCont )


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
                self.tag = RETURN
            elif isinstance(self.exp, StringLiteral):
                self.val = self.exp.string
                self.tag = RETURN
            elif isinstance(self.exp, Atom):
                self.val = self.interpreter.lookup(self.exp, self.env)
                self.tag = RETURN
            elif isinstance(self.exp, SExpression):
                code = self.exp.code
                opexp = self.exp.spine[0]
                if not isinstance(opexp, Atom):
                    print 'not atom: {0} {1} {2} {3}'.format(opexp, type(opexp), self.exp, self.exp.code)
                assert isinstance(opexp, Atom)
                op = opexp.string
                if code is Syntax.SEQ:
                    self.k = SeqCont(self.exp, self.exp.spine[1:], self.env, self.k);
                    self.tag = CONTINUE
                elif code is Syntax.LET:
                    self.k = LetCont(self.exp, self.exp.spine[1:], self.env, self.k);
                    self.tag = CONTINUE
                elif code is Syntax.DEFINE:
                    self.k = DefineCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.LAMBDA:
                    spine = self.exp.spine
                    self.val = Closure(self, spine[1], spine[2], self.env, spine[0].location)
                    self.tag = RETURN
                elif code is Syntax.INVOKE:                    
                    self.k = InvokeCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.APPLY:
                    self.k = ApplyCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.PRIMITIVE_DATA_OP:
                    self.val = self.interpreter.evalPrimitiveDataOp(self.exp, self.env)
                    self.tag = RETURN
                elif code is Syntax.UNARY_OP:
                    self.k = UnaryOpCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.BINARY_OP:                    
                    self.k = BinaryOpCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.TERNARY_OP:
                    self.k = TernaryOpCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.AMBI1_OP:
                    self.k = Ambi1OpCont(op, self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.AMBI2_OP:
                    if op is SymbolTable.IF:
                        self.k = IfCont(self.exp, self.exp.spine[1:], self.env, self.k)
                        self.tag = CONTINUE
                    elif op is SymbolTable.GETATTR:
                        self.k = GetAttrCont(self.exp, self.exp.spine[1:], self.env, self.k)
                        self.tag = CONTINUE
                    else:
                        raise PLambdaException("Unhandled ambi2 op form in State.step {0} {1}".format(op, self.exp.spine[0].location))
                elif code is Syntax.N_ARY_OP:
                    if op is SymbolTable.AND:
                        self.k = AndCont(self.exp, self.exp.spine[1:], self.env, self.k)
                        self.tag = CONTINUE
                    elif op is SymbolTable.OR:
                        self.k = OrCont(self.exp, self.exp.spine[1:], self.env, self.k)
                        self.tag = CONTINUE
                    elif op is SymbolTable.CONCAT:
                        self.k = ConcatCont(self.exp, self.exp.spine[1:], self.env, self.k)
                        self.tag = CONTINUE
                    elif op in (SymbolTable.MKTUPLE, SymbolTable.MKLIST, SymbolTable.MKDICT):
                        self.k = MkCont(op, self.exp, self.exp.spine[1:], self.env, self.k)
                        self.tag = CONTINUE
                    else:
                        raise PLambdaException("Unhandled n-ary op form in State.step {0} {1}".format(op, self.exp.spine[0].location))
                elif code is Syntax.TRY:
                    self.k = TryCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.FOR:
                    self.k = ForCont(self.exp, self.exp.spine[1:], self.env, self.k)
                    self.tag = CONTINUE
                elif code is Syntax.CATCH:
                    raise PLambdaException("Orphan catch. Should not happen")
                else:
                   raise PLambdaException("Unhandled form in State.step")
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
