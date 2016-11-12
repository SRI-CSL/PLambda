

class Environment(object):

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
            #print 'looking up {0} in {1}'.format(keystr, env.frame)
            if keystr in env.frame:
                return (True, env.frame[keystr])
            else:
                env = env.next
        return (False, None)






