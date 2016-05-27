



class Environment(object):

    def __init__(self, env = None):
        self.env = {}
        self.next = env

    def extend(self, key, value):
        self.env[key] = value
        return self
    
    def lookup(self, key):
        env = self
        while env is not None:
            val = self.env.get(key)
            if val is not None:
                return val
            else:
                env = env.next
        return None
    
        
        
        

    
