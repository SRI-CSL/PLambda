"""  The python plambda actor library.
"""
import sys

debug = False

def send(target, sender, msg):
    """Send a message to actor 'target' from actor 'sender' with content 'msg'.

    This uses iop's underlying message format.
    """

    obytes = '{0}\n{1}\n{2}'.format(target, sender, msg)
    length = len(obytes)
    outgoing = '{0}\n{1}'.format(length, obytes)
    if debug:
        sys.stderr.write(outgoing)
        sys.stderr.write('\n')
    sys.stdout.write(outgoing)
    sys.stdout.flush()

def parseBytes(obytes):
    if obytes[-1] == '\n':
        obytes = obytes[:-1]
    if obytes[0] == '(' and obytes[-1] == ')':
        nl = obytes.find(' ')
        if nl > 0:
            return (True, obytes[1: nl], obytes[nl:-1])
    return (False, None, obytes)

def receive():
    """Reads an actor message and parses it as such.

    Returns (sender, msg) if successful,
    otherwise (None, bytes)
    """
    try:
        nobytes = sys.stdin.readline().strip()
        if debug:
            sys.stderr.write('got {0} bytes\n'.format(nobytes))
        ibytes = sys.stdin.read(int(nobytes))
        if debug:
            sys.stderr.write('[[{0}]]\n'.format(ibytes))
        (ok, sender, msg) = parseBytes(ibytes)
        if ok:
            return (sender, msg)
        else:
            return (None, ibytes)
    except KeyboardInterrupt:
        return None
    except Exception as e:
        sys.stderr.write('{0}\n'.format(e))
        return (None, None)
