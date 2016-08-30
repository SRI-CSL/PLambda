
from ..eval.PLambdaException import PLambdaException

import State


class Continuation(object):


    def __init__(self, exp=None, args=None, env=None, k=None):
        self.exp = exp
        self.args = args
        if self.args is not None:
            self.vals = [ None ] * len(args)
        self.n = 0
        self.env = env
        self.k = k
        self.excep = None
        if self.exp is not None:
            self.msg = '{0} :'.format(exp.spine[0])


    def ret(self, state):
        """ ret is deals with the exceptional case. 
        
        By default, thrown exceptions propagated up the continuation
        chain.  Continuations that handle exceptions (TryCont and
        TopCont, currently) do so by overriding `ret'.
        """
        if self.excep is not None:
            #FIXME: info() gets passed in to the EvaluateError
            self.k.excep = excep
            state.k = self.k
        else:
            self.handleReturn(state)


    def handleReturn(self, state):
        pass


    def info(self):
        """FIXME: can write this soon.
        """
        pass

    

class TopCont(Continuation):

    def __init__(self):
        Continuation.__init__(self)

    def cont(self, state):
        raise PLambdaException("Calling cont on a TopCont is forbidden")


    def ret(self, state):
        if self.excep is not None:
            sys.stderr.write("FIXME: Debugger.handle(excep)\n")

        state.tag = State.DONE

            
    def handleReturn(self, state):
        pass

    
        
