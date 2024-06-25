import os
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor

FLAG = open("flag.txt", "rb").read()

key = os.urandom(4) * 20
c = strxor(FLAG, key[:len(FLAG)])
print(c.hex())
