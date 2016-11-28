import inspect

try:
    import builtins as BuiltIns
except ImportError:
    import __builtin__ as BuiltIns


pythonGlobals = {}

def populateGlobals():
    d = BuiltIns.__dict__
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
