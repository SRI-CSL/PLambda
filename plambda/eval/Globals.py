import inspect

import builtins

pythonGlobals = {}

def populateGlobals():
    d = builtins.__dict__
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
