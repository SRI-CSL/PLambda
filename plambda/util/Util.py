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
        string2error(f'string2File(..., {path}, ...) threw {str(e)}\n')
    return retval


def file2String(path):
    retval = None
    try:
        with open(path, 'r') as fp:
            retval = fp.read()
    except Exception as e:
        sys.stderr.write(f'file2String("{path}") threw {str(e)}\n')
    return retval


def string2error(string):
    sys.stderr.write(f'{string}\n')
    sys.stderr.flush()
