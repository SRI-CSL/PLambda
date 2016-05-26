from antlr4 import *

from src.gen.PLambdaLexer import PLambdaLexer

from src.gen.PLambdaParser import PLambdaParser

from src.visitor.Visitor import Visitor

import sys

def load(filename):
    input = FileStream(filename)
    lexer = PLambdaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PLambdaParser(stream)
    tree = parser.unit()
    visitor = Visitor(filename)
    return visitor.visit(tree)
    



def rep(filename):
    try:

        if filename is not None:
            codelist = load(filename)
            
        sys.stdout.write(WELCOME)
        
        while True:
            sys.stdout.write('> ')
            line = sys.stdin.readline().strip()
            if line == 'q':
                return 0
            elif line == '?':
                sys.stdout.write(INSTRUCTIONS)
            else:
                print line

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
    
