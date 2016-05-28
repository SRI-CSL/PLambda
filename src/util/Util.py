import sys


def isString(data):
    if (sys.version_info[0] == 3):
        return isinstance(data, str)
    return isinstance(data, basestring)


def isInteger(data):
    if (sys.version_info[0] == 3):
        return isinstance(data, int)
    return isinstance(data, (int, long))
