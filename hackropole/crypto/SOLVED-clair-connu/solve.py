#!/usr/bin/env python3
"""
os.urandom(4) return 4 bytes as a bytestring, since we know the first for bytes
of the flag (`FCSC`) we can use strxor again to decode the os.urandom bytes and
then we xor the entire encrypted text with it.
"""

from Crypto.Util.strxor import strxor

def solve(c: bytes):
    FLAG_FIRST_4 = b'FCSC'
    
    key: bytes = strxor(FLAG_FIRST_4, c[:4])
    key *= 20

    m: bytes = strxor(c, key[:len(c)])

    return m.decode()


def main():
    with open("./output.txt", "r") as f:
        encrypted_str: str = f.read()

        encrypted_bytes: bytes = bytes.fromhex(encrypted_str)

    decrypted: str = solve(encrypted_bytes)

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
