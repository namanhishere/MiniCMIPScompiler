.data
var_sum: .word 0
var_i: .word 0

.text
.globl main
main:
    li   $t0, 0
    sw   $t0, var_sum
    li   $t0, 1
    sw   $t0, var_i
Lstart1:
    lw   $t0, var_i
    li   $t1, 5
    slt  $t2, $t1, $t0
    xori $t2, $t2, 1
    beq  $t2, $zero, Lend2
    lw   $t2, var_sum
    lw   $t1, var_i
    add  $t0, $t2, $t1
    sw   $t0, var_sum
    lw   $t0, var_i
    li   $t1, 1
    add  $t2, $t0, $t1
    sw   $t2, var_i
    j    Lstart1
Lend2:
    lw   $t2, var_sum
    move $a0, $t2
    li   $v0, 1
    syscall
    li   $a0, 10
    li   $v0, 11
    syscall
    li   $v0, 10
    syscall