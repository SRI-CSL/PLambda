""" The Read-Evaluate-Print loop.
"""

import platform
import sys
import select
import time
import traceback

from ..util.StringBuffer import StringBuffer

from ..visitor.Parser import parseFromString
from ..eval.Interpreter  import Interpreter
from ..eval.PLambdaException import PLambdaException
from ..version import plambda_version

def main():
    rep(sys.argv[1] if len(sys.argv) == 2 else None)
    return 0


def snarf(delay):
    """ read as much as possible without blocking. (won't work on windows) """
    if platform.system == 'Windows':
        return sys.stdin.readline().strip()
    else:
        sb = StringBuffer()
        count = 0
        while True:
            while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = sys.stdin.readline()
                if line:
                    count += 1
                    sb.append(line)

            if sb.isempty():
                time.sleep(delay)
            else:
                if count > 1:
                    return str(sb)
                else:
                    return str(sb).strip()



def rep(filename):
    """The Read Eval Print loop for the plambda language.
    """
    interpreter = Interpreter()

    debug = False

    try:

        interpreter.load(filename)

        sys.stdout.write(WELCOME.format(plambda_version))

        while True:
            try:
                sys.stdout.write('> ')
                sys.stdout.flush()
                line = snarf(0.2)
                if line == 'q':
                    return 0
                elif line == 'v':
                    debug = not debug
                elif line == '?':
                    sys.stdout.write(INSTRUCTIONS)
                elif line == 'd':
                    interpreter.showDefinitions()
                elif line == 'u':
                    interpreter.showUIDs()
                elif line == 's':
                    interpreter.showCode()
                else:
                    if line:
                        if debug:
                            print('rep: line  = ', line)
                        code = parseFromString(line)
                        for c in code:
                            if c is not None:
                                if debug:
                                    print('rep: sexp  = ', c)
                                value = interpreter.evaluate(c)
                                if debug:
                                    print('rep: value = ', value)
                                print(value)
            except PLambdaException as e:
                print('PLambda.rep PLambdaException: ', e)
            except Exception as e:
                print('PLambda.rep Exception: ', e)
                traceback.print_exc(file=sys.stderr)

    except KeyboardInterrupt:
        return 0



WELCOME = """
Welcome to the PLambda interface to Python (version {0}), type ? for help.
"""

INSTRUCTIONS = """
Type one of the following:
\tany valid plambda expression to be evaluated, or
\tq to quit
\t? to see these instructions
\td to see the current definitions
\ts <name> to see the raw definition of <name>
\tu to see the current uids
\tv to toggle the degree of verbosity in error reports
"""
