import sys

class SimpleDrone(object):
    """The simplest drone that can be managed by the python Actor.
    """

    debug = False
    
    def __init__(self, name):
        """Creates a drone with given name and defautl state.
        """
        self.name = name
        self.x = 0
        self.y = 0
        self.z = 0
        self.v = 0
        self.e = 10.0


    def initialize(self, x, y, z, v, e):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.v = float(v)
        self.e = float(e)
        return True
        

    def mv(self, x, y, z, v):
        self.x += float(x) * float(v)
        self.y += float(y) * float(v)
        self.z += float(z) * float(v)
        self.e -= 1.0
        return True

    def charge(self, amt):
        self.e += float(amt)
        return True
        
            
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.x, self.y, self.z, self.v, self.e)   
        
            

