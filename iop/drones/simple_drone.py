import sys

class SimpleDrone(object):
    """The simplest drone that can be managed by the python Actor.
    """
    
    def __init__(self, name):
        """Creates a drone with given name and defautl state.
        """
        self.name = name
        self.x = 0
        self.y = 0
        self.e = 10


    def initialize(self, x, y, e):
        self.x = int(x)
        self.y = int(y)
        self.e = int(e)
        return True
        

    def mv(self, direction):
        if direction == 'E':
            self.x += 1
        elif direction == 'W':
            self.x -= 1
        elif direction == 'N':
            self.y += 1
        elif direction == 'S':
            self.y -= 1
        else:
            fmsg = 'SimpleDrone.mv unknown direction: {0}'
            emsg = fmsg.format(str(direction))
            sys.stderr.write(emsg)
            return False
        self.e -= 1
        return True

    def charge(self, amt):
        self.e += int(amt)
        return True
        
            
    def __str__(self):
        return '{0} {1} {2}'.format(self.x, self.y, self.e)   
        
            

