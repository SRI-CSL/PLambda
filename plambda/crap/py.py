import sys



def plambda_intern(string):
    return sys.intern(string) if sys.version_info[0] > 2 else intern(string)

def plambda_unicode(string):
    return  str(string) if sys.version_info[0] > 2 else unicode(string)
