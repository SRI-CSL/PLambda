

class ParseError(Exception):

    def _init_(self, msg):
        self.msg = msg

    def _str_(self):
        return repr(self.msg)

    
