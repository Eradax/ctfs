"""
This is a standard RSA implementation except for the fact that the mixed up the
public and private key we now know both the real pk and sk so we can use
standard technices to decrypt it
"""

import json
from Crypto.Util.number import long_to_bytes
def solve(c: int, pk: tuple[int], sk: tuple[int]) -> str:
    m: int = pow(c, sk[0], sk[1])

    m_str: str = long_to_bytes(m).decode()

    return m_str

def main() -> None:
    with open("./output.txt", "r") as f:
        r: dict[str:str] = json.loads(f.read())

        e: int = 2 ** 16 +1
        d: int = int(r['e'])
        n: int = int(r['n'])
        c: int = int(r['c'])

        sk: tuple[int] = (e, n)
        pk: tuple[int] = (d, n)

    decrypted: str = solve(c, pk, sk)

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
