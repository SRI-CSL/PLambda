import sys

from src.visitor.Parser import parseFromFile, parseFromString


def rep(filename):
    try:

        if filename is not None:
            codelist = parseFromFile(filename)
            
        sys.stdout.write(WELCOME)
        
        while True:
            sys.stdout.write('> ')
            line = sys.stdin.readline().strip()
            if line == 'q':
                return 0
            elif line == '?':
                sys.stdout.write(INSTRUCTIONS)
            elif line in ('d', 's', 'u', 'v'):
                print 'Coming soon(ish)'
            else:
                print line
                code = parseFromString(line)
                print code

    except KeyboardInterrupt:
        return 0



WELCOME = """
Welcome to the PLambda interface to Python, type ? for help.
"""

INSTRUCTIONS="""
Type one of the following:
\tany valid jlambda expression to be evaluated, or
\tq to quit  (or quit)
\t? to see these instructions
\td to see the current definitions
\ts <name> to see the raw definition of <name>
\tu to see the current uids
\tv to toggle the degree of verbosity in error reports
"""
    
