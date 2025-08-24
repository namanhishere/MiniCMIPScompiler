# Create an ANTLR4-based mini project: MiniC (C-like subset) -> MIPS (SPIM/MARS).
# Files:
# - grammar/MiniC.g4
# - src/main.py
# - src/CodeGenMIPS.py
# - src/VisitorImpl.py
# - examples/sample.mc
# - README.md
# Finally, zip everything for download.

import os, textwrap, zipfile, json, io, pathlib

root = "./"
os.makedirs(root, exist_ok=True)
os.makedirs(f"{root}/grammar", exist_ok=True)
os.makedirs(f"{root}/src", exist_ok=True)
os.makedirs(f"{root}/examples", exist_ok=True)

mini_c_g4 = r"""
grammar MiniC;

// Entry
program : (decl | stmt)* EOF ;

// Declarations
decl : 'int' ID ('=' expr)? ';' ;

// Statements
stmt
    : assign ';'
    | printStmt ';'
    | ifStmt
    | whileStmt
    | block
    ;

assign : ID '=' expr ;
printStmt : 'print' '(' expr ')' ;

ifStmt : 'if' '(' expr ')' stmt ('else' stmt)? ;
whileStmt : 'while' '(' expr ')' stmt ;
block : '{' (decl | stmt)* '}' ;

// Expressions with ANTLR4 direct left recursion (supported)
expr
    : '-' expr                               #unaryMinusExpr
    | expr op=('*'|'/') expr                 #mulDivExpr
    | expr op=('+'|'-') expr                 #addSubExpr
    | expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr  #cmpExpr
    | '(' expr ')'                           #parenExpr
    | NUMBER                                 #numberExpr
    | ID                                     #idExpr
    ;

ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
MCOMMENT: '/*' .*? '*/' -> skip ;
"""

open(f"{root}/grammar/MiniC.g4","w").write(mini_c_g4)

codegen_py = r"""
from typing import List, Dict

class CodeGenMIPS:
    def __init__(self):
        self.text: List[str] = []
        self.data: List[str] = []
        self.vars: Dict[str, str] = {}
        self.reg_pool = [f"$t{i}" for i in range(10)]
        self.label_id = 0

    # --- utils ---
    def emit(self, line:str):
        self.text.append(line)

    def new_label(self, base="L"):
        self.label_id += 1
        return f"{base}{self.label_id}"

    def alloc(self):
        if not self.reg_pool:
            raise RuntimeError("Out of temporaries ($t0-$t9). Consider splitting expression.")
        return self.reg_pool.pop(0)

    def free(self, r:str):
        if r not in self.reg_pool:
            self.reg_pool.insert(0, r)

    def ensure_var(self, name:str):
        if name not in self.vars:
            label = f"var_{name}"
            self.vars[name] = label
            self.data.append(f"{label}: .word 0")
        return self.vars[name]

    # --- prologue/epilogue ---
    def prologue(self):
        self.text += [".text", ".globl main", "main:"]

    def epilogue(self):
        self.emit("    li   $v0, 10")
        self.emit("    syscall")

    # --- expression helpers returning a register ---
    def load_number(self, val:int):
        r = self.alloc()
        self.emit(f"    li   {r}, {val}")
        return r

    def load_var(self, name:str):
        r = self.alloc()
        label = self.ensure_var(name)
        self.emit(f"    lw   {r}, {label}")
        return r

    def binop_arith(self, op:str, ra:str, rb:str):
        r = self.alloc()
        if op == '+':
            self.emit(f"    add  {r}, {ra}, {rb}")
        elif op == '-':
            self.emit(f"    sub  {r}, {ra}, {rb}")
        elif op == '*':
            # MARS/QtSPIM allow 'mul rd, rs, rt' pseudo
            self.emit(f"    mul  {r}, {ra}, {rb}")
        elif op == '/':
            self.emit(f"    div  {ra}, {rb}")
            self.emit(f"    mflo {r}")
        else:
            raise ValueError(f'Unknown arith op {op}')
        self.free(ra); self.free(rb)
        return r

    def unary_minus(self, rx:str):
        r = self.alloc()
        self.emit(f"    sub  {r}, $zero, {rx}")
        self.free(rx)
        return r

    def binop_cmp(self, op:str, ra:str, rb:str):
        r = self.alloc()
        if op == '<':
            self.emit(f"    slt  {r}, {ra}, {rb}")
        elif op == '>':
            self.emit(f"    slt  {r}, {rb}, {ra}")
        elif op == '<=':
            self.emit(f"    slt  {r}, {rb}, {ra}")
            self.emit(f"    xori {r}, {r}, 1")
        elif op == '>=':
            self.emit(f"    slt  {r}, {ra}, {rb}")
            self.emit(f"    xori {r}, {r}, 1")
        elif op == '==':
            self.emit(f"    subu {r}, {ra}, {rb}")
            self.emit(f"    sltiu {r}, {r}, 1")
        elif op == '!=':
            self.emit(f"    subu {r}, {ra}, {rb}")
            self.emit(f"    sltu {r}, $zero, {r}")
        else:
            raise ValueError(f'Unknown cmp op {op}')
        self.free(ra); self.free(rb)
        return r

    # --- statements ---
    def assign(self, name:str, rexpr:str):
        label = self.ensure_var(name)
        self.emit(f"    sw   {rexpr}, {label}")
        self.free(rexpr)

    def print_int(self, r:str, newline=True):
        self.emit(f"    move $a0, {r}")
        self.emit(f"    li   $v0, 1")
        self.emit(f"    syscall")
        self.free(r)
        if newline:
            self.emit(f"    li   $a0, 10")
            self.emit(f"    li   $v0, 11")
            self.emit(f"    syscall")

    def begin_while(self):
        Lstart = self.new_label("Lstart")
        Lend   = self.new_label("Lend")
        self.emit(f"{Lstart}:")
        return Lstart, Lend

    def while_cond(self, rcond:str, Lend:str):
        self.emit(f"    beq  {rcond}, $zero, {Lend}")
        self.free(rcond)

    def end_while(self, Lstart:str, Lend:str):
        self.emit(f"    j    {Lstart}")
        self.emit(f"{Lend}:")

    def if_else_labels(self):
        Lelse = self.new_label("Lelse")
        Lend  = self.new_label("Lendif")
        return Lelse, Lend

    def if_jump_if_false(self, rcond:str, Lelse:str):
        self.emit(f"    beq  {rcond}, $zero, {Lelse}")
        self.free(rcond)

    def if_end_then_jump(self, Lend:str):
        self.emit(f"    j    {Lend}")

    def place_label(self, L:str):
        self.emit(f"{L}:")

    # --- final assemble ---
    def build(self)->str:
        data = [".data"] + self.data + [""] if self.data else [".data", ""]
        return "\\n".join(data + self.text)
"""

