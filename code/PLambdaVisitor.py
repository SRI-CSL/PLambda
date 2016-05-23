# Generated from java-escape by ANTLR 4.5
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


    # Visit a parse tree produced by PLambdaParser#quoteExpression.
    def visitQuoteExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#stringLiteral.
    def visitStringLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#do_binding_list.
    def visitDo_binding_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#do_binding_triple.
    def visitDo_binding_triple(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#do_exit_clause.
    def visitDo_exit_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameter_list.
    def visitParameter_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binding_list.
    def visitBinding_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binding_pair.
    def visitBinding_pair(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#catch_expression.
    def visitCatch_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#range_expression.
    def visitRange_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#data.
    def visitData(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#string.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#token.
    def visitToken(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#type_expression.
    def visitType_expression(self, ctx):
        return self.visitChildren(ctx)


