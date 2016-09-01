import sys, collections

from ..eval.PLambdaException import PLambdaException

from ..eval.Environment import Environment

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

    
class DefineCont(Continuation):

    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        name = self.args[0].string
        if self.argslen == 2:
            self.vals[0] = name
            state.tag = State.EVAL
            state.exp = self.args[1]
            state.env = self.env
        else:
            params = self.args[1]
            body = self.args[2]
            val = Closure(self.interpreter, params, body, env, self.exp.spine[0].location)
            state.interpreter.definitions[name] =  val
            state.tag = State.RETURN
            state.val = name
            state.k = self.k

            
    def handleReturn(self, state):
        name = self.vals[0]
        state.interpreter.definitions[name] =  state.val
        state.tag = State.RETURN
        state.val = name
        state.k = self.k
        
    
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
        

class TryCont(Continuation):

    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        state.tag = State.EVAL
        state.exp = self.args[0]
        state.env = self.env

    def handleReturn(self, state):
        pass

    def ret(self, state):
        if self.excep is None:
            """
            No exception was thrown during evaluation of the `try'
            body.  We simply invoke the next continuation in the chain.
            """
            state.k = self.k
        else:
            """
            Need to evaluate the catch with the param bound to self.excep.
            """
            catchexp = self.args[1].spine
            catchid = catchexp[1]
            catchbody =  catchexp[2]
            catchenv = Environment(self.env)
            state.tag = State.EVAL
            state.exp = catchbody
            state.env = catchenv.extend(catchid, self.excep)
            self.excep = None


class LetCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)
        self.lexicalEnv = Envronment(self.env)
        self.bindings = self.args[1].spine
        self.body = self.args[2]
        self.bindingslen = len(self.bindings)
        self.bindingexp = None
        self.bindingid = None
        

    def cont(self, state):
        if self.n < self.bindingslen:
            binding = self.bindings[self.n].spine
            self.bindingid = binding[0]
            self.bindingexp = binding[1]
            state.exp = self.bindingexp
        else:
            state.exp = self.body
            state.k = self.k

        state.env = self.lexicalEnv
        state.tag = State.CONTINUE
        


    def handleReturn(self, state):
        self.lexicalEnv.extend(self.bindingid, state.val)
        self.n += 1
        state.tag = State.CONTINUE
    
    

        
class ForCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)
        self.iterator = None
        self.length = None
        self.id = self.args[0]
        self.body = self.args[2]


    def cont(self, state):
        state.tag = State.EVAL
        state.exp = self.args[1]
        state.env = self.env

    def handleReturn(self, state):
        self.n += 1

        val = state.val
        
        if self.n == 1:

            if val is None:
                self.setException(state, "for target is None {0}".format(self.exp.spine[0].location))
                return
            if isinstance(val, int):
                self.iterator = iter(range(val))
                self.length = val
                if self.length == 0:
                    self.setReturnState(state, None)
                    return
            elif isinstance(val, collections.Iterable):
                self.iterator = iter(val)
                self.length = len(val)
                if self.length == 0:
                    self.setReturnState(state, None)
                    return
            else:
                self.setException(state, "for target is not iterable {0} {1}".format(val, self.exp.spine[0].location))
                return
        elif self.n  == self.length + 2:
            self.setReturnState(state, val)
        else:
            next = self.iterator.next()
            #sys.stderr.write('{0} out of {1}\n'.format(next, self.length))
            env = Environment(self.env)
            env.extend(self.id, next)
            state.tag = State.EVAL
            state.exp = self.body
            state.env = env
        

    def setException(self, state, msg):
        self.k.excep = PLambdaException(msg)
        self.setReturnState(state, None)

    def setReturnState(self, state, val):
        state.val = val
        state.k = self.k
        state.tag = State.RETURN



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

class Ambi1OpCont(EvalArgsCont):

    def __init__(self, op, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)
        self.op = op

    def computeResult(self, state):
        if self.op is SymbolTable.MINUS:
            if len(self.vals) == 2:
                return (True, self.vals[0] - self.vals[1])
            else:
                return (True, - self.vals[0])
        else:
            fmsg = 'Unrecognized ambi1 operation: {0}'
            emsg = fmsg.format(self.op)
            return (False, PLambdaException(emsg))


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
         return state.interpreter.callGetAttr(self.vals,  self.exp.spine[0].location)
     

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


    
