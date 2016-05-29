import sys

from src.visitor.Parser import parseFromString
from src.plambda.Interpreter  import Interpreter
from src.plambda.PLambdaException import PLambdaException


def rep(filename):
    """The Read Eval Print loop for the plambda language.
    """
    interpreter = Interpreter()
    
    try:

        interpreter.load(filename)
        
        sys.stdout.write(WELCOME)
        
        while True:
            try:
                sys.stdout.write('> ')
                line = sys.stdin.readline().strip()
                if line == 'q':
                    return 0
                elif line == '?':
                    sys.stdout.write(INSTRUCTIONS)
                elif line == 'd':
                    interpreter.showDefinitions()
                elif line in ('s', 'u', 'v'):
                    print 'Coming soon(ish)'
                else:
                    if line:
                        print 'rep: line  = ', line
                        code = parseFromString(line)
                        for c in code:
                            if c is not None:
                                print 'rep: sexp  = ', c
                                value = interpreter.evaluate(c)
                                print 'rep: value = ', value
            except PLambdaException as e:
                print 'PLambda.rep PLambdaException: ', e
            except Exception as e:
                print 'PLambda.rep Exception: ', e
                
    except KeyboardInterrupt:
        return 0



WELCOME = """
Welcome to the PLambda interface to Python, type ? for help.
"""

INSTRUCTIONS="""
Type one of the following:
\tany valid plambda expression to be evaluated, or
\tq to quit  (or quit)
\t? to see these instructions
\td to see the current definitions
\ts <name> to see the raw definition of <name>
\tu to see the current uids
\tv to toggle the degree of verbosity in error reports
"""
    
