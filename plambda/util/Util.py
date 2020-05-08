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
        sys.stderr.write('string2File(..., {0}, ...) threw {1}\n'.format(path, str(e)))
    return retval


def file2String(path):
    retval = None
    try:
        with open(path, 'r') as fp:
            retval = fp.read()
    except Exception as e:
        sys.stderr.write('file2String("{0}") threw {1}\n'.format(path, str(e)))
    return retval
