



class Environment(object):

    def __init__(self, env = None):
        self.env = {}
        self.next = env

    def extend(self, key, value):
        self.env[key] = value

    def lookup(self, key):
        val = self.env.get(key)
        if val is not None or self.next is None:
            return val
        else:
            return self.next.lookup(key)

        
        
        

    
