	.file	"prog.c"
	.text
	.globl	bubble_sort
	.type	bubble_sort, @function
bubble_sort:
.LFB2:

#Basic Block

	addq $6,insn_count(%rip)
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L2
.L8:

#Basic Block

	addq $3,insn_count(%rip)
	movl	$0, -12(%rbp)
	movl	$1, -8(%rbp)
	jmp	.L3
.L5:

#Basic Block

	addq $15,insn_count(%rip)
	movl	-8(%rbp), %eax
	cltq
	salq	$2, %rax
	leaq	-4(%rax), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	(%rax), %edx
	movl	-8(%rbp), %eax
	cltq
	leaq	0(,%rax,4), %rcx
	movq	-24(%rbp), %rax
	addq	%rcx, %rax
	movl	(%rax), %eax
	cmpl	%eax, %edx
	jle	.L4

#Basic Block

	addq $29,insn_count(%rip)
	movl	-8(%rbp), %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	(%rax), %eax
	movl	%eax, -16(%rbp)
	movl	-8(%rbp), %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-8(%rbp), %eax
	cltq
	salq	$2, %rax
	leaq	-4(%rax), %rcx
	movq	-24(%rbp), %rax
	addq	%rcx, %rax
	movl	(%rax), %eax
	movl	%eax, (%rdx)
	movl	-8(%rbp), %eax
	cltq
	salq	$2, %rax
	leaq	-4(%rax), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-16(%rbp), %eax
	movl	%eax, (%rdx)
	movl	$1, -12(%rbp)
.L4:

#Basic Block

	addq $1,insn_count(%rip)
	addl	$1, -8(%rbp)
.L3:

#Basic Block

	addq $3,insn_count(%rip)
	movl	-8(%rbp), %eax
	cmpl	-28(%rbp), %eax
	jl	.L5

#Basic Block

	addq $2,insn_count(%rip)
	cmpl	$0, -12(%rbp)
	jne	.L6

#Basic Block

	addq $1,insn_count(%rip)
	jmp	.L1
.L6:

#Basic Block

	addq $1,insn_count(%rip)
	addl	$1, -4(%rbp)
.L2:

#Basic Block

	addq $3,insn_count(%rip)
	movl	-4(%rbp), %eax
	cmpl	-28(%rbp), %eax
	jl	.L8
.L1:

#Basic Block

	addq $2,insn_count(%rip)
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:

#Basic Block

	.size	bubble_sort, .-bubble_sort
	.globl	check_sorted
	.type	check_sorted, @function
check_sorted:
.LFB3:

#Basic Block

	addq $6,insn_count(%rip)
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	$1, -4(%rbp)
	jmp	.L10
.L13:

#Basic Block

	addq $15,insn_count(%rip)
	movl	-4(%rbp), %eax
	cltq
	salq	$2, %rax
	leaq	-4(%rax), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	(%rax), %edx
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,4), %rcx
	movq	-24(%rbp), %rax
	addq	%rcx, %rax
	movl	(%rax), %eax
	cmpl	%eax, %edx
	jle	.L11

#Basic Block

	addq $2,insn_count(%rip)
	movl	$0, %eax
	jmp	.L12
.L11:

#Basic Block

	addq $1,insn_count(%rip)
	addl	$1, -4(%rbp)
.L10:

#Basic Block

	addq $3,insn_count(%rip)
	movl	-4(%rbp), %eax
	cmpl	-28(%rbp), %eax
	jl	.L13

#Basic Block

	addq $1,insn_count(%rip)
	movl	$1, %eax
.L12:

#Basic Block

	addq $2,insn_count(%rip)
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:

#Basic Block

	.size	check_sorted, .-check_sorted
	.comm	numbers,40000,32
	.section	.rodata
.LC0:

#Basic Block

	.string	"numbers are sorted"
.LC1:

#Basic Block

	.string	"numbers are not sorted"
	.text
	.globl	main
	.type	main, @function
main:
.LFB4:

#Basic Block

	addq $5,insn_count(%rip)
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$0, -4(%rbp)
	jmp	.L15
.L16:

#Basic Block

	addq $5,insn_count(%rip)
	call	rand
	movl	-4(%rbp), %edx
	movslq	%edx, %rdx
	movl	%eax, numbers(,%rdx,4)
	addl	$1, -4(%rbp)
.L15:

#Basic Block

	addq $2,insn_count(%rip)
	cmpl	$9999, -4(%rbp)
	jle	.L16

#Basic Block

	addq $8,insn_count(%rip)
	movl	$10000, %esi
	movl	$numbers, %edi
	call	bubble_sort
	movl	$10000, %esi
	movl	$numbers, %edi
	call	check_sorted
	testl	%eax, %eax
	je	.L17

#Basic Block

	addq $3,insn_count(%rip)
	movl	$.LC0, %edi
	call	puts
	jmp	.L18
.L17:

#Basic Block

	addq $2,insn_count(%rip)
	movl	$.LC1, %edi
	call	puts
.L18:

#Basic Block

	addq $2,insn_count(%rip)
	movl	$0, %edi

	#printing count
    
	movq    insn_count, %rax
	movq    %rax, %rsi
    leaq    fmt_string(%rip), %rdi
    movl    $0, %eax
    call    printf@PLT
	call	exit
	.cfi_endproc
.LFE4:

#Basic Block

	.size	main, .-main
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-44)"
	.section	.note.GNU-stack,"",@progbits

.data
insn_count: .quad 0
fmt_string: .asciz "%lld instructions executed"