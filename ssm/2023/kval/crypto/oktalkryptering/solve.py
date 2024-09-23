#!/usr/bin/env python3
import itertools
import re

def decrypt(key, data):
	transformedData = []
	for char in data:
		transformedData.append(key.index(char))


	binstr = ""
	for char in transformedData:
		binstr += bin(char)[2:].rjust(3, '0')

	binstr = binstr.ljust(len(binstr) + (-len(binstr)%8), '0')

	out = []
	for i in range(0, len(binstr), 8):
		num = int(binstr[i:i+8], 2)
		out.append(num ^ 0)

	return bytes(out)

with open("./out.txt", "r") as f:
    out = f.readline().strip()

for idx, perm in enumerate(itertools.permutations("1234567890")):
    perm = ''.join(perm)

    # if idx % 10_000 == 0:
    #    print(f"{perm = }")

    res: str = ""
    try:
        res = decrypt(perm, out).decode()
    except:
        ...
    m = re.match(r"SSM{[\w\d]+}", res)
    if m:
        print(m.group(0))
        break
