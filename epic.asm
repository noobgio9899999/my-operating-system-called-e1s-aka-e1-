default rel
section .data
    msg db "mov eax, ecx", 13, 10 ; Message with CR+LF
    msglen equ $ - msg ; Length of message
    STD_OUTPUT_HANDLE equ -11 ; Windows constant for stdout
    NULL equ 0
section .bss
    stdout resq 1 ; Reserve space for handle
    written resq 1 ; Reserve space for bytes written
section .text
global epic
epic:
    ; Set up stack frame
    push rbp
    mov rbp, rsp
    sub rsp, 32 ; Shadow space for function calls

    ; Get handle to stdout
    mov ecx, STD_OUTPUT_HANDLE
    call GetStdHandle
    mov qword [rel stdout], rax

    ; Write to console
    mov rcx, qword [rel stdout] ; Console handle
    lea rdx, [rel msg] ; Message to write
    mov r8, msglen ; Message length
    lea r9, [rel written] ; Bytes written
    push NULL ; Overlapped
    sub rsp, 32 ; Shadow space
    call WriteConsoleA
    add rsp, 40 ; Clean up stack (32 + 8)
    ; Exit program
    xor ecx, ecx ; Exit code 0
    call ExitProcess
section .data
    msg db "i am epic", 13, 10 ; Message with CR+LF
    msglen equ $ - msg ; Length of message
    STD_OUTPUT_HANDLE equ -11 ; Windows constant for stdout
    NULL equ 0
section .bss
    stdout resq 1 ; Reserve space for handle
    written resq 1 ; Reserve space for bytes written
section .text
global main
main:
    ; Set up stack frame
    push rbp
    mov rbp, rsp
    sub rsp, 32
    mov ecx, STD_OUTPUT_HANDLE
    call GetStdHandle
    mov qword [rel stdout], rax
    mov rcx, qword [rel stdout] ; Console handle
    lea rdx, [rel msg]
    mov r8, msglen
    lea r9, [rel written]
    push NULL
    sub rsp, 32
    call WriteConsoleA
    add rsp, 40
    xor ecx, ecx ; Exit code 0
    call ExitProcess