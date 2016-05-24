# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .PLambdaListener import PLambdaListener
    from .PLambdaVisitor import PLambdaVisitor
else:
    from PLambdaListener import PLambdaListener
    from PLambdaVisitor import PLambdaVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"B\u00ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\3\2\6\2\34\n\2\r\2\16\2\35\3\3\3\3\3\3\6\3#\n\3\r\3")
        buf.write(u"\16\3$\3\3\3\3\3\3\3\3\3\3\3\3\6\3-\n\3\r\3\16\3.\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\5\3\67\n\3\3\3\6\3:\n\3\r\3\16\3")
        buf.write(u";\3\3\3\3\3\3\3\3\3\3\3\3\6\3D\n\3\r\3\16\3E\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\7\3O\n\3\f\3\16\3R\13\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\7\3Z\n\3\f\3\16\3]\13\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\5\3\177\n\3\3\4\3\4\7\4\u0083\n\4\f\4\16")
        buf.write(u"\4\u0086\13\4\3\4\3\4\3\5\3\5\3\6\3\6\6\6\u008e\n\6\r")
        buf.write(u"\6\16\6\u008f\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write(u"\3\b\6\b\u009d\n\b\r\b\16\b\u009e\3\b\3\b\3\t\3\t\3\n")
        buf.write(u"\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f")
        buf.write(u"\16\20\22\24\26\30\2\6\3\2:<\3\2;<\4\2;;==\4\2\5\5;;")
        buf.write(u"\u00b7\2\33\3\2\2\2\4~\3\2\2\2\6\u0080\3\2\2\2\b\u0089")
        buf.write(u"\3\2\2\2\n\u008b\3\2\2\2\f\u0093\3\2\2\2\16\u0098\3\2")
        buf.write(u"\2\2\20\u00a2\3\2\2\2\22\u00a4\3\2\2\2\24\u00a6\3\2\2")
        buf.write(u"\2\26\u00a8\3\2\2\2\30\u00aa\3\2\2\2\32\34\5\4\3\2\33")
        buf.write(u"\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write(u"\36\3\3\2\2\2\37 \7\3\2\2 \"\7\r\2\2!#\5\4\3\2\"!\3\2")
        buf.write(u"\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\7\4")
        buf.write(u"\2\2\'\177\3\2\2\2()\7\3\2\2)*\7\17\2\2*,\5\n\6\2+-\5")
        buf.write(u"\4\3\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\60\3")
        buf.write(u"\2\2\2\60\61\7\4\2\2\61\177\3\2\2\2\62\63\7\3\2\2\63")
        buf.write(u"\64\7\20\2\2\64\66\7;\2\2\65\67\5\6\4\2\66\65\3\2\2\2")
        buf.write(u"\66\67\3\2\2\2\679\3\2\2\28:\5\4\3\298\3\2\2\2:;\3\2")
        buf.write(u"\2\2;9\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\7\4\2\2>\177\3\2")
        buf.write(u"\2\2?@\7\3\2\2@A\7\21\2\2AC\5\6\4\2BD\5\4\3\2CB\3\2\2")
        buf.write(u"\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\7\4\2\2")
        buf.write(u"H\177\3\2\2\2IJ\7\3\2\2JK\7\23\2\2KL\5\4\3\2LP\5\4\3")
        buf.write(u"\2MO\5\4\3\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2")
        buf.write(u"QS\3\2\2\2RP\3\2\2\2ST\7\4\2\2T\177\3\2\2\2UV\7\3\2\2")
        buf.write(u"VW\7\22\2\2W[\5\4\3\2XZ\5\4\3\2YX\3\2\2\2Z]\3\2\2\2[")
        buf.write(u"Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\7\4\2\2_")
        buf.write(u"\177\3\2\2\2`a\7\3\2\2ab\7\5\2\2bc\5\22\n\2cd\7\4\2\2")
        buf.write(u"d\177\3\2\2\2ef\7\3\2\2fg\7\6\2\2gh\5\4\3\2hi\7\4\2\2")
        buf.write(u"i\177\3\2\2\2jk\7\3\2\2kl\7\7\2\2lm\5\4\3\2mn\5\4\3\2")
        buf.write(u"no\7\4\2\2o\177\3\2\2\2pq\7\3\2\2qr\7\b\2\2rs\5\4\3\2")
        buf.write(u"st\5\4\3\2tu\5\4\3\2uv\7\4\2\2v\177\3\2\2\2wx\7\3\2\2")
        buf.write(u"xy\7\'\2\2yz\5\24\13\2z{\7\4\2\2{\177\3\2\2\2|\177\7")
        buf.write(u"=\2\2}\177\7;\2\2~\37\3\2\2\2~(\3\2\2\2~\62\3\2\2\2~")
        buf.write(u"?\3\2\2\2~I\3\2\2\2~U\3\2\2\2~`\3\2\2\2~e\3\2\2\2~j\3")
        buf.write(u"\2\2\2~p\3\2\2\2~w\3\2\2\2~|\3\2\2\2~}\3\2\2\2\177\5")
        buf.write(u"\3\2\2\2\u0080\u0084\7\3\2\2\u0081\u0083\5\b\5\2\u0082")
        buf.write(u"\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2")
        buf.write(u"\2\u0084\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0084")
        buf.write(u"\3\2\2\2\u0087\u0088\7\4\2\2\u0088\7\3\2\2\2\u0089\u008a")
        buf.write(u"\7;\2\2\u008a\t\3\2\2\2\u008b\u008d\7\3\2\2\u008c\u008e")
        buf.write(u"\5\f\7\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write(u"\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2")
        buf.write(u"\2\u0091\u0092\7\4\2\2\u0092\13\3\2\2\2\u0093\u0094\7")
        buf.write(u"\3\2\2\u0094\u0095\5\b\5\2\u0095\u0096\5\4\3\2\u0096")
        buf.write(u"\u0097\7\4\2\2\u0097\r\3\2\2\2\u0098\u0099\7\3\2\2\u0099")
        buf.write(u"\u009a\7\32\2\2\u009a\u009c\5\b\5\2\u009b\u009d\5\4\3")
        buf.write(u"\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c")
        buf.write(u"\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write(u"\u00a1\7\4\2\2\u00a1\17\3\2\2\2\u00a2\u00a3\5\4\3\2\u00a3")
        buf.write(u"\21\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5\23\3\2\2\2\u00a6")
        buf.write(u"\u00a7\t\3\2\2\u00a7\25\3\2\2\2\u00a8\u00a9\t\4\2\2\u00a9")
        buf.write(u"\27\3\2\2\2\u00aa\u00ab\t\5\2\2\u00ab\31\3\2\2\2\16\35")
        buf.write(u"$.\66;EP[~\u0084\u008f\u009e")
        return buf.getvalue()


class PLambdaParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'null'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"PRIMITIVE_DATA_OP", 
                      u"UNARY_OP", u"BINARY_OP", u"TERNARY_OP", u"N_ARY_OP", 
                      u"AMBI1_OP", u"AMBI2_OP", u"NULL", u"SEQ", u"DO", 
                      u"LET", u"DEFINE", u"LAMBDA", u"APPLY", u"INVOKE", 
                      u"SINVOKE", u"OBJECT", u"FOR", u"ARRAY", u"MKARRAY", 
                      u"TRY", u"CATCH", u"BOOLEAN", u"BYTE", u"DOUBLE", 
                      u"CHAR", u"FLOAT", u"INT", u"LONG", u"SHORT", u"LOAD", 
                      u"ISNULL", u"ISOBJECT", u"GETUID", u"QUOTE", u"NOT", 
                      u"THROW", u"FETCH", u"NARROW", u"INSTANCEOF", u"AGET", 
                      u"LOOKUP", u"SETUID", u"ASET", u"UPDATE", u"SUPDATE", 
                      u"SETATTR", u"CONCAT", u"AND", u"OR", u"MINUS", u"IF", 
                      u"GETATTR", u"CHARACTER", u"ID", u"NUMBER", u"STRING", 
                      u"SYMBOL", u"LINE_COMMENT", u"NEW_LINE_COMMENT", u"NEW_COMMENT", 
                      u"WHITE_SPACE" ]

    RULE_unit = 0
    RULE_expression = 1
    RULE_parameter_list = 2
    RULE_parameter = 3
    RULE_binding_list = 4
    RULE_binding_pair = 5
    RULE_catch_expression = 6
    RULE_range_expression = 7
    RULE_data = 8
    RULE_string = 9
    RULE_token = 10
    RULE_type_expression = 11

    ruleNames =  [ u"unit", u"expression", u"parameter_list", u"parameter", 
                   u"binding_list", u"binding_pair", u"catch_expression", 
                   u"range_expression", u"data", u"string", u"token", u"type_expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PRIMITIVE_DATA_OP=3
    UNARY_OP=4
    BINARY_OP=5
    TERNARY_OP=6
    N_ARY_OP=7
    AMBI1_OP=8
    AMBI2_OP=9
    NULL=10
    SEQ=11
    DO=12
    LET=13
    DEFINE=14
    LAMBDA=15
    APPLY=16
    INVOKE=17
    SINVOKE=18
    OBJECT=19
    FOR=20
    ARRAY=21
    MKARRAY=22
    TRY=23
    CATCH=24
    BOOLEAN=25
    BYTE=26
    DOUBLE=27
    CHAR=28
    FLOAT=29
    INT=30
    LONG=31
    SHORT=32
    LOAD=33
    ISNULL=34
    ISOBJECT=35
    GETUID=36
    QUOTE=37
    NOT=38
    THROW=39
    FETCH=40
    NARROW=41
    INSTANCEOF=42
    AGET=43
    LOOKUP=44
    SETUID=45
    ASET=46
    UPDATE=47
    SUPDATE=48
    SETATTR=49
    CONCAT=50
    AND=51
    OR=52
    MINUS=53
    IF=54
    GETATTR=55
    CHARACTER=56
    ID=57
    NUMBER=58
    STRING=59
    SYMBOL=60
    LINE_COMMENT=61
    NEW_LINE_COMMENT=62
    NEW_COMMENT=63
    WHITE_SPACE=64

    def __init__(self, input):
        super(PLambdaParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class UnitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.UnitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_unit

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterUnit(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitUnit(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = PLambdaParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.expression()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLambdaParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(PLambdaParser.ExpressionContext, self).copyFrom(ctx)



    class LambdaExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.LambdaExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(PLambdaParser.LAMBDA, 0)
        def parameter_list(self):
            return self.getTypedRuleContext(PLambdaParser.Parameter_listContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterLambdaExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitLambdaExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitLambdaExpression(self)
            else:
                return visitor.visitChildren(self)


    class SeqExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.SeqExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def SEQ(self):
            return self.getToken(PLambdaParser.SEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterSeqExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitSeqExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitSeqExpression(self)
            else:
                return visitor.visitChildren(self)


    class ApplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.ApplyExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def APPLY(self):
            return self.getToken(PLambdaParser.APPLY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterApplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitApplyExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitApplyExpression(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.BinaryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BINARY_OP(self):
            return self.getToken(PLambdaParser.BINARY_OP, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitBinaryExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitBinaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.StringLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PLambdaParser.STRING, 0)

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitStringLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class DefineExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.DefineExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DEFINE(self):
            return self.getToken(PLambdaParser.DEFINE, 0)
        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)
        def parameter_list(self):
            return self.getTypedRuleContext(PLambdaParser.Parameter_listContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterDefineExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitDefineExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitDefineExpression(self)
            else:
                return visitor.visitChildren(self)


    class LetExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.LetExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(PLambdaParser.LET, 0)
        def binding_list(self):
            return self.getTypedRuleContext(PLambdaParser.Binding_listContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterLetExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitLetExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitLetExpression(self)
            else:
                return visitor.visitChildren(self)


    class QuoteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.QuoteExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def QUOTE(self):
            return self.getToken(PLambdaParser.QUOTE, 0)
        def string(self):
            return self.getTypedRuleContext(PLambdaParser.StringContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterQuoteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitQuoteExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitQuoteExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.IdentifierLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterIdentifierLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitIdentifierLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitIdentifierLiteral(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.UnaryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UNARY_OP(self):
            return self.getToken(PLambdaParser.UNARY_OP, 0)
        def expression(self):
            return self.getTypedRuleContext(PLambdaParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.TernaryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TERNARY_OP(self):
            return self.getToken(PLambdaParser.TERNARY_OP, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitTernaryExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class InvokeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.InvokeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INVOKE(self):
            return self.getToken(PLambdaParser.INVOKE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterInvokeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitInvokeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitInvokeExpression(self)
            else:
                return visitor.visitChildren(self)


    class DataExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.DataExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PRIMITIVE_DATA_OP(self):
            return self.getToken(PLambdaParser.PRIMITIVE_DATA_OP, 0)
        def data(self):
            return self.getTypedRuleContext(PLambdaParser.DataContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterDataExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitDataExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitDataExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = PLambdaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 124
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = PLambdaParser.SeqExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(PLambdaParser.T__0)
                self.state = 30
                self.match(PLambdaParser.SEQ)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 31
                    self.expression()
                    self.state = 34 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 36
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 2:
                localctx = PLambdaParser.LetExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(PLambdaParser.T__0)
                self.state = 39
                self.match(PLambdaParser.LET)
                self.state = 40
                self.binding_list()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 41
                    self.expression()
                    self.state = 44 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 46
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 3:
                localctx = PLambdaParser.DefineExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(PLambdaParser.T__0)
                self.state = 49
                self.match(PLambdaParser.DEFINE)
                self.state = 50
                self.match(PLambdaParser.ID)
                self.state = 52
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 51
                    self.parameter_list()


                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 54
                    self.expression()
                    self.state = 57 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 59
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 4:
                localctx = PLambdaParser.LambdaExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.match(PLambdaParser.T__0)
                self.state = 62
                self.match(PLambdaParser.LAMBDA)
                self.state = 63
                self.parameter_list()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 64
                    self.expression()
                    self.state = 67 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 69
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 5:
                localctx = PLambdaParser.InvokeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.match(PLambdaParser.T__0)
                self.state = 72
                self.match(PLambdaParser.INVOKE)
                self.state = 73
                self.expression()
                self.state = 74
                self.expression()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 75
                    self.expression()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 6:
                localctx = PLambdaParser.ApplyExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.match(PLambdaParser.T__0)
                self.state = 84
                self.match(PLambdaParser.APPLY)
                self.state = 85
                self.expression()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 86
                    self.expression()
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 92
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 7:
                localctx = PLambdaParser.DataExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.match(PLambdaParser.T__0)
                self.state = 95
                self.match(PLambdaParser.PRIMITIVE_DATA_OP)
                self.state = 96
                self.data()
                self.state = 97
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 8:
                localctx = PLambdaParser.UnaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.match(PLambdaParser.T__0)
                self.state = 100
                self.match(PLambdaParser.UNARY_OP)
                self.state = 101
                self.expression()
                self.state = 102
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 9:
                localctx = PLambdaParser.BinaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 104
                self.match(PLambdaParser.T__0)
                self.state = 105
                self.match(PLambdaParser.BINARY_OP)
                self.state = 106
                self.expression()
                self.state = 107
                self.expression()
                self.state = 108
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 10:
                localctx = PLambdaParser.TernaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 110
                self.match(PLambdaParser.T__0)
                self.state = 111
                self.match(PLambdaParser.TERNARY_OP)
                self.state = 112
                self.expression()
                self.state = 113
                self.expression()
                self.state = 114
                self.expression()
                self.state = 115
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 11:
                localctx = PLambdaParser.QuoteExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 117
                self.match(PLambdaParser.T__0)
                self.state = 118
                self.match(PLambdaParser.QUOTE)
                self.state = 119
                self.string()
                self.state = 120
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 12:
                localctx = PLambdaParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 122
                self.match(PLambdaParser.STRING)
                pass

            elif la_ == 13:
                localctx = PLambdaParser.IdentifierLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 123
                self.match(PLambdaParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Parameter_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ParameterContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_parameter_list

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterParameter_list(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitParameter_list(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = PLambdaParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(PLambdaParser.T__0)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PLambdaParser.ID:
                self.state = 127
                self.parameter()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.ParameterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)

        def getRuleIndex(self):
            return PLambdaParser.RULE_parameter

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterParameter(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitParameter(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = PLambdaParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(PLambdaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def binding_pair(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.Binding_pairContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.Binding_pairContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_binding_list

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterBinding_list(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitBinding_list(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitBinding_list(self)
            else:
                return visitor.visitChildren(self)




    def binding_list(self):

        localctx = PLambdaParser.Binding_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_binding_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(PLambdaParser.T__0)
            self.state = 139 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.binding_pair()
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PLambdaParser.T__0):
                    break

            self.state = 143
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binding_pairContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Binding_pairContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(PLambdaParser.ParameterContext,0)


        def expression(self):
            return self.getTypedRuleContext(PLambdaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLambdaParser.RULE_binding_pair

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterBinding_pair(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitBinding_pair(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitBinding_pair(self)
            else:
                return visitor.visitChildren(self)




    def binding_pair(self):

        localctx = PLambdaParser.Binding_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_binding_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(PLambdaParser.T__0)
            self.state = 146
            self.parameter()
            self.state = 147
            self.expression()
            self.state = 148
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Catch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(PLambdaParser.CATCH, 0)

        def parameter(self):
            return self.getTypedRuleContext(PLambdaParser.ParameterContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_catch_expression

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterCatch_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitCatch_expression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitCatch_expression(self)
            else:
                return visitor.visitChildren(self)




    def catch_expression(self):

        localctx = PLambdaParser.Catch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_catch_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(PLambdaParser.T__0)
            self.state = 151
            self.match(PLambdaParser.CATCH)
            self.state = 152
            self.parameter()
            self.state = 154 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 153
                self.expression()
                self.state = 156 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                    break

            self.state = 158
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Range_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PLambdaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLambdaParser.RULE_range_expression

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterRange_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitRange_expression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitRange_expression(self)
            else:
                return visitor.visitChildren(self)




    def range_expression(self):

        localctx = PLambdaParser.Range_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_range_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.DataContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PLambdaParser.NUMBER, 0)

        def CHARACTER(self):
            return self.getToken(PLambdaParser.CHARACTER, 0)

        def getRuleIndex(self):
            return PLambdaParser.RULE_data

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterData(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitData(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = PLambdaParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.CHARACTER) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.NUMBER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.StringContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PLambdaParser.NUMBER, 0)

        def getRuleIndex(self):
            return PLambdaParser.RULE_string

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterString(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitString(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = PLambdaParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==PLambdaParser.ID or _la==PLambdaParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.TokenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)

        def STRING(self):
            return self.getToken(PLambdaParser.STRING, 0)

        def getRuleIndex(self):
            return PLambdaParser.RULE_token

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterToken(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitToken(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitToken(self)
            else:
                return visitor.visitChildren(self)




    def token(self):

        localctx = PLambdaParser.TokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_token)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==PLambdaParser.ID or _la==PLambdaParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Type_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_DATA_OP(self):
            return self.getToken(PLambdaParser.PRIMITIVE_DATA_OP, 0)

        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)

        def getRuleIndex(self):
            return PLambdaParser.RULE_type_expression

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterType_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitType_expression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitType_expression(self)
            else:
                return visitor.visitChildren(self)




    def type_expression(self):

        localctx = PLambdaParser.Type_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==PLambdaParser.PRIMITIVE_DATA_OP or _la==PLambdaParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




