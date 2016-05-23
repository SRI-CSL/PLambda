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
        buf.write(u"B\u00ca\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\3\2\6\2\"\n\2\r\2\16\2")
        buf.write(u"#\3\3\3\3\3\3\6\3)\n\3\r\3\16\3*\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\6\3\63\n\3\r\3\16\3\64\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write(u"\3=\n\3\3\3\6\3@\n\3\r\3\16\3A\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\6\3J\n\3\r\3\16\3K\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write(u"U\n\3\f\3\16\3X\13\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3`\n\3")
        buf.write(u"\f\3\16\3c\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0085\n\3")
        buf.write(u"\3\4\3\4\6\4\u0089\n\4\r\4\16\4\u008a\3\4\3\4\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\6\3\6\3\6\6\6\u0098\n\6\r\6\16\6\u0099")
        buf.write(u"\3\6\3\6\3\7\3\7\7\7\u00a0\n\7\f\7\16\7\u00a3\13\7\3")
        buf.write(u"\7\3\7\3\b\3\b\3\t\3\t\6\t\u00ab\n\t\r\t\16\t\u00ac\3")
        buf.write(u"\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\6\13\u00ba")
        buf.write(u"\n\13\r\13\16\13\u00bb\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write(u"\3\16\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\34\36\2\6\3\2:<\3\2;<\4\2;;==\4\2")
        buf.write(u"\5\5;;\u00d3\2!\3\2\2\2\4\u0084\3\2\2\2\6\u0086\3\2\2")
        buf.write(u"\2\b\u008e\3\2\2\2\n\u0094\3\2\2\2\f\u009d\3\2\2\2\16")
        buf.write(u"\u00a6\3\2\2\2\20\u00a8\3\2\2\2\22\u00b0\3\2\2\2\24\u00b5")
        buf.write(u"\3\2\2\2\26\u00bf\3\2\2\2\30\u00c1\3\2\2\2\32\u00c3\3")
        buf.write(u"\2\2\2\34\u00c5\3\2\2\2\36\u00c7\3\2\2\2 \"\5\4\3\2!")
        buf.write(u" \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\3\3\2\2\2%")
        buf.write(u"&\7\3\2\2&(\7\r\2\2\')\5\4\3\2(\'\3\2\2\2)*\3\2\2\2*")
        buf.write(u"(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7\4\2\2-\u0085\3\2\2")
        buf.write(u"\2./\7\3\2\2/\60\7\17\2\2\60\62\5\20\t\2\61\63\5\4\3")
        buf.write(u"\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3")
        buf.write(u"\2\2\2\65\66\3\2\2\2\66\67\7\4\2\2\67\u0085\3\2\2\28")
        buf.write(u"9\7\3\2\29:\7\20\2\2:<\7;\2\2;=\5\f\7\2<;\3\2\2\2<=\3")
        buf.write(u"\2\2\2=?\3\2\2\2>@\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?\3\2")
        buf.write(u"\2\2AB\3\2\2\2BC\3\2\2\2CD\7\4\2\2D\u0085\3\2\2\2EF\7")
        buf.write(u"\3\2\2FG\7\21\2\2GI\5\f\7\2HJ\5\4\3\2IH\3\2\2\2JK\3\2")
        buf.write(u"\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\4\2\2N\u0085\3")
        buf.write(u"\2\2\2OP\7\3\2\2PQ\7\23\2\2QR\5\4\3\2RV\5\4\3\2SU\5\4")
        buf.write(u"\3\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2")
        buf.write(u"\2XV\3\2\2\2YZ\7\4\2\2Z\u0085\3\2\2\2[\\\7\3\2\2\\]\7")
        buf.write(u"\22\2\2]a\5\4\3\2^`\5\4\3\2_^\3\2\2\2`c\3\2\2\2a_\3\2")
        buf.write(u"\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7\4\2\2e\u0085\3")
        buf.write(u"\2\2\2fg\7\3\2\2gh\7\5\2\2hi\5\30\r\2ij\7\4\2\2j\u0085")
        buf.write(u"\3\2\2\2kl\7\3\2\2lm\7\6\2\2mn\5\4\3\2no\7\4\2\2o\u0085")
        buf.write(u"\3\2\2\2pq\7\3\2\2qr\7\7\2\2rs\5\4\3\2st\5\4\3\2tu\7")
        buf.write(u"\4\2\2u\u0085\3\2\2\2vw\7\3\2\2wx\7\b\2\2xy\5\4\3\2y")
        buf.write(u"z\5\4\3\2z{\5\4\3\2{|\7\4\2\2|\u0085\3\2\2\2}~\7\3\2")
        buf.write(u"\2~\177\7\'\2\2\177\u0080\5\32\16\2\u0080\u0081\7\4\2")
        buf.write(u"\2\u0081\u0085\3\2\2\2\u0082\u0085\7=\2\2\u0083\u0085")
        buf.write(u"\7;\2\2\u0084%\3\2\2\2\u0084.\3\2\2\2\u00848\3\2\2\2")
        buf.write(u"\u0084E\3\2\2\2\u0084O\3\2\2\2\u0084[\3\2\2\2\u0084f")
        buf.write(u"\3\2\2\2\u0084k\3\2\2\2\u0084p\3\2\2\2\u0084v\3\2\2\2")
        buf.write(u"\u0084}\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2")
        buf.write(u"\2\u0085\5\3\2\2\2\u0086\u0088\7\3\2\2\u0087\u0089\5")
        buf.write(u"\b\5\2\u0088\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write(u"\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2")
        buf.write(u"\2\u008c\u008d\7\4\2\2\u008d\7\3\2\2\2\u008e\u008f\7")
        buf.write(u"\3\2\2\u008f\u0090\5\16\b\2\u0090\u0091\5\4\3\2\u0091")
        buf.write(u"\u0092\5\4\3\2\u0092\u0093\7\4\2\2\u0093\t\3\2\2\2\u0094")
        buf.write(u"\u0095\7\3\2\2\u0095\u0097\5\4\3\2\u0096\u0098\5\4\3")
        buf.write(u"\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097")
        buf.write(u"\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write(u"\u009c\7\4\2\2\u009c\13\3\2\2\2\u009d\u00a1\7\3\2\2\u009e")
        buf.write(u"\u00a0\5\16\b\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2")
        buf.write(u"\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write(u"\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7\4\2\2\u00a5")
        buf.write(u"\r\3\2\2\2\u00a6\u00a7\7;\2\2\u00a7\17\3\2\2\2\u00a8")
        buf.write(u"\u00aa\7\3\2\2\u00a9\u00ab\5\22\n\2\u00aa\u00a9\3\2\2")
        buf.write(u"\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write(u"\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7\4\2\2\u00af")
        buf.write(u"\21\3\2\2\2\u00b0\u00b1\7\3\2\2\u00b1\u00b2\5\16\b\2")
        buf.write(u"\u00b2\u00b3\5\4\3\2\u00b3\u00b4\7\4\2\2\u00b4\23\3\2")
        buf.write(u"\2\2\u00b5\u00b6\7\3\2\2\u00b6\u00b7\7\32\2\2\u00b7\u00b9")
        buf.write(u"\5\16\b\2\u00b8\u00ba\5\4\3\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write(u"\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2")
        buf.write(u"\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\7\4\2\2\u00be\25\3")
        buf.write(u"\2\2\2\u00bf\u00c0\5\4\3\2\u00c0\27\3\2\2\2\u00c1\u00c2")
        buf.write(u"\t\2\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\t\3\2\2\u00c4\33")
        buf.write(u"\3\2\2\2\u00c5\u00c6\t\4\2\2\u00c6\35\3\2\2\2\u00c7\u00c8")
        buf.write(u"\t\5\2\2\u00c8\37\3\2\2\2\20#*\64<AKVa\u0084\u008a\u0099")
        buf.write(u"\u00a1\u00ac\u00bb")
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
    RULE_do_binding_list = 2
    RULE_do_binding_triple = 3
    RULE_do_exit_clause = 4
    RULE_parameter_list = 5
    RULE_parameter = 6
    RULE_binding_list = 7
    RULE_binding_pair = 8
    RULE_catch_expression = 9
    RULE_range_expression = 10
    RULE_data = 11
    RULE_string = 12
    RULE_token = 13
    RULE_type_expression = 14

    ruleNames =  [ u"unit", u"expression", u"do_binding_list", u"do_binding_triple", 
                   u"do_exit_clause", u"parameter_list", u"parameter", u"binding_list", 
                   u"binding_pair", u"catch_expression", u"range_expression", 
                   u"data", u"string", u"token", u"type_expression" ]

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
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.expression()
                self.state = 33 
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
            self.state = 130
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = PLambdaParser.SeqExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(PLambdaParser.T__0)
                self.state = 36
                self.match(PLambdaParser.SEQ)
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 37
                    self.expression()
                    self.state = 40 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 42
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 2:
                localctx = PLambdaParser.LetExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(PLambdaParser.T__0)
                self.state = 45
                self.match(PLambdaParser.LET)
                self.state = 46
                self.binding_list()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 47
                    self.expression()
                    self.state = 50 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 52
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 3:
                localctx = PLambdaParser.DefineExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(PLambdaParser.T__0)
                self.state = 55
                self.match(PLambdaParser.DEFINE)
                self.state = 56
                self.match(PLambdaParser.ID)
                self.state = 58
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 57
                    self.parameter_list()


                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 60
                    self.expression()
                    self.state = 63 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 65
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 4:
                localctx = PLambdaParser.LambdaExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.match(PLambdaParser.T__0)
                self.state = 68
                self.match(PLambdaParser.LAMBDA)
                self.state = 69
                self.parameter_list()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 70
                    self.expression()
                    self.state = 73 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 75
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 5:
                localctx = PLambdaParser.InvokeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(PLambdaParser.T__0)
                self.state = 78
                self.match(PLambdaParser.INVOKE)
                self.state = 79
                self.expression()
                self.state = 80
                self.expression()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 81
                    self.expression()
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 6:
                localctx = PLambdaParser.ApplyExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.match(PLambdaParser.T__0)
                self.state = 90
                self.match(PLambdaParser.APPLY)
                self.state = 91
                self.expression()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 92
                    self.expression()
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 98
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 7:
                localctx = PLambdaParser.DataExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self.match(PLambdaParser.T__0)
                self.state = 101
                self.match(PLambdaParser.PRIMITIVE_DATA_OP)
                self.state = 102
                self.data()
                self.state = 103
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 8:
                localctx = PLambdaParser.UnaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 105
                self.match(PLambdaParser.T__0)
                self.state = 106
                self.match(PLambdaParser.UNARY_OP)
                self.state = 107
                self.expression()
                self.state = 108
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 9:
                localctx = PLambdaParser.BinaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 110
                self.match(PLambdaParser.T__0)
                self.state = 111
                self.match(PLambdaParser.BINARY_OP)
                self.state = 112
                self.expression()
                self.state = 113
                self.expression()
                self.state = 114
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 10:
                localctx = PLambdaParser.TernaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 116
                self.match(PLambdaParser.T__0)
                self.state = 117
                self.match(PLambdaParser.TERNARY_OP)
                self.state = 118
                self.expression()
                self.state = 119
                self.expression()
                self.state = 120
                self.expression()
                self.state = 121
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 11:
                localctx = PLambdaParser.QuoteExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 123
                self.match(PLambdaParser.T__0)
                self.state = 124
                self.match(PLambdaParser.QUOTE)
                self.state = 125
                self.string()
                self.state = 126
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 12:
                localctx = PLambdaParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 128
                self.match(PLambdaParser.STRING)
                pass

            elif la_ == 13:
                localctx = PLambdaParser.IdentifierLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 129
                self.match(PLambdaParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Do_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def do_binding_triple(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.Do_binding_tripleContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.Do_binding_tripleContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_do_binding_list

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterDo_binding_list(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitDo_binding_list(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitDo_binding_list(self)
            else:
                return visitor.visitChildren(self)




    def do_binding_list(self):

        localctx = PLambdaParser.Do_binding_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_do_binding_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(PLambdaParser.T__0)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.do_binding_triple()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PLambdaParser.T__0):
                    break

            self.state = 138
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_binding_tripleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Do_binding_tripleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(PLambdaParser.ParameterContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_do_binding_triple

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterDo_binding_triple(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitDo_binding_triple(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitDo_binding_triple(self)
            else:
                return visitor.visitChildren(self)




    def do_binding_triple(self):

        localctx = PLambdaParser.Do_binding_tripleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_do_binding_triple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(PLambdaParser.T__0)
            self.state = 141
            self.parameter()
            self.state = 142
            self.expression()
            self.state = 143
            self.expression()
            self.state = 144
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_exit_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.Do_exit_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_do_exit_clause

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterDo_exit_clause(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitDo_exit_clause(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitDo_exit_clause(self)
            else:
                return visitor.visitChildren(self)




    def do_exit_clause(self):

        localctx = PLambdaParser.Do_exit_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_do_exit_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(PLambdaParser.T__0)
            self.state = 147
            self.expression()
            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148
                self.expression()
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                    break

            self.state = 153
            self.match(PLambdaParser.T__1)
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
        self.enterRule(localctx, 10, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(PLambdaParser.T__0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PLambdaParser.ID:
                self.state = 156
                self.parameter()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
        self.enterRule(localctx, 12, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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
        self.enterRule(localctx, 14, self.RULE_binding_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(PLambdaParser.T__0)
            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.binding_pair()
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PLambdaParser.T__0):
                    break

            self.state = 172
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
        self.enterRule(localctx, 16, self.RULE_binding_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(PLambdaParser.T__0)
            self.state = 175
            self.parameter()
            self.state = 176
            self.expression()
            self.state = 177
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
        self.enterRule(localctx, 18, self.RULE_catch_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(PLambdaParser.T__0)
            self.state = 180
            self.match(PLambdaParser.CATCH)
            self.state = 181
            self.parameter()
            self.state = 183 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.expression()
                self.state = 185 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                    break

            self.state = 187
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
        self.enterRule(localctx, 20, self.RULE_range_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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
        self.enterRule(localctx, 22, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
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
        self.enterRule(localctx, 24, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
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
        self.enterRule(localctx, 26, self.RULE_token)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 28, self.RULE_type_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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




