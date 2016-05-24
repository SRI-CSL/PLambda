from PLambdaVisitor import PLambdaVisitor

class Visitor(PLambdaVisitor):

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

    # Visit a parse tree produced by PLambdaParser#invokeExpression.
    def visitInvokeExpression(self, ctx):
        return self.visitExpressionList(ctx.INVOKE(), ctx.expression())
    
    def visitExpressionList(self, tsym, explist):
        retval = [tsym.getSymbol().text]
        for e in explist:
            retval.append(self.visit(e))
        return retval


    ###################### HERE ####################################
    
    # Visit a parse tree produced by PLambdaParser#seqExpression.
    def visitSeqExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#letExpression.
    def visitLetExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#defineExpression.
    def visitDefineExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#applyExpression.
    def visitApplyExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#dataExpression.
    def visitDataExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binaryExpression.
    def visitBinaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#quoteExpression.
    def visitQuoteExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameter_list.
    def visitParameter_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binding_list.
    def visitBinding_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#binding_pair.
    def visitBinding_pair(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#catch_expression.
    def visitCatch_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#range_expression.
    def visitRange_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#data.
    def visitData(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#string.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#token.
    def visitToken(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLambdaParser#type_expression.
    def visitType_expression(self, ctx):
        return self.visitChildren(ctx)


    
