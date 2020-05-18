import collections.abc

from .PLambdaException import PLambdaException

from .Environment import Environment

from .Closure import Closure

from ..util.StringBuffer import StringBuffer

from ..util.Util import string2error

from .SymbolTable import SymbolTable

from .Flags import DONE, EVAL, RETURN, CONTINUE


class Continuation:


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
            self.msg = f'{exp.spine[0]} :'


    def ret(self, state):
        """ ret is deals with the exceptional case.

        By default, thrown exceptions propagated up the continuation
        chain.  Continuations that handle exceptions (TryCont and
        TopCont, currently) do so by overriding `ret'.
        """
        if self.excep is not None:
            if isinstance(self.excep, PLambdaException):
                self.excep.extendBT(self.info())
            self.k.excep = self.excep
            state.k = self.k
        else:
            self.handleReturn(state)


    def handleReturn(self, state):
        pass


    def info(self):
        sb = StringBuffer()
        if not self.vals:
            sb.append('\tcomputing result of top-level form ')
        elif self.n < len(self.vals):
            sb.append('\tcomputing result of ').append(self.exp.spine[0]).append(' form')
        else:
            sb.append('\tat  argument ').append(self.n).append(' of ').append(self.exp.spine[0]).append(' form')
        sb.append(' at ').append(self.exp.location)
        return str(sb)


class TopCont(Continuation):

    def __init__(self):
        Continuation.__init__(self)

    def cont(self, _):
        raise PLambdaException("Calling cont on a TopCont is forbidden")


    def ret(self, state):
        if self.excep is not None:
            string2error('FIXME: Debugger.handle(excep)')
            string2error(f'{self.excep}')
        state.tag = DONE


    def handleReturn(self, state):
        pass


class DefineCont(Continuation):

    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        name = self.args[0].string
        if self.argslen == 2:
            self.vals[0] = name
            state.tag = EVAL
            state.exp = self.args[1]
            state.env = self.env
        else:
            params = self.args[1]
            body = self.args[2]
            val = Closure(state.interpreter, params, body, self.env, self.exp.spine[0].location)
            state.interpreter.definitions[name] =  val
            state.tag = RETURN
            state.val = name
            state.k = self.k


    def handleReturn(self, state):
        name = self.vals[0]
        state.interpreter.definitions[name] =  state.val
        state.tag = RETURN
        state.val = name
        state.k = self.k


class IfCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        state.tag = EVAL
        state.exp = self.args[0]
        state.env = self.env

    def handleReturn(self, state):
        if not isinstance(state.val, bool):
            msg = f'{state.val} is not a boolean in conditional {self.exp.spine[0].location}'
            self.k.excep = PLambdaException(msg)
            state.k = self.k
            state.val = None
            return
        if state.val:
            state.tag = EVAL
            state.exp = self.args[1]
            state.env = self.env
        elif  self.argslen == 3:
            state.tag = EVAL
            state.exp = self.args[2]
            state.env = self.env
        else:
            state.tag = RETURN
            state.val = None

        state.k = self.k


class TryCont(Continuation):

    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        state.tag = EVAL
        state.exp = self.args[0]
        state.env = self.env

    def handleReturn(self, _):
        pass

    def ret(self, state):
        if self.excep is None:
            # No exception was thrown during evaluation of the `try'
            # body.  We simply invoke the next continuation in the chain.
            state.k = self.k
        else:
            # Need to evaluate the catch with the param bound to self.excep.
            catchexp = self.args[1].spine
            catchid = catchexp[1]
            catchbody =  catchexp[2]
            catchenv = Environment(self.env)
            state.tag = EVAL
            state.exp = catchbody
            state.env = catchenv.extend(catchid, self.excep)
            self.excep = None


class LetCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)
        self.lexicalEnv = Environment(self.env)
        self.bindings = self.args[0].spine
        self.body = self.args[1]
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
        state.tag = EVAL



    def handleReturn(self, state):
        self.lexicalEnv.extend(self.bindingid, state.val)
        self.n += 1
        state.tag = CONTINUE




class ForCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)
        self.iterator = None
        self.length = None
        self.id = self.args[0]
        self.body = self.args[2]


    def cont(self, state):
        state.tag = EVAL
        state.exp = self.args[1]
        state.env = self.env

    def handleReturn(self, state):

        val = state.val

        if self.n == 0:

            if val is None:
                self.setException(state, f'for target is None {self.exp.spine[0].location}')
                return
            if isinstance(val, int):
                self.iterator = iter(range(val))
                self.length = val
                if self.length == 0:
                    self.setReturnState(state, None)
            elif isinstance(val, collections.abc.Iterable):
                self.iterator = iter(val)
                self.length = len(val)
                if self.length == 0:
                    self.setReturnState(state, None)
            else:
                self.setException(state, f'for target is not iterable {val} {self.exp.spine[0].location}')
        elif self.n  == self.length + 1:
            self.setReturnState(state, val)
        else:
            nxt = next(self.iterator)
            env = Environment(self.env)
            env.extend(self.id, nxt)
            state.tag = EVAL
            state.exp = self.body
            state.env = env

        self.n += 1


    def setException(self, state, msg):
        self.k.excep = PLambdaException(msg)
        self.setReturnState(state, None)

    def setReturnState(self, state, val):
        state.val = val
        state.k = self.k
        state.tag = RETURN