open(f"{root}/src/CodeGenMIPS.py", "w").write(codegen_py)

visitor_impl_py = r"""
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
"""

open(f"{root}/src/VisitorImpl.py", "w").write(visitor_impl_py)

main_py = r"""
import sys, os
from antlr4 import *
# Generated by ANTLR: run `antlr4 -Dlanguage=Python3 grammar/MiniC.g4 -o gen`
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.VisitorImpl import VisitorImpl
from src.CodeGenMIPS import CodeGenMIPS

def compile_file(input_path:str)->str:
    from gen.MiniCLexer import MiniCLexer
    from gen.MiniCParser import MiniCParser

    input_stream = FileStream(input_path, encoding='utf-8')
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    gen = CodeGenMIPS()
    VisitorImpl(gen).visit(tree)
    return gen.build()

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <source.mc> [out.s]")
        sys.exit(1)
    src = sys.argv[1]
    asm = compile_file(src)
    if len(sys.argv) >= 3:
        out = sys.argv[2]
    else:
        base, _ = os.path.splitext(src)
        out = base + ".s"
    with open(out, "w", encoding="utf-8") as f:
        f.write(asm)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
"""

open(f"{root}/src/main.py", "w").write(main_py)

sample = r"""
int a = 1;
int b = 2;
int c;

c = a + 2 * (b - 3);
if (c >= 0) {
    print(c);
} else {
    print(-c);
}

int i = 0;
while (i < 5) {
    a = a + b;
    i = i + 1;
}
print(a);
"""

open(f"{root}/examples/sample.mc", "w").write(sample)

readme = r"""
# MiniC (ANTLR4) → MIPS (SPIM/MARS)

A tiny C-like compiler front-end using **ANTLR4** (Python target) and a simple backend that emits **MIPS assembly**. 
Supports:
- `int` declarations with optional init
- assignments
- arithmetic `+ - * /`, unary `-`, parentheses
- comparisons `< <= > >= == !=` (yield 0/1)
- `if/else`, `while`, blocks `{ ... }`
- `print(expr);` → uses MIPS syscalls to print integer and newline

> This is intentionally small and educational. No scoping, all variables are global in `.data`.

## Layout

"""
