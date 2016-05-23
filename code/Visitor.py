from PLambdaVisitor import PLambdaVisitor

class Visitor(PLambdaVisitor):

    # Visit a parse tree produced by PLambdaParser#unit.
    def visitUnit(self, ctx):
        retval = []
        for exp in ctx.expression():
            retval.append(self.visit(exp))
        return retval

    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PLambdaParser#stringLiteral.
    def visitStringLiteral(self, ctx):
        return ctx.STRING().getSymbol().text

    # Visit a parse tree produced by PLambdaParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx):
        return ctx.ID().getSymbol().text

    # Visit a parse tree produced by PLambdaParser#invokeExpression.
    def visitInvokeExpression(self, ctx):
        return self.visitExpressionList(ctx.INVOKE(), ctx.expression())
    
    def visitExpressionList(self, tsym, explist):
        retval = [tsym.getSymbol().text]
        for e in explist:
            retval.append(self.visit(e))
        return retval
