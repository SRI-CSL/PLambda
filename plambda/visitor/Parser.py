""" Entry points into the antlr4 parser.
"""

import sys

from antlr4 import FileStream, InputStream, CommonTokenStream

from ..antlr4.PLambdaLexer import PLambdaLexer

from ..antlr4.PLambdaParser import PLambdaParser

from .Visitor import Visitor


def main():
    if len(sys.argv) != 2:
        print 'Usage: {0} <plambda file>'.format(sys.argv[0])
    else:
        codelist = parseFromFile(sys.argv[1])
        for c in codelist:
            print str(c)
            print repr(c)
        return 0

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
