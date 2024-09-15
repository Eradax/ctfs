#!/usr/bin/env python3

import pwn

pwn.context.log_level = "warn"

r = pwn.remote("188.126.67.132", 50015)

e = pwn.ELF("./service")

passwd: str
passwd = ""

while (e.read(e.symbols["password"]+len(passwd), 1)) != b'\x00':
    passwd += e.read(e.symbols["password"]+len(passwd), 1).decode()

# print(f"{passwd = }")

r.recvuntil(b"Invaded!\n")
r.sendline(passwd.encode())

r.recvuntil(b"flag:\n")
flag = r.recvline().decode().strip()

print(flag)

