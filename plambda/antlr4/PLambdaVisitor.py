# Generated from PLambda.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by PLambdaParser.

class PLambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLambdaParser#unit.
    def visitUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#seqExpression.
    def visitSeqExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#letExpression.
    def visitLetExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#invokeExpression.
    def visitInvokeExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#applyExpression.
    def visitApplyExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#dataExpression.
    def visitDataExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binaryExpression.
    def visitBinaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def visitOneOrMoreExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def visitTwoOrMoreExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#naryExpression.
    def visitNaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#tryExpression.
    def visitTryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#forExpression.
    def visitForExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#stringLiteral.
    def visitStringLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#noneLiteral.
    def visitNoneLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameterList.
    def visitParameterList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#bindingList.
    def visitBindingList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#bindingPair.
    def visitBindingPair(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#catchExpression.
    def visitCatchExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#rangeExpression.
    def visitRangeExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#data.
    def visitData(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#token.
    def visitToken(self, ctx):
        return self.visitChildren(ctx)


