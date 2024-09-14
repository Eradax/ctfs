"""
This is standard RSA we will encrypt the value `m`
"""

def solve(m: int, n: int, e: int) -> str:
    c = pow(m, e, n)

    return str(c)

def main() -> None:
    with open("./encrypted.txt", "r") as f:
        m: int = int(f.readline()[4:-1]) 
        n: int = int(f.readline()[4:-1]) 
        e: int = int(f.readline()[4:-1])

    decrypted: str = f"FCSC{{{solve(m, n, e)}}}"

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
