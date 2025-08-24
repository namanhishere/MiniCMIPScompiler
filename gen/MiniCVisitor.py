# Generated from ./grammar/MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#decl.
    def visitDecl(self, ctx:MiniCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stmt.
    def visitStmt(self, ctx:MiniCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assign.
    def visitAssign(self, ctx:MiniCParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printStmt.
    def visitPrintStmt(self, ctx:MiniCParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ifStmt.
    def visitIfStmt(self, ctx:MiniCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#whileStmt.
    def visitWhileStmt(self, ctx:MiniCParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forStmt.
    def visitForStmt(self, ctx:MiniCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#block.
    def visitBlock(self, ctx:MiniCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forInitDecl.
    def visitForInitDecl(self, ctx:MiniCParser.ForInitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forInitAssign.
    def visitForInitAssign(self, ctx:MiniCParser.ForInitAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forInitEmpty.
    def visitForInitEmpty(self, ctx:MiniCParser.ForInitEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forCondExpr.
    def visitForCondExpr(self, ctx:MiniCParser.ForCondExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forCondEmpty.
    def visitForCondEmpty(self, ctx:MiniCParser.ForCondEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forStepAssign.
    def visitForStepAssign(self, ctx:MiniCParser.ForStepAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forStepEmpty.
    def visitForStepEmpty(self, ctx:MiniCParser.ForStepEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#addSubExpr.
    def visitAddSubExpr(self, ctx:MiniCParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MiniCParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#postfixminus.
    def visitPostfixminus(self, ctx:MiniCParser.PostfixminusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#numberExpr.
    def visitNumberExpr(self, ctx:MiniCParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#postfixadd.
    def visitPostfixadd(self, ctx:MiniCParser.PostfixaddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:MiniCParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parenExpr.
    def visitParenExpr(self, ctx:MiniCParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idExpr.
    def visitIdExpr(self, ctx:MiniCParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#cmpExpr.
    def visitCmpExpr(self, ctx:MiniCParser.CmpExprContext):
        return self.visitChildren(ctx)



del MiniCParser