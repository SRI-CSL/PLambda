from antlr4 import *

from plam.antlr4.PLambdaLexer import PLambdaLexer

from plam.antlr4.PLambdaParser import PLambdaParser

from plam.visitor.Visitor import Visitor

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
    
