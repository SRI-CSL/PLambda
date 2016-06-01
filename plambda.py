#!/usr/bin/env python

import sys


from plambda.eval.PLambda import rep

def main(argv):
    rep(argv[1] if len(sys.argv) == 2 else None)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
