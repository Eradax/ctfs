"""
In this problem `flag.jpg.enc` has been encrypted using AES-128 in CTR mode, with the 128-bit key `00112233445566778899aabbccddeeff` and the all-zero IV.

to solve the problem we will simply reverse this process.
"""

from Crypto.Cipher import AES
from Crypto.Util import Counter
def solve(c: bytes, key: bytes, iv: int):
    counter = Counter.new(128, initial_value = iv)
    aes = AES.new(key, AES.MODE_CTR, counter = counter)

    m: bytes = aes.decrypt(c)

    with open("./flag.jpg", "wb") as f:
        f.write(m)
    

def main() -> None:
    with open("./flag.jpg.enc", "rb") as f:
        enc: bytes = f.read()

    key_str: str = "00112233445566778899aabbccddeeff"
    key_bytes: bytes = bytes.fromhex(key_str)

    iv: int = 0

    solve(enc, key_bytes, iv)

    print("The decryption went successfully, see the result in `./flag.jpg`")

if __name__ == "__main__":
    main()
