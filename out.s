.data
var_a: .word 0
var_b: .word 0
var_c: .word 0

.text
.globl main
main:
    li   $t0, 0
    sw   $t0, var_a
    lw   $t0, var_a
    lw   $t1, var_b
    add  $t2, $t0, $t1
    li   $t1, 2
    div  $t2, $t1
    mflo $t0
    sw   $t0, var_c
    lw   $t0, var_c
    move $a0, $t0
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    li   $v0, 10
    syscall