""" A Util module for odds and ends.
"""
import sys

def isString(data):
    return isinstance(data, str)

def isInteger(data):
    return isinstance(data, int)


def string2File(string, path, append):
    retval = False
    try:
        mode = 'a' if append else 'w'
        with open(path, mode) as fp:
            fp.write(string)
        retval = True
    except Exception as e:
        string2error(f'string2File(..., {path}, ...) threw {str(e)}')
    return retval


def file2String(path):
    retval = None
    try:
        with open(path, 'r') as fp:
            retval = fp.read()
    except Exception as e:
        string2error(f'file2String("{path}") threw {str(e)}')
    return retval


def string2error(string, newline=True):
    """Writes the string to standard error, followed by a newline if desired, and then a flush."""
    sys.stderr.write(string)
    if newline:
        sys.stderr.write('\n')
    sys.stderr.flush()


def string2out(string, newline=True):
    """Writes the string to standard out, followed by a newline if desired, and then a flush."""
    sys.stdout.write(string)
    if newline:
        sys.stdout.write('\n')
    sys.stdout.flush()
