
from ..eval.Code import SExpression, Atom, StringLiteral, Syntax


class Tag(object):
    EVAL     = 0
    CONTINUE = 1
    RETURN   = 2
    DONE     = 3


class State(object):

    def __init__(self, interpreter, exp, env):
        self.interpreter = interpreter
        self.tag = Tag.EVAL
        self.val = None
        self.exp = exp
        self.env = env
        self.k = None #FIXME: TopCont()


    def isDone(self):
        return self.tag is Tag.DONE


    def step(self):

        if self.tag is Tag.EVAL:

            if  self.exp is None:
                self.val = None
            elif isinstance(self.exp, StringLiteral):
                self.val = exp.string
            elif isinstance(self.exp, Atom):
                self.val = self.lookup(exp, env)
            elif isinstance(exp, SExpression):
                self.val = interpreter.evalSExpression(self.exp, self.env) #FIXME here we make continuations
            else:
                self.val = None
                self.k.setException(PLambdaException("huh? I did not grok {0}".format(exp)))

            self.tag = Tag.RETURN
            
        elif self.tag is Tag.CONTINUE:
            k.cont(self)
        elif self.tag is Tag.RETURN:
            k.ret(self)
        elif self.tag is Tag.DONE:
            pass
        else:
            pass

        return
