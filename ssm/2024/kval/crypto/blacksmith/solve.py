#!/usr/bin/env python3
import pwn
import Crypto.Util.number as C
import itertools
import random
import string

pwn.context.log_level = "warn"

r = pwn.remote("188.126.67.132", 50017)
# r = pwn.process("./service.py")

r.recvuntil(b'card: ')
e, n = eval(r.recvuntil(b')'))

alnum = string.ascii_letters + string.digits


def find_nums() -> tuple[bytes, ...]:
    while True:
        v1 = random.choices(alnum, k=4)
        v2 = random.choices(alnum, k=4)
        
        b1 = C.bytes_to_long(''.join(v1).encode())
        b2 = C.bytes_to_long(''.join(v2).encode())

        b3 = b1 * b2
        v3 = C.long_to_bytes(b3)
        if v3.isalnum():
            a = ''.join(v1).encode()
            b = ''.join(v2).encode()
            c = v3

            assert C.bytes_to_long(a)*C.bytes_to_long(b) == C.bytes_to_long(c)

            return (a, b, c)


a, b, c = find_nums()

r.recvuntil(b'craft: ')
r.sendline(c)

r.recvuntil(b'of: ')
r.sendline(a)

r.recvuntil(b'else: ')
r.sendline(b)

r.recvuntil(b'samples: ')
sig1, sig2 = eval(r.recvuntil(b')'))
sig3 = (sig1*sig2)%n

r.recvuntil(b'for: ')
r.sendline(hex(sig3).encode())

flag = r.recvline().decode().strip()

print(flag)

