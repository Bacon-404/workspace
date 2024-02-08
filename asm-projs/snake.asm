;-------------------------------------------------------;
;Snake game written by Bacon_404, use at your own risk. ;
;-------------------------------------------------------;

;Complier directions

.386                                ; Full 80386 instruction set
.model flat, stdcall                ; 32-bit memory model
option casemap:none                 ; case sensitive

;Includes files

include \masm32\include\windows.inc ; Windows.inc
include \masm32\include\kernel32.inc; Kernel32.inc
include \masm32\include\user32.inc  ; User32.inc
include \masm32\include\gdi32.inc   ; GDI32.inc

; Libraries

includelib \masm32\lib\kernel32.lib ; Kernel32.lib
includelib \masm32\lib\user32.lib   ; User32.lib
includelib \masm32\lib\gdi32.lib    ; GDI32.lib

;Forward declarations

WinMain PROTO :DWORD,:DWORD,:DWORD,:DWORD

;Constants and variables

WindowWidth equ 800
WindowHeight equ 600

ClassName db "SnakeClass",0
AppName db "Snake Game",0

MainEntry
    push NULL
    call GetModuleHandle
    mov hInstance, eax
    
    call GetCommandLine
    mov CommandLine, eax
    
    push SW_SHOWDEFAULT
    lea eax, CommandLine
    push eax
    push NULL
    push hInstance
    call WinMain
    
    push eax
    call ExitProcess
    