from antlr4 import *

from src.gen.PLambdaLexer import PLambdaLexer

from src.gen.PLambdaParser import PLambdaParser

from src.visitor.Visitor import Visitor


def load(filename):
    input = FileStream(filename)
    lexer = PLambdaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PLambdaParser(stream)
    tree = parser.unit()
    visitor = Visitor(filename)
    return visitor.visit(tree)
    
