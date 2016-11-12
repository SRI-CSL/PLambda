import sys

debug = False

def send(target, sender, msg):
    """Send a message to actor 'target' from actor 'sender' with content 'msg'.

    This uses iop's underlying message format.
    """

    bytes = '{0}\n{1}\n{2}'.format(target, sender, msg)
    length = len(bytes)
    outgoing = '{0}\n{1}'.format(len(bytes), bytes)
    if debug:
        sys.stderr.write(outgoing)
        sys.stderr.write('\n')
    sys.stdout.write(outgoing)
    sys.stdout.flush()

def parseBytes(bytes, nobytes):
    if bytes[-1] == '\n':
        bytes = bytes[:-1]
    if bytes[0] == '(' and bytes[-1] == ')':
            nl = bytes.find(' ')
            if nl > 0:
                return (True, bytes[1: nl], bytes[nl:-1])
    return (False, None, bytes)

def receive():
    """Reads an actor message and parses it as such.

    Returns (sender, msg) if successful,
    otherwise (None, bytes)
    """
    try:
        nobytes = sys.stdin.readline().strip()
        if debug:
            sys.stderr.write('got {0} bytes\n'.format(nobytes))
        bytes = sys.stdin.read(int(nobytes))
        if debug:
            sys.stderr.write('[[{0}]]\n'.format(bytes))
        (ok, sender, msg) = parseBytes(bytes, nobytes)
        if ok:
            return (sender, msg)
        else:
            return (None, bytes)
    except KeyboardInterrupt:
        return None
    except Exception as e:
        print e
        return (None, None)




