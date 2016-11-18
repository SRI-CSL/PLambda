# iam: This is needed to stop python from treating 'print' as something special; rather than
# just a builtin. Wonder how much of this hackery is in our future?
#
from __future__ import print_function


import __builtin__

import inspect

pythonGlobals = {}

def populateGlobals():
    d = __builtin__.__dict__
    for x in d:
        try:
            vx = d.get(x)
            if  inspect.isclass(vx) and issubclass(vx, BaseException):
                continue
            if callable(vx):
                pythonGlobals[x] = vx
        except Exception:
            continue

populateGlobals()



#deprecated unless ...
_pythonGlobals = {
    'abs'           : abs,
    'all'           : all,
    'any'           : any,
    'basestring'    : basestring,
    'bin'           : bin,
    'bool'          : bool,
    'bytearray'     : bytearray,
    'callable'      : callable,
    'chr'           : chr,
    'classmethod'   : classmethod,
    'cmp'           : cmp,
    'compile'       : compile,
    'complex'       : complex,
    'delattr'       : delattr,
    'dict'          : dict,
    'dir'           : dir,
    'divmod'        : divmod,
    'enumerate'     : enumerate,
    'eval'          : eval,
    'execfile'      : execfile,
    'file'          : file,
    'filter'        : filter,
    'float'         : float,
    'format'        : format,
    'frozenset'     : frozenset,
    'getattr'       : getattr,
    'globals'       : globals,
    'hasattr'       : hasattr,
    'hash'          : hash,
    'help'          : help,
    'hex'           : hex,
    'id'            : id,
    'input'         : input,
    'int'           : int,
    'isinstance'    : isinstance,
    'issubclass'    : issubclass,
    'iter'          : iter,
    'len'           : len,
    'locals'        : locals,
    'long'          : long,
    'map'           : map,
    'max'           : max,
    'memoryview'    : memoryview,
    'min'           : min,
    'next'          : next,
    'object'        : object,
    'oct'           : oct,
    'open'          : open,
    'ord'           : ord,
    'pow'           : pow,
    'print'         : print,
    'property'      : property,
    'range'         : range,
    'raw_input'     : raw_input,
    'reduce'        : reduce,
    'reload'        : reload,
    'repr'          : repr,
    'reversed'      : reversed,
    'round'         : round,
    'set'           : set,
    'setattr'       : setattr,
    'slice'         : slice,
    'sorted'        : sorted,
    'staticmethod'  : staticmethod,
    'str'           : str,
    'sum'           : sum,
    'super'         : super,
    'tuple'         : tuple,
    'type'          : type,
    'unichr'        : unichr,
    'unicode'       : unicode,
    'vars'          : vars,
    'xrange'        : xrange,
    'zip'           : zip,
    '__import__'    : __import__
}


#may as well keep an eye on this.
for g in _pythonGlobals:
    if pythonGlobals.get(g) is None:
        print('Warning: {0} is missing from pythonGlobals\n'.format(g))
