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

