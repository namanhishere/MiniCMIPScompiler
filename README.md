# Mini C Compiler to MIPS
Tui phải học được một cái gì đó từ cái môn PPL này

## Overview
This is a project using antlr4 to for lexcial and praser to build a Compiler from a modified version of C to MIPS.  
Just only some small function of C is supported, but it will be extend more when I fully understand this Compiler course

## What is currently supporteed
* Variable
* if statement
* Math function (+,-,*,/)
* while loop
* for loop


## Demo

``` c
int a = 0;
int b;

int c =  (a + b)/2;

print(c);
```

It can be compile to:
```mips
.data
var_a: .word 0
var_b: .word 0
var_c: .word 0

.text
.globl main
main:
    # this is load to temporarily register 
    li   $t0, 0
    sw   $t0, var_a
    lw   $t0, var_a
    lw   $t1, var_b
    
    add  $t2, $t0, $t1 # perform (a+b) add command

    li   $t1, 2
    div  $t2, $t1
    mflo $t0     #perfrom division commands
    sw   $t0, var_c 
    # this is the end of int c = (a+b)/2

    #perfrom print commands
    lw   $t0, var_c
    move $a0, $t0
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall

    #end of functiom
    li   $v0, 10
    syscall
```

# Usage
Requirement to build: 
* Java
* Python-3

**Step 1 (build the lexical)**: Using antlr4 to buld the Lexer and Praser:
```
java -jar ./antlr4.jar -Dlanguage=Python3 -visitor ./grammar/MiniC.g4 -o gen
```
**Step 2 (Run the compiler)**: The compiler can be run using python:
```
python -m src.main [input Mini-C file] [output mips file]
```

For example
```
python -m src.main examples/sample.mc out.s
```
