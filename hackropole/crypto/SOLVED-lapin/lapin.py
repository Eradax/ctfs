from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes

while True:
	pin = int(input(">>> PIN code (4 digits): "))
	if 0 < pin < 9999:
		break

flag = open("flag.txt", "rb").read()
k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
aes = AES.new(k, AES.MODE_GCM)
c, tag = aes.encrypt_and_digest(flag)

enc = aes.nonce + c + tag
print(enc.hex())
