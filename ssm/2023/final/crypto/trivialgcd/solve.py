#!/usr/bin/env python3
import math
from Crypto.Util.number import long_to_bytes

#NOTE: This program takes roughly two hours to run
"""
c1 + p*q*k = m**e1
c2 + p*r*j = m**e2

c1 = m**e1 (mod p*q)
c2 = m**e2 (mod p*r)

=>

p*q*k = m**e1 - c1 = q1
p*r*j = m**e2 - c2 = q2

p = gcd(q1, q2)

wlog e1 <= e2

m**e1 = k

p = gcd(k - c1, k*m**(e2-e1)-c2)

p = gcd(m**e1 - c1, m**e2 - c2)
p = gcd(m**e1 - c1 (mod m**e2 - c2), m**e2 - c2)

p = gcd(m**e1 - c1, m**e2 - c2)

= (m**e1 - c1, m**e2 - c2 - (m**(e2 - e1) * (m ** e1 - c1)))
= (m**e1 - c1, m**e2 - (m**(e2 - e1) * (m ** e1 - c1)) - c2)

m**e2 - (m**(e2 - e1) * (m ** e1 - c1)) - c2)
m**(e2-e1)*(m**e1 - m**e1 + c1) - c2
c1 * m**(e2-e1) - c2

=>

p = gcd(m**e1, c1 * m**(e2-e1) - c2)

-------

wlog y > b
gcd(c2**a * m**b - c1**c, c1**x * m**y - c2**z)
(c2**a * m**b - c1**c, c2**a * c1**x * m**y - c2**(z+a))
(c2**a * m**b - c1**c, c2**a * c1**x * m**y - c2**(z+a) - c1**x * m ** (y-b)*(m**b * c2**a - c1**c))
(c2**a * m**b - c1**c, c2**a * c1**x * m**y - m**(y - b)*(m**b * c1**x * c2**a - c1**(c+x)))
(c2**a * m**b - c1**c, m**(y-b)*(c2** a * c1**x * m**b - c2 ** a * c1**x * m**b + c1**(c+x)) - c2**(z+a))
(c2**a * m**b - c1**c, c1**(c+x)*m**(y-b) - c2**(z+a))

i.e.
gcd(c2**a * m**b - c1**c, c1**x * m**y - c2**z)
=> if y > b
gcd(c2**a * m**b - c1**c, c1**(c+x) * m**(y-b) - c2**(a+z))

compute time:

O(gcd(c2**a * m**b - c1**c, c1**x * m**y - c2**z))
=
O(max(c2**a * m**b - c1**c, c1**x * m**y - c2**z))
= (because c1 ~= c2 ~= m)
O(max(m**(a + b) - m**c, m**(x + y) - m**z))

Help me!!!

----

Q: What the hell are you doing here?!
A: To solve this problem we will first symbolicly make the exponents of `m`
smaller, we do this by some clever multiplication and applying properties of
gcd. The tradeoff for decreasing the exponent of `m` is increasing the other
exponents. To solve this we estimate the timecomplexity of the gcd and look if
the next iteration is slower, then we stop.
"""

def ct(a: int, b: int, c: int, x: int, y: int, z: int) -> int:
    return max(a+b, c, x+y, z)

with open("./data.txt", "r") as f:
    m: int = int(f.readline().strip().split('=')[-1])
    e1: int = int(f.readline().strip().split('=')[-1])
    e2: int = int(f.readline().strip().split('=')[-1])
    c1: int = int(f.readline().strip().split('=')[-1])
    c2: int = int(f.readline().strip().split('=')[-1])
    cipher: int = int(f.readline().strip().split('=')[-1])

a: int = 0
b: int = e1
c: int = 1

x: int = 0
y: int = e2
z: int = 1

curr = ct(a, b, c, x, y, z)
nxt = curr

na: int = 0
nb: int = e1
nc: int = 1
nx: int = 0
ny: int = e2
nz: int = 1

first = True

while nxt <= curr or first:
    first = False

    a = na
    b = nb
    c = nc
    x = nx
    y = ny
    z = nz
    curr = nxt

    # print(f"{curr, nxt = }")
    # print(f"{a, b, c = }")
    # print(f"{x, y, z = }")

    if y >= b:
        # print("y")
        na = a
        nb = b
        nc = c

        nx = x + c
        ny = y - b
        nz = z + a
    elif y < b:
        # print("b")
        na = a + z
        nb = b - y
        nc = c + x

        nx = x
        ny = y
        nz = z

    nxt = ct(na, nb, nc, nx, ny, nz)

# print("--------------")
# print(f"{curr, nxt = }")
# print(f"{a, b, c = }")
# print(f"{x, y, z = }")

g1: int
g2: int

if ct(a, b, c, 0, 0, 0) < ct(0, 0, 0, x, y, z):
    g1 = c2**a * m**b - c1**c
    g2 = (pow(c1, x, g1) * pow(m, y, g1) - pow(c2, z, g1))
else:
    g1 = c1**x * m**y - c2**z
    g2 = (pow(c2, a, g1) * pow(m, b, g1) - pow(c1, c, g1))

"""
gcd = math.gcd(
    c2**a * m**b - c1**c,
    c1**(c+x) * m**(y-b) - c2**(a+z)
)
"""

# print(f"{g1, g2 = }")

gcd = math.gcd(
    g1,
    g2
)

# print(f"{gcd = }")

phi = (gcd-1) * gcd ** 9

# print(f"{phi = }")

d = pow(2**16+1, -1, phi)

# print(f"{d = }")

msg = pow(cipher, d, gcd**10)

print(long_to_bytes(msg).decode()[::-1])
