import sys, time


global_trace = []

global_start_time = time.time()

global_trace_enabled = True

# do the name thing manually since 2.7 and 3 seem to differ about this
# and this is just a test...
def gtracer(name):
    def gtrace(fn):
        if not global_trace_enabled:
            return fn
        else:
            def gtraced(*args, **kwargs):
                global_trace.append(('>', name, time.time() - global_start_time, args, kwargs))
                retval = fn(*args, **kwargs)
                global_trace.append(('<', name, time.time() - global_start_time, args, kwargs))
                return retval
            return gtraced
    return gtrace


def printTrace():
    sys.stderr.write('tracing {0}\n'.format('enabled' if global_trace_enabled else 'not enabled'))
    for elem in global_trace:
        sys.stderr.write(str(elem))
        sys.stderr.write('\n')




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
        self.e = 10

    @gtracer('initialize')
    def initialize(self, x, y, e):
        self.x = int(x)
        self.y = int(y)
        self.e = int(e)
        return True

    @gtracer('mv')
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

    @gtracer('charge')
    def charge(self, amt):
        self.e += int(amt)
        return True


    def __str__(self):
        return '{0} {1} {2}'.format(self.x, self.y, self.e)
