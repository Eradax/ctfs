#!/usr/local/bin/python3.8

from Crypto.PublicKey import RSA

def sign(sk, m):
    mp, dq = m % sk.q, sk.d % (sk.q - 1)
    mq, dp = m % sk.p, sk.d % (sk.p - 1)

    s1 = pow(mq, dq, sk.q)
    s2 = pow(mp, dp, sk.p)
    h = (sk.u * (s1 - s2)) % sk.q
    s = (s2 + h * sk.p) % sk.n
    return s

if __name__ == "__main__":
    
    sk = RSA.generate(2048)

    flag = int.from_bytes(b'FLAG{yay}', "big")

    c = pow(flag, sk.e, sk.n)
    print(f"Encrypted flag: {c}")

    while True:
        print("What do you want me to sign?")
        try:
            m = int(input(">>> "))
            print(sign(sk, m))
        except:
            break
