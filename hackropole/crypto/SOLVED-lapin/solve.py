"""
For this problem we notice that the PIN is four digits which means we can
bruteforce it.

Pretending we know the pin, we can extract the `nonce`, `c` and `tag` by
noticing that when we add bytes we actually concatenate them and we know
the lengths of the `nonce` and tag to be 16 bytes.

After that we will just create an AES object and decrypt `c`
"""
__dbg__: bool = False

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes

def dbg(text: str) -> None:
    if __dbg__:
        print(text)
    else:
        ...


def solve(nonce: bytes, c: bytes, tag: bytes) -> str:
    for pin in range(0, 10_000):
        if pin%100 == 0:
            dbg(f"{pin}")
        k: bytes = scrypt(
            long_to_bytes(pin),
            b'FCSC',
            32,
            N = 2 ** 10,
            r = 8,
            p = 1
        )

        aes = AES.new(k, AES.MODE_GCM, nonce=nonce)
        try:
            m: bytes = aes.decrypt_and_verify(c, tag)
            return m.decode()
        except ValueError:
            ...

    raise Exception("No flag found")




def main() -> None:
    with open("./output.txt", "r") as f:
        enc_str: str = f.read()
        enc_bytes: bytes = bytes.fromhex(enc_str)

        nonce: bytes = enc_bytes[:16]
        c: bytes = enc_bytes[16:-16]
        tag: bytes = enc_bytes[-16:]

        assert len(nonce) == 16
        assert len(tag) == 16
        assert nonce + c + tag == enc_bytes

    decrypted: str = solve(nonce, c, tag)

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
