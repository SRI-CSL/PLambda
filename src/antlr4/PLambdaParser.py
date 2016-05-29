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
        buf.write(u">\u00d8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2")
        buf.write(u"\32\n\2\r\2\16\2\33\3\3\3\3\3\3\6\3!\n\3\r\3\16\3\"\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\6\3+\n\3\r\3\16\3,\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\5\3\65\n\3\3\3\6\38\n\3\r\3\16\39\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\6\3B\n\3\r\3\16\3C\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\7\3M\n\3\f\3\16\3P\13\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\7\3X\n\3\f\3\16\3[\13\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3z\n\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0083\n\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\6\3\u008a\n\3\r\3\16\3\u008b\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\6\3\u0093\n\3\r\3\16\3\u0094\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\6\3\u009f\n\3\r\3\16\3\u00a0\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00ac\n\3\3\4\3\4\7\4")
        buf.write(u"\u00b0\n\4\f\4\16\4\u00b3\13\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write(u"\6\6\6\u00bb\n\6\r\6\16\6\u00bc\3\6\3\6\3\7\3\7\3\7\3")
        buf.write(u"\7\3\7\3\b\3\b\3\b\3\b\6\b\u00ca\n\b\r\b\16\b\u00cb\3")
        buf.write(u"\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\2\5\3\2\668\3\2\678\4\2\67")
        buf.write(u"\6799\u00ed\2\31\3\2\2\2\4\u00ab\3\2\2\2\6\u00ad\3\2")
        buf.write(u"\2\2\b\u00b6\3\2\2\2\n\u00b8\3\2\2\2\f\u00c0\3\2\2\2")
        buf.write(u"\16\u00c5\3\2\2\2\20\u00cf\3\2\2\2\22\u00d1\3\2\2\2\24")
        buf.write(u"\u00d3\3\2\2\2\26\u00d5\3\2\2\2\30\32\5\4\3\2\31\30\3")
        buf.write(u"\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\3")
        buf.write(u"\3\2\2\2\35\36\7\3\2\2\36 \7\r\2\2\37!\5\4\3\2 \37\3")
        buf.write(u"\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7")
        buf.write(u"\4\2\2%\u00ac\3\2\2\2&\'\7\3\2\2\'(\7\17\2\2(*\5\n\6")
        buf.write(u"\2)+\5\4\3\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2")
        buf.write(u"-.\3\2\2\2./\7\4\2\2/\u00ac\3\2\2\2\60\61\7\3\2\2\61")
        buf.write(u"\62\7\20\2\2\62\64\7\67\2\2\63\65\5\6\4\2\64\63\3\2\2")
        buf.write(u"\2\64\65\3\2\2\2\65\67\3\2\2\2\668\5\4\3\2\67\66\3\2")
        buf.write(u"\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7\4")
        buf.write(u"\2\2<\u00ac\3\2\2\2=>\7\3\2\2>?\7\21\2\2?A\5\6\4\2@B")
        buf.write(u"\5\4\3\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DE\3")
        buf.write(u"\2\2\2EF\7\4\2\2F\u00ac\3\2\2\2GH\7\3\2\2HI\7\23\2\2")
        buf.write(u"IJ\5\4\3\2JN\5\4\3\2KM\5\4\3\2LK\3\2\2\2MP\3\2\2\2NL")
        buf.write(u"\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\7\4\2\2R\u00ac")
        buf.write(u"\3\2\2\2ST\7\3\2\2TU\7\22\2\2UY\5\4\3\2VX\5\4\3\2WV\3")
        buf.write(u"\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2")
        buf.write(u"\2\2\\]\7\4\2\2]\u00ac\3\2\2\2^_\7\3\2\2_`\7\5\2\2`a")
        buf.write(u"\5\22\n\2ab\7\4\2\2b\u00ac\3\2\2\2cd\7\3\2\2de\7\6\2")
        buf.write(u"\2ef\5\4\3\2fg\7\4\2\2g\u00ac\3\2\2\2hi\7\3\2\2ij\7\7")
        buf.write(u"\2\2jk\5\4\3\2kl\5\4\3\2lm\7\4\2\2m\u00ac\3\2\2\2no\7")
        buf.write(u"\3\2\2op\7\b\2\2pq\5\4\3\2qr\5\4\3\2rs\5\4\3\2st\7\4")
        buf.write(u"\2\2t\u00ac\3\2\2\2uv\7\3\2\2vw\7\n\2\2wy\5\4\3\2xz\5")
        buf.write(u"\4\3\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\4\2\2|\u00ac")
        buf.write(u"\3\2\2\2}~\7\3\2\2~\177\7\13\2\2\177\u0080\5\4\3\2\u0080")
        buf.write(u"\u0082\5\4\3\2\u0081\u0083\5\4\3\2\u0082\u0081\3\2\2")
        buf.write(u"\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085")
        buf.write(u"\7\4\2\2\u0085\u00ac\3\2\2\2\u0086\u0087\7\3\2\2\u0087")
        buf.write(u"\u0089\7\t\2\2\u0088\u008a\5\4\3\2\u0089\u0088\3\2\2")
        buf.write(u"\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c")
        buf.write(u"\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7\4\2\2\u008e")
        buf.write(u"\u00ac\3\2\2\2\u008f\u0090\7\3\2\2\u0090\u0092\7\31\2")
        buf.write(u"\2\u0091\u0093\5\4\3\2\u0092\u0091\3\2\2\2\u0093\u0094")
        buf.write(u"\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write(u"\u0096\3\2\2\2\u0096\u0097\5\16\b\2\u0097\u0098\7\4\2")
        buf.write(u"\2\u0098\u00ac\3\2\2\2\u0099\u009a\7\3\2\2\u009a\u009b")
        buf.write(u"\7\26\2\2\u009b\u009c\7\67\2\2\u009c\u009e\5\20\t\2\u009d")
        buf.write(u"\u009f\5\4\3\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2")
        buf.write(u"\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write(u"\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3\u00ac\3\2\2\2\u00a4")
        buf.write(u"\u00a5\7\3\2\2\u00a5\u00a6\7#\2\2\u00a6\u00a7\5\24\13")
        buf.write(u"\2\u00a7\u00a8\7\4\2\2\u00a8\u00ac\3\2\2\2\u00a9\u00ac")
        buf.write(u"\79\2\2\u00aa\u00ac\7\67\2\2\u00ab\35\3\2\2\2\u00ab&")
        buf.write(u"\3\2\2\2\u00ab\60\3\2\2\2\u00ab=\3\2\2\2\u00abG\3\2\2")
        buf.write(u"\2\u00abS\3\2\2\2\u00ab^\3\2\2\2\u00abc\3\2\2\2\u00ab")
        buf.write(u"h\3\2\2\2\u00abn\3\2\2\2\u00abu\3\2\2\2\u00ab}\3\2\2")
        buf.write(u"\2\u00ab\u0086\3\2\2\2\u00ab\u008f\3\2\2\2\u00ab\u0099")
        buf.write(u"\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write(u"\u00aa\3\2\2\2\u00ac\5\3\2\2\2\u00ad\u00b1\7\3\2\2\u00ae")
        buf.write(u"\u00b0\5\b\5\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2")
        buf.write(u"\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4")
        buf.write(u"\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\4\2\2\u00b5")
        buf.write(u"\7\3\2\2\2\u00b6\u00b7\7\67\2\2\u00b7\t\3\2\2\2\u00b8")
        buf.write(u"\u00ba\7\3\2\2\u00b9\u00bb\5\f\7\2\u00ba\u00b9\3\2\2")
        buf.write(u"\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd")
        buf.write(u"\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\7\4\2\2\u00bf")
        buf.write(u"\13\3\2\2\2\u00c0\u00c1\7\3\2\2\u00c1\u00c2\5\b\5\2\u00c2")
        buf.write(u"\u00c3\5\4\3\2\u00c3\u00c4\7\4\2\2\u00c4\r\3\2\2\2\u00c5")
        buf.write(u"\u00c6\7\3\2\2\u00c6\u00c7\7\32\2\2\u00c7\u00c9\5\b\5")
        buf.write(u"\2\u00c8\u00ca\5\4\3\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write(u"\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write(u"\u00cd\3\2\2\2\u00cd\u00ce\7\4\2\2\u00ce\17\3\2\2\2\u00cf")
        buf.write(u"\u00d0\5\4\3\2\u00d0\21\3\2\2\2\u00d1\u00d2\t\2\2\2\u00d2")
        buf.write(u"\23\3\2\2\2\u00d3\u00d4\t\3\2\2\u00d4\25\3\2\2\2\u00d5")
        buf.write(u"\u00d6\t\4\2\2\u00d6\27\3\2\2\2\23\33\",\649CNYy\u0082")
        buf.write(u"\u008b\u0094\u00a0\u00ab\u00b1\u00bc\u00cb")
        return buf.getvalue()


class PLambdaParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'None'", u"<INVALID>", u"<INVALID>", 
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
                      u"AMBI1_OP", u"AMBI2_OP", u"NONE", u"SEQ", u"DO", 
                      u"LET", u"DEFINE", u"LAMBDA", u"APPLY", u"INVOKE", 
                      u"SINVOKE", u"OBJECT", u"FOR", u"ARRAY", u"MKARRAY", 
                      u"TRY", u"CATCH", u"BOOLEAN", u"FLOAT", u"INT", u"LOAD", 
                      u"IMPORT", u"ISNONE", u"ISOBJECT", u"GETUID", u"QUOTE", 
                      u"NOT", u"THROW", u"FETCH", u"NARROW", u"INSTANCEOF", 
                      u"AGET", u"LOOKUP", u"SETUID", u"ASET", u"UPDATE", 
                      u"SUPDATE", u"SETATTR", u"CONCAT", u"AND", u"OR", 
                      u"MINUS", u"IF", u"GETATTR", u"CHARACTER", u"ID", 
                      u"NUMBER", u"STRING", u"SYMBOL", u"LINE_COMMENT", 
                      u"NEW_LINE_COMMENT", u"NEW_COMMENT", u"WHITE_SPACE" ]

    RULE_unit = 0
    RULE_expression = 1
    RULE_parameterList = 2
    RULE_parameter = 3
    RULE_bindingList = 4
    RULE_bindingPair = 5
    RULE_catchExpression = 6
    RULE_rangeExpression = 7
    RULE_data = 8
    RULE_string = 9
    RULE_token = 10

    ruleNames =  [ u"unit", u"expression", u"parameterList", u"parameter", 
                   u"bindingList", u"bindingPair", u"catchExpression", u"rangeExpression", 
                   u"data", u"string", u"token" ]

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
    NONE=10
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
    FLOAT=26
    INT=27
    LOAD=28
    IMPORT=29
    ISNONE=30
    ISOBJECT=31
    GETUID=32
    QUOTE=33
    NOT=34
    THROW=35
    FETCH=36
    NARROW=37
    INSTANCEOF=38
    AGET=39
    LOOKUP=40
    SETUID=41
    ASET=42
    UPDATE=43
    SUPDATE=44
    SETATTR=45
    CONCAT=46
    AND=47
    OR=48
    MINUS=49
    IF=50
    GETATTR=51
    CHARACTER=52
    ID=53
    NUMBER=54
    STRING=55
    SYMBOL=56
    LINE_COMMENT=57
    NEW_LINE_COMMENT=58
    NEW_COMMENT=59
    WHITE_SPACE=60

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.expression()
                self.state = 25 
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



    class NaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.NaryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def N_ARY_OP(self):
            return self.getToken(PLambdaParser.N_ARY_OP, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterNaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitNaryExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitNaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class ForExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.ForExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(PLambdaParser.FOR, 0)
        def ID(self):
            return self.getToken(PLambdaParser.ID, 0)
        def rangeExpression(self):
            return self.getTypedRuleContext(PLambdaParser.RangeExpressionContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterForExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitForExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitForExpression(self)
            else:
                return visitor.visitChildren(self)


    class LambdaExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.LambdaExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(PLambdaParser.LAMBDA, 0)
        def parameterList(self):
            return self.getTypedRuleContext(PLambdaParser.ParameterListContext,0)

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


    class OneOrMoreExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.OneOrMoreExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def AMBI1_OP(self):
            return self.getToken(PLambdaParser.AMBI1_OP, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterOneOrMoreExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitOneOrMoreExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitOneOrMoreExpression(self)
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


    class TwoOrMoreExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.TwoOrMoreExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def AMBI2_OP(self):
            return self.getToken(PLambdaParser.AMBI2_OP, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterTwoOrMoreExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitTwoOrMoreExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitTwoOrMoreExpression(self)
            else:
                return visitor.visitChildren(self)


    class TryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.TryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(PLambdaParser.TRY, 0)
        def catchExpression(self):
            return self.getTypedRuleContext(PLambdaParser.CatchExpressionContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterTryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitTryExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitTryExpression(self)
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
        def parameterList(self):
            return self.getTypedRuleContext(PLambdaParser.ParameterListContext,0)

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
        def bindingList(self):
            return self.getTypedRuleContext(PLambdaParser.BindingListContext,0)

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
            self.state = 169
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = PLambdaParser.SeqExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(PLambdaParser.T__0)
                self.state = 28
                self.match(PLambdaParser.SEQ)
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 29
                    self.expression()
                    self.state = 32 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 34
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 2:
                localctx = PLambdaParser.LetExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(PLambdaParser.T__0)
                self.state = 37
                self.match(PLambdaParser.LET)
                self.state = 38
                self.bindingList()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 39
                    self.expression()
                    self.state = 42 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 44
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 3:
                localctx = PLambdaParser.DefineExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(PLambdaParser.T__0)
                self.state = 47
                self.match(PLambdaParser.DEFINE)
                self.state = 48
                self.match(PLambdaParser.ID)
                self.state = 50
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 49
                    self.parameterList()


                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 52
                    self.expression()
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 57
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 4:
                localctx = PLambdaParser.LambdaExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.match(PLambdaParser.T__0)
                self.state = 60
                self.match(PLambdaParser.LAMBDA)
                self.state = 61
                self.parameterList()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 62
                    self.expression()
                    self.state = 65 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 67
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 5:
                localctx = PLambdaParser.InvokeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(PLambdaParser.T__0)
                self.state = 70
                self.match(PLambdaParser.INVOKE)
                self.state = 71
                self.expression()
                self.state = 72
                self.expression()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 73
                    self.expression()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 6:
                localctx = PLambdaParser.ApplyExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.match(PLambdaParser.T__0)
                self.state = 82
                self.match(PLambdaParser.APPLY)
                self.state = 83
                self.expression()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 84
                    self.expression()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 7:
                localctx = PLambdaParser.DataExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.match(PLambdaParser.T__0)
                self.state = 93
                self.match(PLambdaParser.PRIMITIVE_DATA_OP)
                self.state = 94
                self.data()
                self.state = 95
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 8:
                localctx = PLambdaParser.UnaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 97
                self.match(PLambdaParser.T__0)
                self.state = 98
                self.match(PLambdaParser.UNARY_OP)
                self.state = 99
                self.expression()
                self.state = 100
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 9:
                localctx = PLambdaParser.BinaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 102
                self.match(PLambdaParser.T__0)
                self.state = 103
                self.match(PLambdaParser.BINARY_OP)
                self.state = 104
                self.expression()
                self.state = 105
                self.expression()
                self.state = 106
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 10:
                localctx = PLambdaParser.TernaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 108
                self.match(PLambdaParser.T__0)
                self.state = 109
                self.match(PLambdaParser.TERNARY_OP)
                self.state = 110
                self.expression()
                self.state = 111
                self.expression()
                self.state = 112
                self.expression()
                self.state = 113
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 11:
                localctx = PLambdaParser.OneOrMoreExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 115
                self.match(PLambdaParser.T__0)
                self.state = 116
                self.match(PLambdaParser.AMBI1_OP)
                self.state = 117
                self.expression()
                self.state = 119
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 118
                    self.expression()


                self.state = 121
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 12:
                localctx = PLambdaParser.TwoOrMoreExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 123
                self.match(PLambdaParser.T__0)
                self.state = 124
                self.match(PLambdaParser.AMBI2_OP)
                self.state = 125
                self.expression()
                self.state = 126
                self.expression()
                self.state = 128
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0):
                    self.state = 127
                    self.expression()


                self.state = 130
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 13:
                localctx = PLambdaParser.NaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 132
                self.match(PLambdaParser.T__0)
                self.state = 133
                self.match(PLambdaParser.N_ARY_OP)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 134
                    self.expression()
                    self.state = 137 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 139
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 14:
                localctx = PLambdaParser.TryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 141
                self.match(PLambdaParser.T__0)
                self.state = 142
                self.match(PLambdaParser.TRY)
                self.state = 144 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 143
                        self.expression()

                    else:
                        raise NoViableAltException(self)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 148
                self.catchExpression()
                self.state = 149
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 15:
                localctx = PLambdaParser.ForExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 151
                self.match(PLambdaParser.T__0)
                self.state = 152
                self.match(PLambdaParser.FOR)
                self.state = 153
                self.match(PLambdaParser.ID)
                self.state = 154
                self.rangeExpression()
                self.state = 156 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 155
                    self.expression()
                    self.state = 158 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                        break

                self.state = 160
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 16:
                localctx = PLambdaParser.QuoteExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 162
                self.match(PLambdaParser.T__0)
                self.state = 163
                self.match(PLambdaParser.QUOTE)
                self.state = 164
                self.string()
                self.state = 165
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 17:
                localctx = PLambdaParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 167
                self.match(PLambdaParser.STRING)
                pass

            elif la_ == 18:
                localctx = PLambdaParser.IdentifierLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 168
                self.match(PLambdaParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.ParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.ParameterContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_parameterList

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitParameterList(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = PLambdaParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PLambdaParser.T__0)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PLambdaParser.ID:
                self.state = 172
                self.parameter()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
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
            self.state = 180
            self.match(PLambdaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BindingListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.BindingListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def bindingPair(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PLambdaParser.BindingPairContext)
            else:
                return self.getTypedRuleContext(PLambdaParser.BindingPairContext,i)


        def getRuleIndex(self):
            return PLambdaParser.RULE_bindingList

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitBindingList(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitBindingList(self)
            else:
                return visitor.visitChildren(self)




    def bindingList(self):

        localctx = PLambdaParser.BindingListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bindingList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(PLambdaParser.T__0)
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 183
                self.bindingPair()
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PLambdaParser.T__0):
                    break

            self.state = 188
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BindingPairContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.BindingPairContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(PLambdaParser.ParameterContext,0)


        def expression(self):
            return self.getTypedRuleContext(PLambdaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLambdaParser.RULE_bindingPair

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterBindingPair(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitBindingPair(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitBindingPair(self)
            else:
                return visitor.visitChildren(self)




    def bindingPair(self):

        localctx = PLambdaParser.BindingPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bindingPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(PLambdaParser.T__0)
            self.state = 191
            self.parameter()
            self.state = 192
            self.expression()
            self.state = 193
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CatchExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.CatchExpressionContext, self).__init__(parent, invokingState)
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
            return PLambdaParser.RULE_catchExpression

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterCatchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitCatchExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitCatchExpression(self)
            else:
                return visitor.visitChildren(self)




    def catchExpression(self):

        localctx = PLambdaParser.CatchExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_catchExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(PLambdaParser.T__0)
            self.state = 196
            self.match(PLambdaParser.CATCH)
            self.state = 197
            self.parameter()
            self.state = 199 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 198
                self.expression()
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.ID) | (1 << PLambdaParser.STRING))) != 0)):
                    break

            self.state = 203
            self.match(PLambdaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PLambdaParser.RangeExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PLambdaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLambdaParser.RULE_rangeExpression

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterRangeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitRangeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitRangeExpression(self)
            else:
                return visitor.visitChildren(self)




    def rangeExpression(self):

        localctx = PLambdaParser.RangeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rangeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
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
            self.state = 207
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
            self.state = 209
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
            self.state = 211
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




