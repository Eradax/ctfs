#!/usr/bin/env python3
from hashlib import sha256
from sympy.ntheory.modular import crt

N = 100_000

with open("./data.txt", "r") as f:
    g: list[int] = eval(f.readline().split('=')[-1].strip())
    A: list[int] = eval(f.readline().split('=')[-1].strip())
    cflag: str = eval(f.readline().split('=')[-1].strip())

def find_steps(start: int, target: int) -> tuple[int, int]:
    pos: int = g[start]
    steps: int = 1
    cycl: int = 1
    while pos != target:
        pos = g[pos]
        steps += 1
        cycl += 1

    while pos != start:
        pos = g[pos]
        cycl += 1
    return steps, cycl

def sha256_once(b: bytes) -> bytes:
    h = sha256()
    h.update(b)
    return h.digest()

def sha256_1e6(b: str) -> str:
    h = b.encode()
    for _ in range(10**6):
        h = sha256_once(h)
    return h.hex()


steps_list = []
with open("./steps.txt", "r") as f:
    steps_list: list[tuple[int, int]] = eval(f.readline().split('=')[-1].strip())

"""
for i in range(N):
    if i % 1_000 == 0:
        print(f"{i // 1_000}%")
    steps = find_steps(g, i, A[i])

    steps_list.append(steps)
"""

#with open("./steps.txt", "w") as f:
#    print(f"{steps_list = }", file=f)

resd: list[int] = []
mods: list[int] = []

for i in steps_list:
    resd.append(i[0])
    mods.append(i[1])

a: int
mod: int
a, mod = crt(mods, resd)

while True:
    flag = f"SSM{{{a}}}"

    if sha256_1e6(flag) == cflag:
        break
    a += mod

flag = f"SSM{{{a}}}"
print(flag)
