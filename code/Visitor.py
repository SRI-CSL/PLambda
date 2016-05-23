from PLambdaVisitor import PLambdaVisitor

class Visitor(PLambdaVisitor):

    # Visit a parse tree produced by PLambdaParser#unit.
    def visitUnit(self, ctx):
        print "Visitor visiting unit"
        return self.visitChildren(ctx)
