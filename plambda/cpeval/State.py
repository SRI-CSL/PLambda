
from ..eval.Code import SExpression, Atom, StringLiteral, Syntax

from .Continuation import TopCont

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
                self.val = exp.string
            elif isinstance(self.exp, Atom):
                self.val = self.lookup(exp, env)
            elif isinstance(self.exp, SExpression):
                self.val = self.interpreter.evalSExpression(self.exp, self.env) #FIXME here we make continuations
            else:
                self.val = None
                self.k.setException(PLambdaException("huh? I did not grok {0}".format(exp)))

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
