from Code import Atom, Location



class Closure(object):

    def __init__(self, interpreter, params, body, env, location):

        assert(isinstance(a, Atom))

        self.interpreter = interpreter
        self.params = params
        self.body = body
        self.env = env
        self.location = location

    def applyClosure(self, *args):
        print "Closure.applyClosure coming soon to an interpreter near you"
        return None
    

    
