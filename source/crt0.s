.section .crt0, "ax", %progbits
.global _start
.extern __nx_module_runtime
.global course

_start:
    .word 0
    .word __nx_mod0 - _start

__nx_mod0:
    .ascii "MOD0"
    .word  _DYNAMIC             - __nx_mod0
    .word  __bss_start__        - __nx_mod0
    .word  __bss_end__          - __nx_mod0
    .word  __eh_frame_hdr_start - __nx_mod0
    .word  __eh_frame_hdr_end   - __nx_mod0
	.word  __nx_module_runtime  - __nx_mod0

    .space 0x10000