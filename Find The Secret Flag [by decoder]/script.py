#!/usr/bin/python

from pwn import *
from binascii import *

context.log_level = "debug"


process("echo '\xDE\xAD\xBE\xEF' > /tmp/secret", shell=1)


for i in range(0, 256):

r = process("./secret_flag.bin %d" % i, shell=1).readline().strip()

log.info("len() = %d", len(r))

if len(r) == 34:

r = '0' + r

if len(r) != 34 and len(r) != 36:
continue

log.info(r)
log.info("unhex = %s" % unhexlify(r))