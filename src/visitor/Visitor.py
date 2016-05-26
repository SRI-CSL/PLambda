
from src.gen.PLambdaVisitor import PLambdaVisitor
from src.plambda.SymbolTable import SymbolTable
from src.visitor.ParseError import ParseError
from src.plambda.Code import SExpression, Atom, Syntax

class Visitor(PLambdaVisitor):

    
    def __init__(self, filename):
        self.filename = filename

    # Visit a parse tree produced by PLambdaParser#unit.
    def visitUnit(self, ctx):
        retval = []
        for exp in ctx.expression():
            retval.append(self.visit(exp))
        return retval

    # Visit a parse tree produced by PLambdaParser#stringLiteral.
    def visitStringLiteral(self, ctx):
        t = ctx.STRING().getSymbol()
        lineno = t.line
        return Atom(t.text, self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx):
        t = ctx.ID().getSymbol()
        lineno = t.line
        return  Atom(t.text, self.filename, lineno)

    def visitExpressionList(self, tsym, code, explist):
        t = tsym.getSymbol()
        lineno = t.line
        retval = [Atom(SymbolTable.canonicalize(t.text), self.filename, lineno)]
        for e in explist:
            retval.append(self.visit(e))
        return SExpression(code, tuple(retval), self.filename, lineno)

    def visitImplicitSeq(self, explist):
        retval = []
        for e in explist:
            retval.append(self.visit(e))
        #if there is an implicit seq, make it explicit    
        if len(retval) > 1:
            retval.insert(0, Atom(SymbolTable.SEQ, self.filename, -1))
            return SExpression(Syntax.SEQ, tuple(retval), self.filename, -1)
        else:
            return retval[0]
            
    # Visit a parse tree produced by PLambdaParser#invokeExpression.
    def visitInvokeExpression(self, ctx):
        return self.visitExpressionList(ctx.INVOKE(), ctx.expression())
    
    # Visit a parse tree produced by PLambdaParser#seqExpression.
    def visitSeqExpression(self, ctx):
        return self.visitExpressionList(Syntax.SEQ, SymbolTable.SEQ, ctx.expression())

    # Visit a parse tree produced by PLambdaParser#applyExpression.
    def visitApplyExpression(self, ctx):
        return self.visitExpressionList(Syntax.APPLY, ctx.APPLY(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        t = ctx.UNARY_OP().getSymbol()
        lineno = t.line
        rawop = t.text
        canonicalop = SymbolTable.canonicalize(rawop)
        if canonicalop is not None:
            op = Atom(canonicalop, self.filename, lineno)
            return SExpression(Syntax.UNARY_OP, (op, self.visit(ctx.expression())), self.filename, lineno)
        else:
            raise ParseError('Ooopsy: {0} not found in the SymbolTable'.format(rawop))

    # Visit a parse tree produced by PLambdaParser#binaryExpression.
    def visitBinaryExpression(self, ctx):
        return self.visitExpressionList(Syntax.BINARY_OP, ctx.BINARY_OP(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx):
        return self.visitExpressionList(Syntax.TERNARY_OP, ctx.TERNARY_OP(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx):
        lineno = ctx.LAMBDA().getSymbol().line
        params = self.visitParameterList(ctx.parameterList())
        body = self.visitImplicitSeq(ctx.expression())
        lamb = Atom(SymbolTable.LAMBDA, self.filename, lineno) 
        return SExpression(Syntax.LAMBDA, (lamb, params, body), self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#parameterList.
    def visitParameterList(self, ctx):
        retval = []
        lineno = -1
        for p in ctx.parameter():
            if lineno == -1:
                lineno = p.ID().getSymbol().line
            retval.append(self.visitParameter(p))
        return SExpression(None, tuple(retval), self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx):
        t = ctx.ID().getSymbol()
        lineno = t.line
        return Atom(t.text, self.filename, lineno)
            
    # Visit a parse tree produced by PLambdaParser#letExpression.
    def visitLetExpression(self, ctx):
        lineno = ctx.LET().getSymbol().line
        bindings = self.visitBindingList(ctx.bindingList())
        body = self.visitImplicitSeq(ctx.expression())
        return SExpression(Syntax.LET, (SymbolTable.LET, bindings, body), self.filename, lineno)
    
    # Visit a parse tree produced by PLambdaParser#bindingList.
    def visitBindingList(self, ctx):
        retval = []
        for b in ctx.bindingPair():
            retval.append(self.visitBindingPair(b))
        return SExpression(None, tuple(retval), self.filename, -1)

    # Visit a parse tree produced by PLambdaParser#binding_pair.
    def visitBindingPair(self, ctx):
        lineno = ctx.parameter().ID().getSymbol().line
        return SExpression(None,
                           (self.visitParameter(ctx.parameter()), self.visit(ctx.expression())),
                           self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx):
        lineno = ctx.DEFINE().getSymbol().line
        define = Atom(SymbolTable.DEFINE, self.filename, lineno)
        paramList = ctx.parameterList()
        params = None
        if paramList is not None:
            params = self.visitParameterList(paramList)
        body = self.visitImplicitSeq(ctx.expression())
        id = ctx.ID().getSymbol().text
        if params is not None:
            return SExpression(Syntax.DEFINE, (define, id, params, body), self.filename, lineno)
        else:
            return SExpression(Syntax.DEFINE, (define, id, body), self.filename, lineno)


    # Visit a parse tree produced by PLambdaParser#forExpression.
    def visitForExpression(self, ctx):
        lineno = ctx.FOR().getSymbol().line
        f = Atom(SymbolTable.FOR, self.filename, lineno)
        t = ctx.ID().getSymbol()
        lineno = t.line
        id = Atom(t.text, self.filename, lineno)
        return SExpression(Syntax.FOR, (f, id,
                                        self.visit(ctx.rangeExpression()),
                                        self.visitImplicitSeq(ctx.expression())),
                           self.filename, lineno)


    # Visit a parse tree produced by PLambdaParser#tryExpression.
    def visitTryExpression(self, ctx):
        lineno = ctx.TRY().getSymbol().line
        tr = Atom(SymbolTable.TRY, self.filename, lineno)
        return SExpression(Syntax.TRY, (tr,
                                        self.visitImplicitSeq(ctx.expression()),
                                        self.visitCatchExpression(ctx.catchExpression())),
                           self.filename, lineno)
    
    # Visit a parse tree produced by PLambdaParser#catchExpression.
    def visitCatchExpression(self, ctx):
        lineno = ctx.CATCH().getSymbol().line
        ctch = Atom(SymbolTable.CATCH, self.filename, lineno)
        return SExpression(Syntax.CATCH, (ctch,
                     self.visitParameter(ctx.parameter()),
                     self.visitImplicitSeq(ctx.expression())),
                    self.filename, lineno)
                    

    # Visit a parse tree produced by PLambdaParser#dataExpression.
    def visitDataExpression(self, ctx):
        t = ctx.PRIMITIVE_DATA_OP().getSymbol()
        lineno = t.line
        op = Atom(SymbolTable.canonicalize(t.text), self.filename, lineno)
        return SExpression(Syntax.PRIMITIVE_DATA_OP, (op, self.visitData(ctx.data())), self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#data.
    def visitData(self, ctx):
        data = None
        if ctx.ID() != None:
            data = ctx.ID()
        elif ctx.NUMBER() != None:
            data = ctx.NUMBER()
        else:
            data = ctx.CHARACTER()
        return Atom(data.getSymbol().text, self.filename, data.getSymbol().line)

    # Visit a parse tree produced by PLambdaParser#string.
    def visitString(self, ctx):
        data = None
        if ctx.ID() != None:
            data = ctx.ID()
        else:
            data = ctx.NUMBER()
        return Atom(data.getSymbol().text, self.filename, data.getSymbol().line)


    
    # Visit a parse tree produced by PLambdaParser#quoteExpression.
    def visitQuoteExpression(self, ctx):
        lineno = ctx.QUOTE().getSymbol().line
        return SExpression(Syntax.Quote, (SymbolTable.QUOTE,
                                          self.visitString(ctx.string())),
                           self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def visitOneOrMoreExpression(self, ctx):
        return self.visitExpressionList(Syntax.AMBI1_OP, ctx.AMBI1_OP(), ctx.expression());

    # Visit a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def visitTwoOrMoreExpression(self, ctx):
        return self.visitExpressionList(Syntax.AMBI2_OP, ctx.AMBI2_OP(), ctx.expression());

    # Visit a parse tree produced by PLambdaParser#naryExpression.
    def visitNaryExpression(self, ctx):
        return self.visitExpressionList(Syntax.N_ARY_OP, ctx.N_ARY_OP(), ctx.expression()); 
