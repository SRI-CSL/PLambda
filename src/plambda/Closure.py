

class Closure(object):

    def __init__(self, interpreter, params, body, env):
        self.interpreter = interpreter
        self.params = params
        self.body = body
        self.env = env


    def applyClosure(self, *args):
        pass

    
