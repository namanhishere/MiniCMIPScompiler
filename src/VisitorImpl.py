
from antlr4 import *
from gen.MiniCVisitor import MiniCVisitor
from gen.MiniCParser import MiniCParser
from .CodeGenMIPS import CodeGenMIPS

class VisitorImpl(MiniCVisitor):
    def __init__(self, codegen: CodeGenMIPS):
        super().__init__()
        self.g = codegen

    # program: (decl | stmt)* EOF ;
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        self.g.prologue()
        for child in ctx.getChildren():
            if isinstance(child, MiniCParser.DeclContext):
                self.visit(child)
            elif isinstance(child, MiniCParser.StmtContext):
                self.visit(child)
        self.g.epilogue()
        return None

    # decl: 'int' ID ('=' expr)? ';' ;
    def visitDecl(self, ctx:MiniCParser.DeclContext):
        name = ctx.ID().getText()
        self.g.ensure_var(name)
        if ctx.expr():
            r = self.visit(ctx.expr())
            self.g.assign(name, r)
        return None

    # stmt: assign ';' | printStmt ';' | ifStmt | whileStmt | block ;
    def visitStmt(self, ctx:MiniCParser.StmtContext):
        if ctx.assign():
            name, r = self.visit(ctx.assign())
            self.g.assign(name, r)
        elif ctx.printStmt():
            r = self.visit(ctx.printStmt())
            self.g.print_int(r, newline=True)
        elif ctx.ifStmt():
            self.visit(ctx.ifStmt())
        elif ctx.whileStmt():
            self.visit(ctx.whileStmt())
        elif ctx.block():
            self.visit(ctx.block())
        elif ctx.forStmt():
            self.visit(ctx.forStmt())
        return None

    # assign: ID '=' expr ;
    def visitAssign(self, ctx:MiniCParser.AssignContext):
        name = ctx.ID().getText()
        r = self.visit(ctx.expr())
        return name, r

    # printStmt: 'print' '(' expr ')' ;
    def visitPrintStmt(self, ctx:MiniCParser.PrintStmtContext):
        return self.visit(ctx.expr())

    # ifStmt: 'if' '(' expr ')' stmt ('else' stmt)? ;
    def visitIfStmt(self, ctx:MiniCParser.IfStmtContext):
        rcond = self.visit(ctx.expr())
        Lelse, Lend = self.g.if_else_labels()
        self.g.if_jump_if_false(rcond, Lelse)
        self.visit(ctx.stmt(0))  # then
        if ctx.getChildCount() > 5:  # has else
            self.g.if_end_then_jump(Lend)
            self.g.place_label(Lelse)
            self.visit(ctx.stmt(1))
            self.g.place_label(Lend)
        else:
            self.g.place_label(Lelse)
        return None

    # whileStmt: 'while' '(' expr ')' stmt ;
    def visitWhileStmt(self, ctx:MiniCParser.WhileStmtContext):
        Lstart, Lend = self.g.begin_while()
        rcond = self.visit(ctx.expr())
        self.g.while_cond(rcond, Lend)
        self.visit(ctx.stmt())
        self.g.end_while(Lstart, Lend)
        return None

    # block: '{' (decl | stmt)* '}' ;
    def visitBlock(self, ctx:MiniCParser.BlockContext):
        for ch in ctx.children[1:-1]:
            self.visit(ch)
        return None

    # --- Expressions ---
    def visitNumberExpr(self, ctx:MiniCParser.NumberExprContext):
        val = int(ctx.NUMBER().getText())
        return self.g.load_number(val)

    def visitIdExpr(self, ctx:MiniCParser.IdExprContext):
        name = ctx.ID().getText()
        return self.g.load_var(name)

    def visitParenExpr(self, ctx:MiniCParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx:MiniCParser.UnaryMinusExprContext):
        r = self.visit(ctx.expr())
        return self.g.unary_minus(r)

    def visitAddSubExpr(self, ctx:MiniCParser.AddSubExprContext):
        ra = self.visit(ctx.expr(0))
        rb = self.visit(ctx.expr(1))
        op = ctx.op.text
        return self.g.binop_arith(op, ra, rb)

    def visitMulDivExpr(self, ctx:MiniCParser.MulDivExprContext):
        ra = self.visit(ctx.expr(0))
        rb = self.visit(ctx.expr(1))
        op = ctx.op.text
        return self.g.binop_arith(op, ra, rb)

    def visitCmpExpr(self, ctx:MiniCParser.CmpExprContext):
        ra = self.visit(ctx.expr(0))
        rb = self.visit(ctx.expr(1))
        op = ctx.op.text
        return self.g.binop_cmp(op, ra, rb)
    
    def visitPostfixadd(self, ctx:MiniCParser.PostfixaddContext):
        name = ctx.ID().getText()
        self.g.ensure_var(name)
        r = self.g.load_var(name)
        self.g.assign(name, self.g.binop_arith("+", r, self.g.load_number(1)))
        return None

    def visitPostfixdec(self, ctx:MiniCParser.PostfixdecContext):
        name = ctx.ID().getText()
        self.g.ensure_var(name)
        r = self.g.load_var(name)
        self.g.assign(name, self.g.binop_arith("-", r, self.g.load_number(1)))
        return None

    # forStmt: 'for' '(' forInit ';' forCond ';' forStep ')' stmt ;
    def visitForStmt(self, ctx):
        # 1) init
        self.visit(ctx.forInital())

        # 2) nhãn vòng lặp
        Lstart, Lend = self.g.begin_while()

        # 3) cond (rỗng => true)
        rcond = self.visit(ctx.forCondition())
        self.g.while_cond(rcond, Lend)

        # 4) thân
        self.visit(ctx.stmt())

        # 5) step
        self.visit(ctx.forStep())

        # 6) nhảy về đầu + kết thúc
        self.g.end_while(Lstart, Lend)
        return None

    # --- forInit ---
    def visitForInitDecl(self, ctx):
        name = ctx.ID().getText()
        self.g.ensure_var(name)
        if ctx.e is not None:
            r = self.visit(ctx.e)
            self.g.assign(name, r)
        return None

    def visitForInitAssign(self, ctx):
        name = ctx.ID().getText()
        r = self.visit(ctx.e)
        self.g.ensure_var(name)   # demo: chấp nhận “dùng luôn nếu chưa khai báo”
        self.g.assign(name, r)
        return None

    def visitForInitEmpty(self, ctx): return None

    # --- forCond ---
    def visitForCondExpr(self, ctx):
        return self.visit(ctx.e)

    def visitForCondEmpty(self, ctx):
        return self.g.load_number(1)  # true

    # --- forStep ---
    def visitForStepAssign(self, ctx):
        name = ctx.ID().getText()
        r = self.visit(ctx.e)
        self.g.assign(name, r)
        return None



