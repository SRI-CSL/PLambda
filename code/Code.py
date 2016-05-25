from StringBuffer import StringBuffer

class Code(object):

    def __init__(self, spine, filename, lineno):
        self.spine = spine
        self.filename = filename
        self.lineno = lineno
        self.str = self.toString()


    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}:{1}@{2}'.format(self.str, self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return self.str


    def toString(self):
        sb = StringBuffer()
        first = True
        sb.append('(')
        for c in self.spine:
            if first:
                first = False
            else:
                sb.append(' ')
            sb.append(c)
        sb.append(')')
        return str(sb)
    
