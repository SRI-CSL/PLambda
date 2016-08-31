import sys

from ..eval.PLambdaException import PLambdaException

from ..util.StringBuffer import StringBuffer

from ..eval.SymbolTable import SymbolTable

import State


class Continuation(object):


    def __init__(self, exp=None, args=None, env=None, k=None):
        self.exp = exp
        self.args = args

        if self.args is not None:
            self.argslen = len(args)
            self.vals = [ None ] * self.argslen
        else:
            self.argslen = None
            self.vals = None
            
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
            if isinstance(self.excep, PLambdaException):
                self.excep.extendBT(self.info())
            self.k.excep = excep
            state.k = self.k
        else:
            self.handleReturn(state)


    def handleReturn(self, state):
        pass


    def info(self):
        sb = StringBuffer()
        if not self.vals:
            sb.append('\tcomputing result of top-level form ')
        elif self.n in len(self.vals):
            sb.append('\tcomputing result of ').append(exp.spine[0]).append(' form')
        else:
            sb.append('\tat  argument ').append(self.n).append(' of ').append(exp.spine[0]).append(' form')
        sb.append(' at ').append(exp.location)
        return str(sb)
    

class TopCont(Continuation):

    def __init__(self):
        Continuation.__init__(self)

    def cont(self, state):
        raise PLambdaException("Calling cont on a TopCont is forbidden")


    def ret(self, state):
        if self.excep is not None:
            sys.stderr.write("FIXME: Debugger.handle(excep)\n")
            #sys.stderr.write(str(self.excep))
        state.tag = State.DONE

            
    def handleReturn(self, state):
        pass

    
        
class IfCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        state.tag = State.EVAL
        state.exp = self.args[0]
        state.env = self.env

    def handleReturn(self, state):
        if not isinstance(state.val, bool):
            msg = '{0} is not a boolean in conditional {1}'
            self.k.excep = PLambdaException(msg.format(state.val, self.exp.spine[0].location))
            state.k = self.k
            return
        elif state.val:
            state.tag = State.EVAL
            state.exp = self.args[1]
            state.env = self.env
        elif  self.argslen == 3:
            state.tag = State.EVAL
            state.exp = self.args[2]
            state.env = self.env
        else:
            state.tag = State.RETURN
            state.val = None

        state.k = self.k
        
    

class EvalArgsCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)


    def cont(self, state):
        if self.argslen > 0:
            state.tag = State.EVAL
            state.exp = self.args[self.n]
            state.env = self.env
        else:
            self.finish(state)

    def handleReturn(self, state):
        self.n += 1

        if not self.receiveVal(state.val):
            state.k = self.k
        elif self.n < self.argslen:
            state.tag = State.CONTINUE
        else:
            self.finish(state)
                
    def receiveVal(self, val):
        self.vals[self.n - 1] = val
        return True

    def finish(self, state):
        (ok, retval) = self.computeResult(state)
        sys.stderr.write("EvalArgsCont.finish returning {0}\n".format(retval))
        if ok:
            state.tag = State.RETURN
            state.val = retval
            state.k = self.k
        else:
            self.k.excep = retval
            state.k = self.k
            

class SeqCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)


    def computeResult(self, state):
        return (True, self.vals[self.n - 1])

class UnaryOpCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)


    def computeResult(self, state):
        op = self.exp.spine[0].string
        val0 = self.vals[0]
        location = self.exp.location
        return state.interpreter.callUnaryOp(op, val0, location)

class BinaryOpCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)


    def computeResult(self, state):
        op = self.exp.spine[0].string
        val0 = self.vals[0]
        val1 = self.vals[1]
        location = self.exp.location
        return state.interpreter.callBinaryOp(op, val0, val1, location)

class TernaryOpCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)


    def computeResult(self, state):
        op = self.exp.spine[0].string
        val0 = self.vals[0]
        val1 = self.vals[1]
        val2 = self.vals[2]
        location = self.exp.location
        return state.interpreter.callTernaryOp(op, val0, val1, val2, location)

class ApplyCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)

    def computeResult(self, state):
         return state.interpreter.callApply(self.vals[0], self.vals[1:],  self.exp.spine[0].location)

class InvokeCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)

    def computeResult(self, state):
         return state.interpreter.callInvoke(self.vals[0], self.vals[1], self.vals[2:],  self.exp.spine[0].location)

class GetAttrCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)

    def computeResult(self, state):
         return state.interpreter.callGetAttr(self, self.vals,  self.exp.spine[0].location)
     

class ConcatCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)


    def computeResult(self, state):
        sb = StringBuffer()
        for v in self.vals:
            sb.append(str(v))
        return (True, str(sb))

class MkCont(EvalArgsCont):
    
    def __init__(self, op, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)
        self.op = op

    def computeResult(self, state):
        if self.op is SymbolTable.MKTUPLE:
            return (True, tuple(self.vals))
        elif self.op is SymbolTable.MKLIST:
            return (True, self.vals)
        else:
            return (True, dict(self.vals[i:i+2] for i in range(0, len(self.vals), 2)))


class PropCont(Continuation):
    
    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)


    def cont(self, state):
        if self.argslen > 0:
            state.tag = State.EVAL
            state.exp = self.args[self.n]
            state.env = self.env
        else:
            self.finish(state)

    
    def handleReturn(self, state):
        self.n += 1

        if not isinstance(state.val, bool):
            msg = '{0} is not a boolean in propsitional operator {1}'
            self.k.excep = PLambdaException(msg.format(state.val, self.exp.spine[0].location))
            state.k = self.k
            return

        if self.isStopValue(state.val) or self.n == self.argslen:
            self.finish(state)
        else:
            state.tag = State.CONTINUE


    def finish(self, state):
        state.tag = State.RETURN
        state.val = self.computeResult(state.val)
        state.k = self.k
  

class AndCont(PropCont):
    
    def __init__(self, exp, args, env, k):
        PropCont.__init__(self, exp, args, env, k)


    def isStopValue(self, val):
        return not val

    def computeResult(self, val):
        if val is None:
            return True
        else:
            return val


    
class OrCont(PropCont):
    
    def __init__(self, exp, args, env, k):
        PropCont.__init__(self, exp, args, env, k)


    def isStopValue(self, val):
        return val

    def computeResult(self, val):
        if val is None:
            return False
        else:
            return val


    
