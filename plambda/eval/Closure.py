from .Environment import Environment

class Closure:

    def __init__(self, interpreter, params, body, env, location):

        self.interpreter = interpreter
        self.params = params
        self.arity = len(params.spine)
        self.body = body
        self.env = env
        self.location = location

    def applyClosure(self, *args):
        nenv = Environment(self.env)
        for (p, v) in zip(self.params.spine, args):
            #print(f'extending: {p} --> {v}')
            nenv.extend(p, v)
        return  self.interpreter.eval(self.body, nenv)
