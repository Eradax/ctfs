#!/usr/bin/env python3
"""
This is normal RSA except for the fact that `n` only has one primefactor
this allows us to easly find `d` and then decrypt the message.
"""

from Crypto.Util.number import long_to_bytes, inverse

def solve(n: int, e: int, c: int):
    d: int = inverse(e, n-1)

    m = pow(c, d, n)

    return m

def main():
    n: int
    e: int
    c: int

    with open("./output.txt", "r") as f:
        raw_data: str = f.read()

        n, e, c = (int(i[4:]) for i in raw_data.split('\n')[:-1])
    
    # assert n.isinstance(int)
    # assert e.isinstance(int)
    # assert c.isinstance(int)

    decrypted_long: int = solve(n, e, c)

    decrypted_bytes: bytes = long_to_bytes(decrypted_long)

    print("The decrypted text is:")
    print(decrypted_bytes.decode())

if __name__ == "__main__":
    main()
