# Generated from ./grammar/MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#decl.
    def enterDecl(self, ctx:MiniCParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniCParser#decl.
    def exitDecl(self, ctx:MiniCParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniCParser#stmt.
    def enterStmt(self, ctx:MiniCParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#stmt.
    def exitStmt(self, ctx:MiniCParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#assign.
    def enterAssign(self, ctx:MiniCParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniCParser#assign.
    def exitAssign(self, ctx:MiniCParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniCParser#printStmt.
    def enterPrintStmt(self, ctx:MiniCParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#printStmt.
    def exitPrintStmt(self, ctx:MiniCParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#ifStmt.
    def enterIfStmt(self, ctx:MiniCParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#ifStmt.
    def exitIfStmt(self, ctx:MiniCParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#whileStmt.
    def enterWhileStmt(self, ctx:MiniCParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#whileStmt.
    def exitWhileStmt(self, ctx:MiniCParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#forStmt.
    def enterForStmt(self, ctx:MiniCParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#forStmt.
    def exitForStmt(self, ctx:MiniCParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#block.
    def enterBlock(self, ctx:MiniCParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniCParser#block.
    def exitBlock(self, ctx:MiniCParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniCParser#forInitDecl.
    def enterForInitDecl(self, ctx:MiniCParser.ForInitDeclContext):
        pass

    # Exit a parse tree produced by MiniCParser#forInitDecl.
    def exitForInitDecl(self, ctx:MiniCParser.ForInitDeclContext):
        pass


    # Enter a parse tree produced by MiniCParser#forInitAssign.
    def enterForInitAssign(self, ctx:MiniCParser.ForInitAssignContext):
        pass

    # Exit a parse tree produced by MiniCParser#forInitAssign.
    def exitForInitAssign(self, ctx:MiniCParser.ForInitAssignContext):
        pass


    # Enter a parse tree produced by MiniCParser#forInitEmpty.
    def enterForInitEmpty(self, ctx:MiniCParser.ForInitEmptyContext):
        pass

    # Exit a parse tree produced by MiniCParser#forInitEmpty.
    def exitForInitEmpty(self, ctx:MiniCParser.ForInitEmptyContext):
        pass


    # Enter a parse tree produced by MiniCParser#forCondExpr.
    def enterForCondExpr(self, ctx:MiniCParser.ForCondExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#forCondExpr.
    def exitForCondExpr(self, ctx:MiniCParser.ForCondExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#forCondEmpty.
    def enterForCondEmpty(self, ctx:MiniCParser.ForCondEmptyContext):
        pass

    # Exit a parse tree produced by MiniCParser#forCondEmpty.
    def exitForCondEmpty(self, ctx:MiniCParser.ForCondEmptyContext):
        pass


    # Enter a parse tree produced by MiniCParser#forStepAssign.
    def enterForStepAssign(self, ctx:MiniCParser.ForStepAssignContext):
        pass

    # Exit a parse tree produced by MiniCParser#forStepAssign.
    def exitForStepAssign(self, ctx:MiniCParser.ForStepAssignContext):
        pass


    # Enter a parse tree produced by MiniCParser#forStepEmpty.
    def enterForStepEmpty(self, ctx:MiniCParser.ForStepEmptyContext):
        pass

    # Exit a parse tree produced by MiniCParser#forStepEmpty.
    def exitForStepEmpty(self, ctx:MiniCParser.ForStepEmptyContext):
        pass


    # Enter a parse tree produced by MiniCParser#addSubExpr.
    def enterAddSubExpr(self, ctx:MiniCParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#addSubExpr.
    def exitAddSubExpr(self, ctx:MiniCParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:MiniCParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:MiniCParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#postfixminus.
    def enterPostfixminus(self, ctx:MiniCParser.PostfixminusContext):
        pass

    # Exit a parse tree produced by MiniCParser#postfixminus.
    def exitPostfixminus(self, ctx:MiniCParser.PostfixminusContext):
        pass


    # Enter a parse tree produced by MiniCParser#numberExpr.
    def enterNumberExpr(self, ctx:MiniCParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#numberExpr.
    def exitNumberExpr(self, ctx:MiniCParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#postfixadd.
    def enterPostfixadd(self, ctx:MiniCParser.PostfixaddContext):
        pass

    # Exit a parse tree produced by MiniCParser#postfixadd.
    def exitPostfixadd(self, ctx:MiniCParser.PostfixaddContext):
        pass


    # Enter a parse tree produced by MiniCParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:MiniCParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:MiniCParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#parenExpr.
    def enterParenExpr(self, ctx:MiniCParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#parenExpr.
    def exitParenExpr(self, ctx:MiniCParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#idExpr.
    def enterIdExpr(self, ctx:MiniCParser.IdExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#idExpr.
    def exitIdExpr(self, ctx:MiniCParser.IdExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#cmpExpr.
    def enterCmpExpr(self, ctx:MiniCParser.CmpExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#cmpExpr.
    def exitCmpExpr(self, ctx:MiniCParser.CmpExprContext):
        pass



del MiniCParser