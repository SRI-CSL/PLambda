import os, sys
from antlr4 import *

sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))


from plambda.antlr4.PLambdaLexer import PLambdaLexer

from plambda.antlr4.PLambdaParser import PLambdaParser

from plambda.visitor.Visitor import Visitor


def main():
    if len(sys.argv) != 2:
        print 'Usage: {0} <plambda file>'.format(sys.argv[0])
    else:
        codelist = parseFromFile(sys.argv[1])
        for c in codelist:
            print str(c)
            print repr(c)
        return 0

import sys

def parseFromFile(filename):
    return parseFromStream(FileStream(filename), filename)
 
def parseFromString(string):
    return parseFromStream(InputStream(string), "stdin")

def parseFromStream(stream, source):
    lexer = PLambdaLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = PLambdaParser(stream)
    tree = parser.unit()
    visitor = Visitor(source)
    return visitor.visit(tree)
    
