#!/usr/bin/env python3
init_seed = 123_456
flag: str = "SSM{yay}"
# flag: str = "aM{ySS}y"

assert init_seed < 800_000

seed: int = init_seed
def randint(top: int) -> int:
    global seed
    
    # print(f"{seed = }")

    seed = seed * 0xE621 + 0xabcd

    return seed % top

def shuffle(lst: list[str]) -> list[str]:
    out: list[str | None] = [None for _ in range(len(lst))]

    for i in range(len(lst)):
        n_spots_left = len(lst) - i
        chosen_spot = randint(n_spots_left)

        count = 0
        for j in range(len(out)):
            if out[j] == None:
                if count == chosen_spot:
                    out[j] = lst[i]
                    break
                else:
                    count += 1

    return [str(i) for i in out]



shuffled_flag: str = "".join(shuffle(list(flag)))
print(shuffled_flag)

