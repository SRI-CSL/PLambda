from ..util.StringBuffer import StringBuffer

class PLambdaException(Exception):

    def _init_(self, msg, backtrace=None, exception=None):
        self.msg = msg
        self.backtrace = backtrace
        self.exception = exception
        
    def _str_(self):
        return repr(self.msg)

    def _repr_(self):
        sb = StringBuffer()
        sb.append(self.msg)
        if self.backtrace:
            sb.append(' ').append(self.backtrace)
        if self.exception:
            sb.append(' ').append(self.exception)
        return str(sb)
        
    def extendBT(self, bt):
        self.bt = '{0}\n{1}'.format(self.bt, bt)
