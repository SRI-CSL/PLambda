import sys

# now that we are no longer supporting 2.7 we could ditch this I suppose.

def plambda_intern(string):
    return sys.intern(string)

def plambda_unicode(string):
    return  str(string)
