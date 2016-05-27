



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
            if key in self.env:
                return (True, self.env.get(key))
            else:
                env = env.next
        return (False, None)
    
        
        
        

    
