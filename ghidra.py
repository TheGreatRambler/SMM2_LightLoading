import sys
from keystone import Ks, KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN

ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)

print(sys.argv[1])
if sys.argv[1] == "addr":
	main_start = int(sys.argv[2], 16)
	print(hex(int(sys.argv[3], 16) - 0x7100000000 + main_start))
if sys.argv[1] == "raddr":
	main_start = int(sys.argv[2], 16)
	print(hex(int(sys.argv[3], 16) - main_start + 0x7100000000))
if sys.argv[1] == "asm":
	print(ks.asm(sys.argv[2], 0x0, True)[0].hex())