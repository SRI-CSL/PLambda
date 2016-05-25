
from PLambdaVisitor import PLambdaVisitor
from SymbolTable import SymbolTable
from ParseError import ParseError
from Code import Code

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
        return ctx.STRING().getSymbol().text

    # Visit a parse tree produced by PLambdaParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx):
        return ctx.ID().getSymbol().text

    def visitExpressionList(self, tsym, explist):
        t = tsym.getSymbol()
        lineno = t.line
        retval = [SymbolTable.canonicalize(t.text)]
        for e in explist:
            retval.append(self.visit(e))
        return Code(tuple(retval), self.filename, lineno)

    def visitImplicitSeq(self, explist):
        retval = []
        for e in explist:
            retval.append(self.visit(e))
        #if there is an implicit seq, make it explicit    
        if len(retval) > 1:
            retval.insert(0, SymbolTable.SEQ)
            return Code(tuple(retval), self.filename, -1)
        else:
            return retval[0]
            
    # Visit a parse tree produced by PLambdaParser#invokeExpression.
    def visitInvokeExpression(self, ctx):
        return self.visitExpressionList(ctx.INVOKE(), ctx.expression())
    
    # Visit a parse tree produced by PLambdaParser#seqExpression.
    def visitSeqExpression(self, ctx):
        return self.visitExpressionList(SymbolTable.SEQ, ctx.expression())

    # Visit a parse tree produced by PLambdaParser#applyExpression.
    def visitApplyExpression(self, ctx):
        return self.visitExpressionList(ctx.APPLY(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        t = ctx.UNARY_OP().getSymbol()
        lineno = t.line
        rawop = t.text
        op = SymbolTable.canonicalize(rawop)
        return Code((op, self.visit(ctx.expression())), self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#binaryExpression.
    def visitBinaryExpression(self, ctx):
        return self.visitExpressionList(ctx.BINARY_OP(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx):
        return self.visitExpressionList(ctx.TERNARY_OP(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx):
        lineno = ctx.LAMBDA().getSymbol().line
        params = self.visitParameterList(ctx.parameterList())
        body = self.visitImplicitSeq(ctx.expression())
        return Code((SymbolTable.LAMBDA, params, body), self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#parameterList.
    def visitParameterList(self, ctx):
        retval = []
        lineno = -1
        for p in ctx.parameter():
            if lineno == -1:
                lineno = p.ID().getSymbol().line
            retval.append(self.visitParameter(p))
        return Code(tuple(retval), self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx):
        return ctx.ID().getSymbol().text
            
    # Visit a parse tree produced by PLambdaParser#letExpression.
    def visitLetExpression(self, ctx):
        lineno = ctx.LET().getSymbol().line
        bindings = self.visitBindingList(ctx.bindingList())
        body = self.visitImplicitSeq(ctx.expression())
        return Code((SymbolTable.LET, bindings, body),
                    self.filename,
                    lineno)
    
    # Visit a parse tree produced by PLambdaParser#bindingList.
    def visitBindingList(self, ctx):
        retval = []
        for b in ctx.bindingPair():
            retval.append(self.visitBindingPair(b))
        return Code(tuple(retval), self.filename, -1)

    # Visit a parse tree produced by PLambdaParser#binding_pair.
    def visitBindingPair(self, ctx):
        lineno = ctx.parameter().ID().getSymbol().line
        return Code((self.visitParameter(ctx.parameter()),
                     self.visit(ctx.expression())),
                    self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx):
        lineno = ctx.DEFINE().getSymbol().line
        paramList = ctx.parameterList()
        params = None
        if paramList is not None:
            params = self.visitParameterList(paramList)
        body = self.visitImplicitSeq(ctx.expression())
        id = ctx.ID().getSymbol().text
        if params is not None:
            return Code((SymbolTable.DEFINE, id, params, body),
                        self.filename, lineno)
        else:
            return Code((SymbolTable.DEFINE, ctx.ID().getSymbol().text, body),
                        self.filename, lineno)


    # Visit a parse tree produced by PLambdaParser#forExpression.
    def visitForExpression(self, ctx):
        lineno = ctx.FOR().getSymbol().line
        return Code((SymbolTable.FOR,
                     ctx.ID().getSymbol().text,
                     self.visit(ctx.rangeExpression()),
                     self.visitImplicitSeq(ctx.expression())),
                    self.filename, lineno)


    # Visit a parse tree produced by PLambdaParser#tryExpression.
    def visitTryExpression(self, ctx):
        lineno = ctx.TRY().getSymbol().line
        return Code((SymbolTable.TRY,
                     self.visitImplicitSeq(ctx.expression()),
                     self.visitCatchExpression(ctx.catchExpression())),
                    self.filename, lineno)
    
    # Visit a parse tree produced by PLambdaParser#catchExpression.
    def visitCatchExpression(self, ctx):
        lineno = ctx.CATCH().getSymbol().line
        return Code((SymbolTable.CATCH,
                     self.visitParameter(ctx.parameter()),
                     self.visitImplicitSeq(ctx.expression())),
                    self.filename, lineno)
                    

    # Visit a parse tree produced by PLambdaParser#dataExpression.
    def visitDataExpression(self, ctx):
        t = ctx.PRIMITIVE_DATA_OP().getSymbol()
        lineno = t.line
        op = SymbolTable.canonicalize(t.text)
        return Code((op, self.visitData(ctx.data())),
                    self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#data.
    def visitData(self, ctx):
        data = None
        if ctx.ID() != None:
            data = ctx.ID()
        elif ctx.NUMBER() != None:
            data = ctx.NUMBER()
        else:
            data = ctx.CHARACTER()
        return data.getSymbol().text

    # Visit a parse tree produced by PLambdaParser#string.
    def visitString(self, ctx):
        data = None
        if ctx.ID() != None:
            data = ctx.ID()
        else:
            data = ctx.NUMBER()
        return data.getSymbol().text


    
    # Visit a parse tree produced by PLambdaParser#quoteExpression.
    def visitQuoteExpression(self, ctx):
        lineno = ctx.QUOTE().getSymbol().line
        return Code((SymbolTable.QUOTE,
                     self.visitString(ctx.string())),
                    self.filename, lineno)

    # Visit a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def visitOneOrMoreExpression(self, ctx):
        return self.visitExpressionList(ctx.AMBI1_OP(), ctx.expression());

    # Visit a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def visitTwoOrMoreExpression(self, ctx):
        return self.visitExpressionList(ctx.AMBI2_OP(), ctx.expression());

    # Visit a parse tree produced by PLambdaParser#naryExpression.
    def visitNaryExpression(self, ctx):
        return self.visitExpressionList(ctx.N_ARY_OP(), ctx.expression()); 
