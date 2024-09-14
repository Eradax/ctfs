#!/usr/bin/env python3
"""
For this problem we know the iv and the encrypted text and an hash of the password
in the problem we are hinted to use `rockyou` password list to brute the password.

We will begin by downloading the rockyou password list into `rockyou.txt`
"""

from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
def solve(iv: bytes, c: bytes, h: bytes) -> str:
    with open("./rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        password: bytes = b''
        for i, line in enumerate(f):
            password_guess = line[:-1]
            if not i%10_000: print(f"{password_guess = }")
            password_guess = password_guess.encode()
            hmac_test = HMAC.new(password_guess, digestmod = SHA256)
            hmac_test.update(b'FCSC2022')
            h_test: str = hmac_test.hexdigest()

            if h_test == h:
                password = password_guess
                print(f"{password = }")
                break

    k = SHA256.new(password).digest()
    m: bytes = AES.new(k, AES.MODE_CBC, iv = iv).decrypt(c)

    return m.decode()


import json
def main():
    with open("./output.txt", "r") as f:
        r: dict[str:str] = json.loads(f.read())

    iv: bytes = bytes.fromhex(r["iv"])
    c: bytes = bytes.fromhex(r["c"])
    h: str =  r["h"]

    decrypted: str = solve(iv, c, h)

    print("The decrypted text is:")
    print(decrypted)

if __name__ == "__main__":
    main()
