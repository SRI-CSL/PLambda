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
        buf.write(u"D\u00d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r")
        buf.write(u"\2\16\2\31\3\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\6\3)\n\3\r\3\16\3*\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\5\3\63\n\3\3\3\6\3\66\n\3\r\3\16\3\67\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\6\3@\n\3\r\3\16\3A\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\7\3K\n\3\f\3\16\3N\13\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\7\3V\n\3\f\3\16\3Y\13\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3x\n\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0081\n\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\7\3\u0088\n\3\f\3\16\3\u008b\13\3\3\3\3\3\3\3")
        buf.write(u"\3\3\6\3\u0091\n\3\r\3\16\3\u0092\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\6\3\u009d\n\3\r\3\16\3\u009e\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00ab\n\3\3\4\3\4\7")
        buf.write(u"\4\u00af\n\4\f\4\16\4\u00b2\13\4\3\4\3\4\3\5\3\5\3\6")
        buf.write(u"\3\6\6\6\u00ba\n\6\r\6\16\6\u00bb\3\6\3\6\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\b\3\b\3\b\3\b\6\b\u00c9\n\b\r\b\16\b\u00ca")
        buf.write(u"\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b")
        buf.write(u"\n\f\16\20\22\24\2\4\3\2<=\4\2\5\5<<\u00ec\2\27\3\2\2")
        buf.write(u"\2\4\u00aa\3\2\2\2\6\u00ac\3\2\2\2\b\u00b5\3\2\2\2\n")
        buf.write(u"\u00b7\3\2\2\2\f\u00bf\3\2\2\2\16\u00c4\3\2\2\2\20\u00ce")
        buf.write(u"\3\2\2\2\22\u00d0\3\2\2\2\24\u00d2\3\2\2\2\26\30\5\4")
        buf.write(u"\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32")
        buf.write(u"\3\2\2\2\32\3\3\2\2\2\33\34\7\3\2\2\34\36\7\16\2\2\35")
        buf.write(u"\37\5\4\3\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3")
        buf.write(u"\2\2\2!\"\3\2\2\2\"#\7\4\2\2#\u00ab\3\2\2\2$%\7\3\2\2")
        buf.write(u"%&\7\20\2\2&(\5\n\6\2\')\5\4\3\2(\'\3\2\2\2)*\3\2\2\2")
        buf.write(u"*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7\4\2\2-\u00ab\3\2\2")
        buf.write(u"\2./\7\3\2\2/\60\7\21\2\2\60\62\7<\2\2\61\63\5\6\4\2")
        buf.write(u"\62\61\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\66\5\4")
        buf.write(u"\3\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3")
        buf.write(u"\2\2\289\3\2\2\29:\7\4\2\2:\u00ab\3\2\2\2;<\7\3\2\2<")
        buf.write(u"=\7\22\2\2=?\5\6\4\2>@\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?")
        buf.write(u"\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\4\2\2D\u00ab\3\2\2\2")
        buf.write(u"EF\7\3\2\2FG\7\24\2\2GH\5\4\3\2HL\5\4\3\2IK\5\4\3\2J")
        buf.write(u"I\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3")
        buf.write(u"\2\2\2OP\7\4\2\2P\u00ab\3\2\2\2QR\7\3\2\2RS\7\23\2\2")
        buf.write(u"SW\5\4\3\2TV\5\4\3\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX")
        buf.write(u"\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\4\2\2[\u00ab\3\2\2\2")
        buf.write(u"\\]\7\3\2\2]^\7\6\2\2^_\5\22\n\2_`\7\4\2\2`\u00ab\3\2")
        buf.write(u"\2\2ab\7\3\2\2bc\7\7\2\2cd\5\4\3\2de\7\4\2\2e\u00ab\3")
        buf.write(u"\2\2\2fg\7\3\2\2gh\7\b\2\2hi\5\4\3\2ij\5\4\3\2jk\7\4")
        buf.write(u"\2\2k\u00ab\3\2\2\2lm\7\3\2\2mn\7\t\2\2no\5\4\3\2op\5")
        buf.write(u"\4\3\2pq\5\4\3\2qr\7\4\2\2r\u00ab\3\2\2\2st\7\3\2\2t")
        buf.write(u"u\7\13\2\2uw\5\4\3\2vx\5\4\3\2wv\3\2\2\2wx\3\2\2\2xy")
        buf.write(u"\3\2\2\2yz\7\4\2\2z\u00ab\3\2\2\2{|\7\3\2\2|}\7\f\2\2")
        buf.write(u"}~\5\4\3\2~\u0080\5\4\3\2\177\u0081\5\4\3\2\u0080\177")
        buf.write(u"\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write(u"\u0083\7\4\2\2\u0083\u00ab\3\2\2\2\u0084\u0085\7\3\2")
        buf.write(u"\2\u0085\u0089\7\n\2\2\u0086\u0088\5\4\3\2\u0087\u0086")
        buf.write(u"\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write(u"\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2")
        buf.write(u"\2\u008c\u00ab\7\4\2\2\u008d\u008e\7\3\2\2\u008e\u0090")
        buf.write(u"\7\27\2\2\u008f\u0091\5\4\3\2\u0090\u008f\3\2\2\2\u0091")
        buf.write(u"\u0092\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2")
        buf.write(u"\2\u0093\u0094\3\2\2\2\u0094\u0095\5\16\b\2\u0095\u0096")
        buf.write(u"\7\4\2\2\u0096\u00ab\3\2\2\2\u0097\u0098\7\3\2\2\u0098")
        buf.write(u"\u0099\7\26\2\2\u0099\u009a\7<\2\2\u009a\u009c\5\20\t")
        buf.write(u"\2\u009b\u009d\5\4\3\2\u009c\u009b\3\2\2\2\u009d\u009e")
        buf.write(u"\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write(u"\u00a0\3\2\2\2\u00a0\u00a1\7\4\2\2\u00a1\u00ab\3\2\2")
        buf.write(u"\2\u00a2\u00a3\7\3\2\2\u00a3\u00a4\7$\2\2\u00a4\u00a5")
        buf.write(u"\5\22\n\2\u00a5\u00a6\7\4\2\2\u00a6\u00ab\3\2\2\2\u00a7")
        buf.write(u"\u00ab\7\5\2\2\u00a8\u00ab\7<\2\2\u00a9\u00ab\7\r\2\2")
        buf.write(u"\u00aa\33\3\2\2\2\u00aa$\3\2\2\2\u00aa.\3\2\2\2\u00aa")
        buf.write(u";\3\2\2\2\u00aaE\3\2\2\2\u00aaQ\3\2\2\2\u00aa\\\3\2\2")
        buf.write(u"\2\u00aaa\3\2\2\2\u00aaf\3\2\2\2\u00aal\3\2\2\2\u00aa")
        buf.write(u"s\3\2\2\2\u00aa{\3\2\2\2\u00aa\u0084\3\2\2\2\u00aa\u008d")
        buf.write(u"\3\2\2\2\u00aa\u0097\3\2\2\2\u00aa\u00a2\3\2\2\2\u00aa")
        buf.write(u"\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2")
        buf.write(u"\2\u00ab\5\3\2\2\2\u00ac\u00b0\7\3\2\2\u00ad\u00af\5")
        buf.write(u"\b\5\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write(u"\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2")
        buf.write(u"\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7\4\2\2\u00b4\7\3")
        buf.write(u"\2\2\2\u00b5\u00b6\7<\2\2\u00b6\t\3\2\2\2\u00b7\u00b9")
        buf.write(u"\7\3\2\2\u00b8\u00ba\5\f\7\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write(u"\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2")
        buf.write(u"\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\7\4\2\2\u00be\13\3")
        buf.write(u"\2\2\2\u00bf\u00c0\7\3\2\2\u00c0\u00c1\5\b\5\2\u00c1")
        buf.write(u"\u00c2\5\4\3\2\u00c2\u00c3\7\4\2\2\u00c3\r\3\2\2\2\u00c4")
        buf.write(u"\u00c5\7\3\2\2\u00c5\u00c6\7\30\2\2\u00c6\u00c8\5\b\5")
        buf.write(u"\2\u00c7\u00c9\5\4\3\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca")
        buf.write(u"\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write(u"\u00cc\3\2\2\2\u00cc\u00cd\7\4\2\2\u00cd\17\3\2\2\2\u00ce")
        buf.write(u"\u00cf\5\4\3\2\u00cf\21\3\2\2\2\u00d0\u00d1\t\2\2\2\u00d1")
        buf.write(u"\23\3\2\2\2\u00d2\u00d3\t\3\2\2\u00d3\25\3\2\2\2\23\31")
        buf.write(u" *\62\67ALWw\u0080\u0089\u0092\u009e\u00aa\u00b0\u00bb")
        buf.write(u"\u00ca")
        return buf.getvalue()


class PLambdaParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'None'", u"<INVALID>", 
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
                     u"<INVALID>", u"<INVALID>", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"STRING", 
                      u"PRIMITIVE_DATA_OP", u"UNARY_OP", u"BINARY_OP", u"TERNARY_OP", 
                      u"N_ARY_OP", u"AMBI1_OP", u"AMBI2_OP", u"NONE", u"SEQ", 
                      u"DO", u"LET", u"DEFINE", u"LAMBDA", u"APPLY", u"INVOKE", 
                      u"SINVOKE", u"FOR", u"TRY", u"CATCH", u"BOOLEAN", 
                      u"FLOAT", u"INT", u"LOAD", u"IMPORT", u"ISNONE", u"ISOBJECT", 
                      u"ISINT", u"ISFLOAT", u"GETUID", u"GLOBAL", u"QUOTE", 
                      u"NOT", u"THROW", u"FETCH", u"NARROW", u"INSTANCEOF", 
                      u"GET", u"IS", u"LOOKUP", u"SETUID", u"KWAPPLY", u"MODIFY", 
                      u"UPDATE", u"SUPDATE", u"SETATTR", u"CONCAT", u"AND", 
                      u"OR", u"MKTUPLE", u"MKLIST", u"MKDICT", u"MINUS", 
                      u"IF", u"GETATTR", u"ID", u"NUMBER", u"STRING_SQ", 
                      u"STRING_DQ", u"SYMBOL", u"LINE_COMMENT", u"NEW_LINE_COMMENT", 
                      u"NEW_COMMENT", u"WHITE_SPACE" ]

    RULE_unit = 0
    RULE_expression = 1
    RULE_parameterList = 2
    RULE_parameter = 3
    RULE_bindingList = 4
    RULE_bindingPair = 5
    RULE_catchExpression = 6
    RULE_rangeExpression = 7
    RULE_data = 8
    RULE_token = 9

    ruleNames =  [ u"unit", u"expression", u"parameterList", u"parameter", 
                   u"bindingList", u"bindingPair", u"catchExpression", u"rangeExpression", 
                   u"data", u"token" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    STRING=3
    PRIMITIVE_DATA_OP=4
    UNARY_OP=5
    BINARY_OP=6
    TERNARY_OP=7
    N_ARY_OP=8
    AMBI1_OP=9
    AMBI2_OP=10
    NONE=11
    SEQ=12
    DO=13
    LET=14
    DEFINE=15
    LAMBDA=16
    APPLY=17
    INVOKE=18
    SINVOKE=19
    FOR=20
    TRY=21
    CATCH=22
    BOOLEAN=23
    FLOAT=24
    INT=25
    LOAD=26
    IMPORT=27
    ISNONE=28
    ISOBJECT=29
    ISINT=30
    ISFLOAT=31
    GETUID=32
    GLOBAL=33
    QUOTE=34
    NOT=35
    THROW=36
    FETCH=37
    NARROW=38
    INSTANCEOF=39
    GET=40
    IS=41
    LOOKUP=42
    SETUID=43
    KWAPPLY=44
    MODIFY=45
    UPDATE=46
    SUPDATE=47
    SETATTR=48
    CONCAT=49
    AND=50
    OR=51
    MKTUPLE=52
    MKLIST=53
    MKDICT=54
    MINUS=55
    IF=56
    GETATTR=57
    ID=58
    NUMBER=59
    STRING_SQ=60
    STRING_DQ=61
    SYMBOL=62
    LINE_COMMENT=63
    NEW_LINE_COMMENT=64
    NEW_COMMENT=65
    WHITE_SPACE=66

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.expression()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
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


    class NoneLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PLambdaParser.ExpressionContext)
            super(PLambdaParser.NoneLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NONE(self):
            return self.getToken(PLambdaParser.NONE, 0)

        def enterRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.enterNoneLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PLambdaListener ):
                listener.exitNoneLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, PLambdaVisitor ):
                return visitor.visitNoneLiteral(self)
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
        def data(self):
            return self.getTypedRuleContext(PLambdaParser.DataContext,0)


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
            self.state = 168
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = PLambdaParser.SeqExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(PLambdaParser.T__0)
                self.state = 26
                self.match(PLambdaParser.SEQ)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 27
                    self.expression()
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
                        break

                self.state = 32
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 2:
                localctx = PLambdaParser.LetExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(PLambdaParser.T__0)
                self.state = 35
                self.match(PLambdaParser.LET)
                self.state = 36
                self.bindingList()
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 37
                    self.expression()
                    self.state = 40 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
                        break

                self.state = 42
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 3:
                localctx = PLambdaParser.DefineExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(PLambdaParser.T__0)
                self.state = 45
                self.match(PLambdaParser.DEFINE)
                self.state = 46
                self.match(PLambdaParser.ID)
                self.state = 48
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 47
                    self.parameterList()


                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    self.expression()
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
                        break

                self.state = 55
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 4:
                localctx = PLambdaParser.LambdaExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(PLambdaParser.T__0)
                self.state = 58
                self.match(PLambdaParser.LAMBDA)
                self.state = 59
                self.parameterList()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 60
                    self.expression()
                    self.state = 63 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
                        break

                self.state = 65
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 5:
                localctx = PLambdaParser.InvokeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.match(PLambdaParser.T__0)
                self.state = 68
                self.match(PLambdaParser.INVOKE)
                self.state = 69
                self.expression()
                self.state = 70
                self.expression()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0):
                    self.state = 71
                    self.expression()
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 77
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 6:
                localctx = PLambdaParser.ApplyExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.match(PLambdaParser.T__0)
                self.state = 80
                self.match(PLambdaParser.APPLY)
                self.state = 81
                self.expression()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0):
                    self.state = 82
                    self.expression()
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 7:
                localctx = PLambdaParser.DataExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.match(PLambdaParser.T__0)
                self.state = 91
                self.match(PLambdaParser.PRIMITIVE_DATA_OP)
                self.state = 92
                self.data()
                self.state = 93
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 8:
                localctx = PLambdaParser.UnaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 95
                self.match(PLambdaParser.T__0)
                self.state = 96
                self.match(PLambdaParser.UNARY_OP)
                self.state = 97
                self.expression()
                self.state = 98
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 9:
                localctx = PLambdaParser.BinaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.match(PLambdaParser.T__0)
                self.state = 101
                self.match(PLambdaParser.BINARY_OP)
                self.state = 102
                self.expression()
                self.state = 103
                self.expression()
                self.state = 104
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 10:
                localctx = PLambdaParser.TernaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 106
                self.match(PLambdaParser.T__0)
                self.state = 107
                self.match(PLambdaParser.TERNARY_OP)
                self.state = 108
                self.expression()
                self.state = 109
                self.expression()
                self.state = 110
                self.expression()
                self.state = 111
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 11:
                localctx = PLambdaParser.OneOrMoreExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 113
                self.match(PLambdaParser.T__0)
                self.state = 114
                self.match(PLambdaParser.AMBI1_OP)
                self.state = 115
                self.expression()
                self.state = 117
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0):
                    self.state = 116
                    self.expression()


                self.state = 119
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 12:
                localctx = PLambdaParser.TwoOrMoreExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 121
                self.match(PLambdaParser.T__0)
                self.state = 122
                self.match(PLambdaParser.AMBI2_OP)
                self.state = 123
                self.expression()
                self.state = 124
                self.expression()
                self.state = 126
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0):
                    self.state = 125
                    self.expression()


                self.state = 128
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 13:
                localctx = PLambdaParser.NaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 130
                self.match(PLambdaParser.T__0)
                self.state = 131
                self.match(PLambdaParser.N_ARY_OP)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0):
                    self.state = 132
                    self.expression()
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 138
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 14:
                localctx = PLambdaParser.TryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 139
                self.match(PLambdaParser.T__0)
                self.state = 140
                self.match(PLambdaParser.TRY)
                self.state = 142 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 141
                        self.expression()

                    else:
                        raise NoViableAltException(self)
                    self.state = 144 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 146
                self.catchExpression()
                self.state = 147
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 15:
                localctx = PLambdaParser.ForExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 149
                self.match(PLambdaParser.T__0)
                self.state = 150
                self.match(PLambdaParser.FOR)
                self.state = 151
                self.match(PLambdaParser.ID)
                self.state = 152
                self.rangeExpression()
                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 153
                    self.expression()
                    self.state = 156 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
                        break

                self.state = 158
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 16:
                localctx = PLambdaParser.QuoteExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 160
                self.match(PLambdaParser.T__0)
                self.state = 161
                self.match(PLambdaParser.QUOTE)
                self.state = 162
                self.data()
                self.state = 163
                self.match(PLambdaParser.T__1)
                pass

            elif la_ == 17:
                localctx = PLambdaParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 165
                self.match(PLambdaParser.STRING)
                pass

            elif la_ == 18:
                localctx = PLambdaParser.IdentifierLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 166
                self.match(PLambdaParser.ID)
                pass

            elif la_ == 19:
                localctx = PLambdaParser.NoneLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 167
                self.match(PLambdaParser.NONE)
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
            self.state = 170
            self.match(PLambdaParser.T__0)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PLambdaParser.ID:
                self.state = 171
                self.parameter()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
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
            self.state = 179
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
            self.state = 181
            self.match(PLambdaParser.T__0)
            self.state = 183 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.bindingPair()
                self.state = 185 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PLambdaParser.T__0):
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
            self.state = 189
            self.match(PLambdaParser.T__0)
            self.state = 190
            self.parameter()
            self.state = 191
            self.expression()
            self.state = 192
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
            self.state = 194
            self.match(PLambdaParser.T__0)
            self.state = 195
            self.match(PLambdaParser.CATCH)
            self.state = 196
            self.parameter()
            self.state = 198 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 197
                self.expression()
                self.state = 200 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PLambdaParser.T__0) | (1 << PLambdaParser.STRING) | (1 << PLambdaParser.NONE) | (1 << PLambdaParser.ID))) != 0)):
                    break

            self.state = 202
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
            self.state = 204
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
            self.state = 206
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
        self.enterRule(localctx, 18, self.RULE_token)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not(_la==PLambdaParser.STRING or _la==PLambdaParser.ID):
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




