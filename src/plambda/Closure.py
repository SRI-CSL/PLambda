from Code import Atom



class Closure(object):

    def __init__(self, interpreter, params, body, env, a):

        assert(isinstance(a, Atom))

        self.interpreter = interpreter
        self.params = params
        self.body = body
        self.env = env
        #time to do some inheritance?
        self.filename = a.filename
        self.line = a.lineno

    def applyClosure(self, *args):
        pass

    
