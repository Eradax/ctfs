#!/usr/bin/env python3
import randcrack
import pwn

pwn.context.log_level = "warn"

r = pwn.remote("188.126.67.132", 50018)
# r = pwn.process("./service.py")

rc = randcrack.RandCrack()

for i in range(624):
    r.recvuntil(b"Enter integer to encropt:\n")
    r.sendline(b'0')
    r.recvuntil(b"Encropted: ")
    res = int(r.recvline().decode().strip())
    rc.submit(res)

r.sendline()
r.recvuntil(b"Super Secure Message:\n")

enc = r.recvline().decode().strip()

FLAG = enc.removeprefix("SSM{").removesuffix("}")
FLAG1, FLAG2 = int(FLAG[:len(FLAG)//2]), int(FLAG[len(FLAG)//2:])

FLAG1 = str(rc.predict_getrandbits(32) ^ FLAG1)
FLAG2 = str(rc.predict_getrandbits(32) ^ FLAG2)

print("SSM{" + FLAG1 + FLAG2 + "}")

