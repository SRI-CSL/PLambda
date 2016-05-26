from antlr4 import *

from PLambdaLexer import PLambdaLexer

from PLambdaParser import PLambdaParser

from Visitor import Visitor


def load(filename):
    input = FileStream(filename)
    lexer = PLambdaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PLambdaParser(stream)
    tree = parser.unit()
    visitor = Visitor(filename)
    return visitor.visit(tree)
    
