#!/usr/bin/env python

import sys


from plam.visitor.Parser import parseFromFile

def main(argv):

    codelist = parseFromFile(argv[1])
    for c in codelist:
        print str(c)
        print repr(c)
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: {0} <plambda file>'.format(sys.argv[0])
    else:
        sys.exit(main(sys.argv))
