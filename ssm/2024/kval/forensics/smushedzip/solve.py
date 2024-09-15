#!/usr/bin/env python3
from itertools import permutations
from os import mkdir
from shutil import rmtree, unpack_archive

try:
    rmtree("./tests")
except:
    pass
mkdir("./tests")

parts: list[bytes]
parts = []

for i in range(1, 6):
    with open(f"part{i}", "rb") as f:
        parts.append(f.read())

for perm in permutations(parts):
    with open("./tests/test.zip", "wb") as f:
        f.write(b''.join(perm))

    try:
        unpack_archive("./tests/test.zip", "./tests/res")
    except:
        try:
            rmtree("./tests/res")
        except:
            pass
    else:
        print("-------- Found ---------")
        exit()

rmtree("./tests")

