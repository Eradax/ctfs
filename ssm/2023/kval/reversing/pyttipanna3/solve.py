#!/usr/bin/env python3
import re

seed: int = 0
def randint(top: int) -> int:
    global seed
    
    # print(f"{seed = }")

    seed = seed * 0xE621 + 0xabcd

    return seed % top

def deshuffle(lst: str) -> str:
    plc: list[str | None] = [None for _ in range(len(lst))]
    res: str = ""

    for i in range(len(lst)):
        n_spots_left: int = len(lst) - i
        chosen_spot: int = randint(n_spots_left)

        count = 0
        for j in range(len(plc)):
            if plc[j] == None:
                if count == chosen_spot:
                    plc[j] = lst[i]
                    res += lst[j]
                    break
                else:
                    count += 1

    return res

with open("./given.txt") as f:
    _ = f.readline()
    shuffled_flag = f.readline().strip()

for s in range(800_000):
    seed = s
    deshuffled_flag: str = deshuffle(shuffled_flag)

    r = re.match(r"SSM{[-!\w]+}", deshuffled_flag)
    if r and len(r.group(0)) == len(shuffled_flag):
        print(r.group(0))
        break
