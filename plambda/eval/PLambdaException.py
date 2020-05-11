from ..util.StringBuffer import StringBuffer

class PLambdaException(Exception):

    def __init__(self, msg, backtrace=None, exception=None):
        Exception.__init__(self)
        self.msg = msg
        self.backtrace = backtrace
        self.exception = exception

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        sb = StringBuffer()
        sb.append(self.msg)
        if self.backtrace:
            sb.append(' ').append(self.backtrace)
        if self.exception:
            sb.append(' ').append(self.exception)
        return str(sb)

    def extendBT(self, bt):
        self.backtrace = f'{self.backtrace}\n{bt}'
