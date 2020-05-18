"""  The python plambda actor library.
"""
import sys

from ..util.Util import (string2error, string2out)

debug = False

def send(target, sender, msg):
    """Send a message to actor 'target' from actor 'sender' with content 'msg'.

    This uses iop's underlying message format.
    """

    obytes = f'{target}\n{sender}\n{msg}'
    length = len(obytes)
    outgoing = f'{length}\n{obytes}'
    if debug:
        string2error(outgoing)
    string2out(outgoing, False)

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
            string2error(f'got {nobytes} bytes')
        ibytes = sys.stdin.read(int(nobytes))
        if debug:
            string2error(f'[[{ibytes}]]')
        (ok, sender, msg) = parseBytes(ibytes)
        if ok:
            return (sender, msg)
        return (None, ibytes)
    except KeyboardInterrupt:
        return None
    except Exception as e:
        string2error(f'{e}')
        return (None, None)
