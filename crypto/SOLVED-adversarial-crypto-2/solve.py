"""
The problem hints that there is something wrong with how they generate `n`.

Looking at `n` we notice that is has very few bits that are on so we can use
polynomials to factor it.
"""

from sage.all import ZZ, PolynomialRing

def solve(c: int, n: int, e: int) -> str:
    R = PolynomialRing(ZZ, 'x')
    x = R.gen()
    poly = sum(int(b) * x**i for i, b in enumerate(bin(n)[2:][::-1]))

    p_poly, q_poly = poly.factor()
    p: int = p_poly[0](x=2)
    q: int = q_poly[0](x=2)

    d = pow(e, -1, (p-1)*(q-1))

    m_int: int = pow(c, d, n)
    m_bytes: bytes = m_int.to_bytes(128, "big")
    start: int = m_bytes.index(b'FCSC')
    m_bytes = m_bytes[start:]
    m_str = m_bytes.decode()

    return m_str


def main() -> None:
    with open("./output.txt", "r") as f:
        c: int = int(f.readline().strip()[4:], 16)
        n: int = int(f.readline().strip()[4:])
        e: int = int(f.readline().strip()[4:])

    decrypted: str = solve(c, n, e)

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
