from pwn import *
from binascii import *

import sys

e = ELF('challenge')

arr = e.read(0x401d28,32)
main_=e.read(0x400b04,32)
text = hexlify(arr)
main_text = hexlify(main_)
print(main_)
print(arr)
print(text)

arr2 = [text[i:i+2] for i in range(0,len(text),2)]
arr_main = [main_text[i:i+2] for i in range(0,len(main_text),2)]

print(arr_main)
print(arr2)


numb = 0x11
def function(number,arrr):
    number = number ^ arrr
    hhh = 0xff & (number << 4 | number >> 4)
    return hhh

hex_string = ''
for i in range(0,len(arr_main)):
    hex_string += (hex(function(int(arr_main[i],16), int(arr2[i],16))).split('x')[-1].decode('hex'))

print(hex_string)

r = remote("svc.pwnable.xyz",30031)


r.sendlineafter("> ","1")
r.sendlineafter("name: ",hex_string)
r.sendlineafter("> ","4")
r.interactive()


