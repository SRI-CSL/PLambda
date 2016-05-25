from StringBuffer import StringBuffer

class Code(object):

    def __init__(self, spine, filename, lineno):
        self.spine = spine
        self.filename = filename
        self.lineno = lineno


    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}:{1}@{2}'.format(repr(self.spine), self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return str(self.spine)

    
