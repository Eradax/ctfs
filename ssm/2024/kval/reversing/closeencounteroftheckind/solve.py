#!/usr/bin/env python3

import pwn

pwn.context.log_level = "warn"

r = pwn.remote("188.126.67.132", 50015)

e = pwn.ELF("./service")

passwd: str
passwd = e.string(e.symbols["password"]).decode().strip()

# print(f"{passwd = }")

r.recvuntil(b"Invaded!\n")
r.sendline(passwd.encode())

r.recvuntil(b"flag:\n")
flag = r.recvline().decode().strip()

print(flag)

