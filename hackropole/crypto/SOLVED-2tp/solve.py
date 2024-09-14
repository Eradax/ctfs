"""
For this problem we can interact with a remote, the remote gives us the
decrypted flag and we can send our own data to encrypt.

By sending multiple requests we can leak the flag since the xor of the
encrypted data is the same as with the unencrypted data.
"""
from pwn import remote
from Crypto.Util.strxor import strxor

def sendQuery(text: str) -> tuple[bytes]:
    r = remote("localhost", 4000)

    r.recvuntil(b'flag: ')
    enc_flag: bytes = bytes.fromhex(r.recvline().decode().strip())
    
    r.recvuntil(b'enter your text: ')
    r.sendline(text.encode())

    r.recvuntil(b'ciphertext: ')
    enc: bytes = bytes.fromhex(r.recvline().decode().strip())

    return enc, enc_flag

def solve() -> str:
    p1: str = '1'*48
    enc: bytes
    enc_flag: bytes

    enc, enc_flag = sendQuery(p1) 

    if len(enc) != len(enc_flag) != len(p1):
        min_len: int = min(len(enc), len(enc_flag), len(p1))

        enc = enc[:min_len] 
        enc_flag = enc_flag[:min_len]
        p1 = p1[:min_len]
   
    flag: bytes = strxor(p1.encode(), strxor(enc, enc_flag))

    return flag.decode(errors = "ignore")

def main() -> None:
    decrypted: str = solve()

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
