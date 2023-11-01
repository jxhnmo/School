	.file	"prog.c"
	.text
	.p2align 4,,15
	.globl	bubble_sort
	.type	bubble_sort, @function
bubble_sort:
.LFB20:

#Basic Block

	addq $2,insn_count(%rip)
	.cfi_startproc
	testl	%esi, %esi
	jle	.L1

#Basic Block

	addq $4,insn_count(%rip)
	leal	-2(%rsi), %eax
	cmpl	$1, %esi
	leaq	4(%rdi,%rax,4), %r8
	jne	.L17
.L1:

#Basic Block

	addq $1,insn_count(%rip)
	rep ret
.L17:

#Basic Block

	addq $1,insn_count(%rip)
	xorl	%r10d, %r10d
	.p2align 4,,10
	.p2align 3
.L4:

#Basic Block

	addq $2,insn_count(%rip)
	movq	%rdi, %rax
	xorl	%r9d, %r9d
	.p2align 4,,10
	.p2align 3
.L8:

#Basic Block

	addq $4,insn_count(%rip)
	movl	(%rax), %ecx
	movl	4(%rax), %edx
	cmpl	%edx, %ecx
	jle	.L5

#Basic Block

	addq $3,insn_count(%rip)
	movl	%ecx, 4(%rax)
	movl	%edx, (%rax)
	movl	$1, %r9d
.L5:

#Basic Block

	addq $3,insn_count(%rip)
	addq	$4, %rax
	cmpq	%r8, %rax
	jne	.L8

#Basic Block

	addq $2,insn_count(%rip)
	testl	%r9d, %r9d
	je	.L1

#Basic Block

	addq $3,insn_count(%rip)
	addl	$1, %r10d
	cmpl	%esi, %r10d
	jne	.L4

#Basic Block

	addq $1,insn_count(%rip)
	rep ret
	.cfi_endproc
.LFE20:

#Basic Block

	.size	bubble_sort, .-bubble_sort
	.p2align 4,,15
	.globl	check_sorted
	.type	check_sorted, @function
check_sorted:
.LFB21:

#Basic Block

	addq $2,insn_count(%rip)
	.cfi_startproc
	cmpl	$1, %esi
	jle	.L22

#Basic Block

	addq $3,insn_count(%rip)
	movl	4(%rdi), %eax
	cmpl	%eax, (%rdi)
	jg	.L24

#Basic Block

	addq $4,insn_count(%rip)
	leal	-2(%rsi), %eax
	addq	$4, %rdi
	leaq	(%rdi,%rax,4), %rdx
	jmp	.L20

#Basic Block

	.p2align 4,,10
	.p2align 3
.L21:

#Basic Block

	addq $4,insn_count(%rip)
	movl	(%rdi), %eax
	addq	$4, %rdi
	cmpl	(%rdi), %eax
	jg	.L24
.L20:

#Basic Block

	addq $2,insn_count(%rip)
	cmpq	%rdx, %rdi
	jne	.L21
.L22:

#Basic Block

	addq $2,insn_count(%rip)
	movl	$1, %eax
	ret
	.p2align 4,,10
	.p2align 3
.L24:

#Basic Block

	addq $2,insn_count(%rip)
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE21:

#Basic Block

	.size	check_sorted, .-check_sorted
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:

#Basic Block

	.string	"numbers are sorted"
.LC1:

#Basic Block

	.string	"numbers are not sorted"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB22:

#Basic Block

	addq $2,insn_count(%rip)
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$numbers, %ebx
	.p2align 4,,10
	.p2align 3
.L27:

#Basic Block

	addq $5,insn_count(%rip)
	call	rand
	addq	$4, %rbx
	movl	%eax, -4(%rbx)
	cmpq	$numbers+40000, %rbx
	jne	.L27

#Basic Block

	addq $6,insn_count(%rip)
	movl	$10000, %esi
	movl	$numbers, %edi
	call	bubble_sort
	movl	$numbers+4, %eax
	movl	numbers(%rip), %ecx
	jmp	.L30

#Basic Block

	.p2align 4,,10
	.p2align 3
.L33:

#Basic Block

	addq $3,insn_count(%rip)
	addq	$4, %rax
	cmpq	$numbers+40000, %rax
	je	.L29

#Basic Block

	addq $1,insn_count(%rip)
	movl	%edx, %ecx
.L30:

#Basic Block

	addq $3,insn_count(%rip)
	movl	(%rax), %edx
	cmpl	%ecx, %edx
	jge	.L33

#Basic Block

	addq $2,insn_count(%rip)
	movl	$.LC1, %edi
	call	puts
.L31:

#Basic Block

	addq $2,insn_count(%rip)
	xorl	%edi, %edi
	
	#printing count
    
	movq    insn_count, %rax
	movq    %rax, %rsi
    leaq    fmt_string(%rip), %rdi
    movl    $0, %eax
    call    printf@PLT
	call	exit
.L29:

#Basic Block

	addq $3,insn_count(%rip)
	movl	$.LC0, %edi
	call	puts
	jmp	.L31

#Basic Block

	.cfi_endproc
.LFE22:

#Basic Block

	.size	main, .-main
	.comm	numbers,40000,32
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-44)"
	.section	.note.GNU-stack,"",@progbits

.data
insn_count: .quad 0
fmt_string: .asciz "%lld instructions executed"