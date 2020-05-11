class Environment:

    def __init__(self, env = None):
        self.frame = {}
        self.next = env

    def extend(self, key, value):
        self.frame[key.string] = value
        return self

    def lookup(self, key):
        keystr = key.string
        env = self
        while env is not None:
            #print(f'looking up {keystr} in {env.frame}')
            if keystr in env.frame:
                return (True, env.frame[keystr])
            env = env.next
        return (False, None)
