# Generated from PLambda.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PLambdaParser import PLambdaParser
else:
    from PLambdaParser import PLambdaParser

# This class defines a complete listener for a parse tree produced by PLambdaParser.
class PLambdaListener(ParseTreeListener):

    # Enter a parse tree produced by PLambdaParser#unit.
    def enterUnit(self, ctx:PLambdaParser.UnitContext):
        pass

    # Exit a parse tree produced by PLambdaParser#unit.
    def exitUnit(self, ctx:PLambdaParser.UnitContext):
        pass


    # Enter a parse tree produced by PLambdaParser#seqExpression.
    def enterSeqExpression(self, ctx:PLambdaParser.SeqExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#seqExpression.
    def exitSeqExpression(self, ctx:PLambdaParser.SeqExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#letExpression.
    def enterLetExpression(self, ctx:PLambdaParser.LetExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#letExpression.
    def exitLetExpression(self, ctx:PLambdaParser.LetExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#defineExpression.
    def enterDefineExpression(self, ctx:PLambdaParser.DefineExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#defineExpression.
    def exitDefineExpression(self, ctx:PLambdaParser.DefineExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:PLambdaParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:PLambdaParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#invokeExpression.
    def enterInvokeExpression(self, ctx:PLambdaParser.InvokeExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#invokeExpression.
    def exitInvokeExpression(self, ctx:PLambdaParser.InvokeExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#applyExpression.
    def enterApplyExpression(self, ctx:PLambdaParser.ApplyExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#applyExpression.
    def exitApplyExpression(self, ctx:PLambdaParser.ApplyExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#dataExpression.
    def enterDataExpression(self, ctx:PLambdaParser.DataExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#dataExpression.
    def exitDataExpression(self, ctx:PLambdaParser.DataExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#unaryExpression.
    def enterUnaryExpression(self, ctx:PLambdaParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#unaryExpression.
    def exitUnaryExpression(self, ctx:PLambdaParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#binaryExpression.
    def enterBinaryExpression(self, ctx:PLambdaParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#binaryExpression.
    def exitBinaryExpression(self, ctx:PLambdaParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#ternaryExpression.
    def enterTernaryExpression(self, ctx:PLambdaParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#ternaryExpression.
    def exitTernaryExpression(self, ctx:PLambdaParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def enterOneOrMoreExpression(self, ctx:PLambdaParser.OneOrMoreExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def exitOneOrMoreExpression(self, ctx:PLambdaParser.OneOrMoreExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def enterTwoOrMoreExpression(self, ctx:PLambdaParser.TwoOrMoreExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def exitTwoOrMoreExpression(self, ctx:PLambdaParser.TwoOrMoreExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#naryExpression.
    def enterNaryExpression(self, ctx:PLambdaParser.NaryExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#naryExpression.
    def exitNaryExpression(self, ctx:PLambdaParser.NaryExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#tryExpression.
    def enterTryExpression(self, ctx:PLambdaParser.TryExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#tryExpression.
    def exitTryExpression(self, ctx:PLambdaParser.TryExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#forExpression.
    def enterForExpression(self, ctx:PLambdaParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#forExpression.
    def exitForExpression(self, ctx:PLambdaParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#stringLiteral.
    def enterStringLiteral(self, ctx:PLambdaParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by PLambdaParser#stringLiteral.
    def exitStringLiteral(self, ctx:PLambdaParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by PLambdaParser#identifierLiteral.
    def enterIdentifierLiteral(self, ctx:PLambdaParser.IdentifierLiteralContext):
        pass

    # Exit a parse tree produced by PLambdaParser#identifierLiteral.
    def exitIdentifierLiteral(self, ctx:PLambdaParser.IdentifierLiteralContext):
        pass


    # Enter a parse tree produced by PLambdaParser#noneLiteral.
    def enterNoneLiteral(self, ctx:PLambdaParser.NoneLiteralContext):
        pass

    # Exit a parse tree produced by PLambdaParser#noneLiteral.
    def exitNoneLiteral(self, ctx:PLambdaParser.NoneLiteralContext):
        pass


    # Enter a parse tree produced by PLambdaParser#parameterList.
    def enterParameterList(self, ctx:PLambdaParser.ParameterListContext):
        pass

    # Exit a parse tree produced by PLambdaParser#parameterList.
    def exitParameterList(self, ctx:PLambdaParser.ParameterListContext):
        pass


    # Enter a parse tree produced by PLambdaParser#parameter.
    def enterParameter(self, ctx:PLambdaParser.ParameterContext):
        pass

    # Exit a parse tree produced by PLambdaParser#parameter.
    def exitParameter(self, ctx:PLambdaParser.ParameterContext):
        pass


    # Enter a parse tree produced by PLambdaParser#bindingList.
    def enterBindingList(self, ctx:PLambdaParser.BindingListContext):
        pass

    # Exit a parse tree produced by PLambdaParser#bindingList.
    def exitBindingList(self, ctx:PLambdaParser.BindingListContext):
        pass


    # Enter a parse tree produced by PLambdaParser#bindingPair.
    def enterBindingPair(self, ctx:PLambdaParser.BindingPairContext):
        pass

    # Exit a parse tree produced by PLambdaParser#bindingPair.
    def exitBindingPair(self, ctx:PLambdaParser.BindingPairContext):
        pass


    # Enter a parse tree produced by PLambdaParser#catchExpression.
    def enterCatchExpression(self, ctx:PLambdaParser.CatchExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#catchExpression.
    def exitCatchExpression(self, ctx:PLambdaParser.CatchExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#rangeExpression.
    def enterRangeExpression(self, ctx:PLambdaParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by PLambdaParser#rangeExpression.
    def exitRangeExpression(self, ctx:PLambdaParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by PLambdaParser#data.
    def enterData(self, ctx:PLambdaParser.DataContext):
        pass

    # Exit a parse tree produced by PLambdaParser#data.
    def exitData(self, ctx:PLambdaParser.DataContext):
        pass


    # Enter a parse tree produced by PLambdaParser#token.
    def enterToken(self, ctx:PLambdaParser.TokenContext):
        pass

    # Exit a parse tree produced by PLambdaParser#token.
    def exitToken(self, ctx:PLambdaParser.TokenContext):
        pass



del PLambdaParser