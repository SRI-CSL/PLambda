#!/usr/bin/env python

import sys


from plambda.actors.pyactor import launch

def main(argv):
    launch(argv[1] if len(sys.argv) == 2 else "dummy")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
