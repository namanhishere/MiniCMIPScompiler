
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
        return "\n".join(data + self.text)
