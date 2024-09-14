"""
In this problem we are tasked with craking standard RSA, we know the public key
i.e. (`n, e`) and the encrypted value `c`.

The problem that makes this possible is that `n` is too small (~10^60)
"""

import requests
def solve(c: int, n: int, e: int) -> str:
    ENDPOINT: str = "http://factordb.com/api"
    response = requests.get(ENDPOINT, params={"query": str(n)})
    factors: list[list[int]] = response.json().get("factors")
    
    p: int = int(factors[0][0])
    q: int = int(factors[1][0])

    d: int = pow(e, -1, (p-1)*(q-1))

    m: int = pow(c, d, n)

    return str(m)

def main() -> None:
    with open("./encrypted.txt", "r") as f:
        c: int = int(f.readline()[4:-1])
        n: int = int(f.readline()[4:-1])
        e: int = int(f.readline()[4:-1])

    decrypted: str = f"FCSC{{{solve(c, n, e)}}}"

    print("The decrypted string is:")
    print(decrypted)


if __name__ == "__main__":
    main()
