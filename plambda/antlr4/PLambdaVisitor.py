# Generated from PLambda.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PLambdaParser import PLambdaParser
else:
    from PLambdaParser import PLambdaParser

# This class defines a complete generic visitor for a parse tree produced by PLambdaParser.

class PLambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLambdaParser#unit.
    def visitUnit(self, ctx:PLambdaParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#seqExpression.
    def visitSeqExpression(self, ctx:PLambdaParser.SeqExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#letExpression.
    def visitLetExpression(self, ctx:PLambdaParser.LetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx:PLambdaParser.DefineExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:PLambdaParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#invokeExpression.
    def visitInvokeExpression(self, ctx:PLambdaParser.InvokeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#applyExpression.
    def visitApplyExpression(self, ctx:PLambdaParser.ApplyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#dataExpression.
    def visitDataExpression(self, ctx:PLambdaParser.DataExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#unaryExpression.
    def visitUnaryExpression(self, ctx:PLambdaParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binaryExpression.
    def visitBinaryExpression(self, ctx:PLambdaParser.BinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx:PLambdaParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def visitOneOrMoreExpression(self, ctx:PLambdaParser.OneOrMoreExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def visitTwoOrMoreExpression(self, ctx:PLambdaParser.TwoOrMoreExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#naryExpression.
    def visitNaryExpression(self, ctx:PLambdaParser.NaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#tryExpression.
    def visitTryExpression(self, ctx:PLambdaParser.TryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#forExpression.
    def visitForExpression(self, ctx:PLambdaParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#stringLiteral.
    def visitStringLiteral(self, ctx:PLambdaParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx:PLambdaParser.IdentifierLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#noneLiteral.
    def visitNoneLiteral(self, ctx:PLambdaParser.NoneLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameterList.
    def visitParameterList(self, ctx:PLambdaParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx:PLambdaParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#bindingList.
    def visitBindingList(self, ctx:PLambdaParser.BindingListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#bindingPair.
    def visitBindingPair(self, ctx:PLambdaParser.BindingPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#catchExpression.
    def visitCatchExpression(self, ctx:PLambdaParser.CatchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#rangeExpression.
    def visitRangeExpression(self, ctx:PLambdaParser.RangeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#data.
    def visitData(self, ctx:PLambdaParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#token.
    def visitToken(self, ctx:PLambdaParser.TokenContext):
        return self.visitChildren(ctx)



del PLambdaParser