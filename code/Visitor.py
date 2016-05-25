
from PLambdaVisitor import PLambdaVisitor
from SymbolTable import SymbolTable
from ParseError import ParseError

class Visitor(PLambdaVisitor):

    
    def __init__(self, filename):
        self.filename = filename

    def location(self, tnode):
        return ' @ line  {0} of {1}'.format(tnode.getSymbol().getLine(), self.filename)
    
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
        retval = [SymbolTable.canonicalize(tsym.getSymbol().text)]
        for e in explist:
            retval.append(self.visit(e))
        return tuple(retval)

    def visitImplicitSeq(self, explist):
        retval = []
        for e in explist:
            retval.append(self.visit(e))
        #if there is an implicit seq, make it explicit    
        if len(retval) > 1:
            retval.insert(0, SymbolTable.SEQ)
            return tuple(retval)
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
        rawop = ctx.UNARY_OP().getSymbol().text
        op = SymbolTable.canonicalize(rawop)
        return (op, self.visit(ctx.expression()))

    # Visit a parse tree produced by PLambdaParser#binaryExpression.
    def visitBinaryExpression(self, ctx):
        return self.visitExpressionList(ctx.BINARY_OP(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx):
        return self.visitExpressionList(ctx.TERNARY_OP(), ctx.expression())

    # Visit a parse tree produced by PLambdaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx):
        params = self.visitParameterList(ctx.parameterList())
        body = self.visitImplicitSeq(ctx.expression())
        return (SymbolTable.LAMBDA, params, body)

    # Visit a parse tree produced by PLambdaParser#parameterList.
    def visitParameterList(self, ctx):
        retval = []
        for p in ctx.parameter():
            retval.append(self.visitParameter(p))
        return tuple(retval)

    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx):
        return ctx.ID().getSymbol().text
            
    # Visit a parse tree produced by PLambdaParser#letExpression.
    def visitLetExpression(self, ctx):
        bindings = self.visitBindingList(ctx.bindingList())
        body = self.visitImplicitSeq(ctx.expression())
        return (SymbolTable.LET, bindings, body)
    
    # Visit a parse tree produced by PLambdaParser#bindingList.
    def visitBindingList(self, ctx):
        retval = []
        for b in ctx.bindingPair():
            retval.append(self.visitBindingPair(b))
        return tuple(retval)

    # Visit a parse tree produced by PLambdaParser#binding_pair.
    def visitBindingPair(self, ctx):
        return (self.visitParameter(ctx.parameter()), self.visit(ctx.expression()))

    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx):
        paramList = ctx.parameterList()
        params = None
        if paramList is not None:
            params = self.visitParameterList(paramList)
        body = self.visitImplicitSeq(ctx.expression())
        if params is not None:
            return (SymbolTable.DEFINE, ctx.ID().getSymbol().text, params, body)
        else:
            return (SymbolTable.DEFINE, ctx.ID().getSymbol().text, body)


    # Visit a parse tree produced by PLambdaParser#forExpression.
    def visitForExpression(self, ctx):
        return (SymbolTable.FOR,
                ctx.ID().getSymbol().text,
                self.visit(ctx.rangeExpression()),
                self.visitImplicitSeq(ctx.expression()))


    # Visit a parse tree produced by PLambdaParser#tryExpression.
    def visitTryExpression(self, ctx):
        return (SymbolTable.TRY,
                self.visitImplicitSeq(ctx.expression()),
                self.visitCatchExpression(ctx.catchExpression()))

    # Visit a parse tree produced by PLambdaParser#catchExpression.
    def visitCatchExpression(self, ctx):
        return (SymbolTable.CATCH,
                self.visitParameter(ctx.parameter()),
                self.visitImplicitSeq(ctx.expression()))

    # Visit a parse tree produced by PLambdaParser#dataExpression.
    def visitDataExpression(self, ctx):
        op = SymbolTable.canonicalize(ctx.PRIMITIVE_DATA_OP().getSymbol().text)
        return (op, self.visitData(ctx.data()))

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
        return [SymbolTable.QUOTE,
                self.visitString(ctx.string())]

    # Visit a parse tree produced by PLambdaParser#oneOrMoreExpression.
    def visitOneOrMoreExpression(self, ctx):
        return self.visitExpressionList(ctx.AMBI1_OP(), ctx.expression());

    # Visit a parse tree produced by PLambdaParser#twoOrMoreExpression.
    def visitTwoOrMoreExpression(self, ctx):
        return self.visitExpressionList(ctx.AMBI2_OP(), ctx.expression());

    # Visit a parse tree produced by PLambdaParser#naryExpression.
    def visitNaryExpression(self, ctx):
        return self.visitExpressionList(ctx.N_ARY_OP(), ctx.expression()); 