class EvalArgsCont(Continuation):


    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)


    def cont(self, state):
        if self.argslen > 0:
            state.tag = EVAL
            state.exp = self.args[self.n]
            state.env = self.env
        else:
            self.finish(state)

    def handleReturn(self, state):
        self.n += 1

        if not self.receiveVal(state.val):
            state.k = self.k
        elif self.n < self.argslen:
            state.tag = CONTINUE
        else:
            self.finish(state)

    def receiveVal(self, val):
        self.vals[self.n - 1] = val
        return True

    def finish(self, state):
        (ok, retval) = self.computeResult(state)
        if ok:
            state.tag = RETURN
            state.val = retval
            state.k = self.k
        else:
            self.k.excep = retval
            state.k = self.k
            state.val = None

    def computeResult(self, _):
        raise PLambdaException('This needs to be over ridden!')


class SeqCont(EvalArgsCont):

    def __init__(self, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)


    def computeResult(self, _):
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

    def computeResult(self, _):
        if self.op is SymbolTable.MINUS:
            if len(self.vals) == 2:
                return (True, self.vals[0] - self.vals[1])
            return (True, - self.vals[0])

        msg = f'Unrecognized ambi1 operation: {self.op}'
        return (False, PLambdaException(msg))


class ApplyCont(Continuation):

    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)

    def cont(self, state):
        state.tag = EVAL
        state.exp = self.args[self.n]
        state.env = self.env

    def handleReturn(self, state):
        val = state.val

        if self.n == 0 and not isinstance(val, Closure) and not callable(val):
            self.k.excep = PLambdaException(f'Cannot apply {val}')
            state.k = self.k
            state.val = None
            return

        self.vals[self.n] = val
        self.n += 1

        if self.n < self.argslen:
            state.tag = CONTINUE
        else:
            func = self.vals[0]
            if isinstance(func, Closure):

                cargs = self.vals[1:]
                if not func.arity is len(cargs):
                    msg = f'number of arguments ({len(cargs)}) != closure arity({func.arity}): {self.info()}'
                    self.k.excep = PLambdaException(msg)
                    state.k = self.k
                    state.val = None
                else:
                    applyEnv = Environment(func.env)
                    for (key, value) in zip(func.params.spine, cargs):
                        applyEnv.extend(key, value)
                    state.tag = EVAL
                    state.exp = func.body
                    state.env = applyEnv
                    state.k = self.k
            else:
                (ok, retval) = state.interpreter.callCallable(func, self.vals[1:],  self.exp.spine[0].location)
                if ok:
                    state.tag = RETURN
                    state.val = retval
                    state.k = self.k
                else:
                    self.k.excep = retval
                    state.k = self.k
                    state.val = None


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


    def computeResult(self, _):
        sb = StringBuffer()
        for v in self.vals:
            sb.append(str(v))
        return (True, str(sb))

class MkCont(EvalArgsCont):

    def __init__(self, op, exp, args, env, k):
        EvalArgsCont.__init__(self, exp, args, env, k)
        self.op = op

    def computeResult(self, _):
        if self.op is SymbolTable.MKTUPLE:
            return (True, tuple(self.vals))
        if self.op is SymbolTable.MKLIST:
            return (True, self.vals)
        return (True, dict(self.vals[i:i+2] for i in range(0, len(self.vals), 2)))


class PropCont(Continuation):

    def __init__(self, exp, args, env, k):
        Continuation.__init__(self, exp, args, env, k)


    def cont(self, state):
        if self.argslen > 0:
            state.tag = EVAL
            state.exp = self.args[self.n]
            state.env = self.env
        else:
            self.finish(state)


    def handleReturn(self, state):
        self.n += 1

        if not isinstance(state.val, bool):
            msg = f'{state.val} is not a boolean in propositional operator {self.exp.spine[0].location}'
            self.k.excep = PLambdaException(msg)
            state.k = self.k
            state.val = None
            return

        if self.isStopValue(state.val) or self.n == self.argslen:
            self.finish(state)
        else:
            state.tag = CONTINUE


    def finish(self, state):
        state.tag = RETURN
        state.val = self.computeResult(state.val)
        state.k = self.k

    def isStopValue(self, _):
        raise PLambdaException('This needs to be over ridden!')

    def computeResult(self, _):
        raise PLambdaException('This needs to be over ridden!')


class AndCont(PropCont):

    def __init__(self, exp, args, env, k):
        PropCont.__init__(self, exp, args, env, k)


    def isStopValue(self, val):
        return not val

    def computeResult(self, val):
        if val is None:
            return True
        return val



class OrCont(PropCont):

    def __init__(self, exp, args, env, k):
        PropCont.__init__(self, exp, args, env, k)


    def isStopValue(self, val):
        return val

    def computeResult(self, val):
        if val is None:
            return False
        return val
