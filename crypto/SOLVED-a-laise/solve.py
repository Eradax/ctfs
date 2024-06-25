#!/usr/bin/env python3
"""
This is a vigenere cipher, we know the key to be `FCSC` and the encrypted text is located in "./encrypted.txt"
"""
# This assumes the english alphabet
ALPHABET_LEN: int = 26
ALPHABET_FIRST_CHAR: str = 'a'

def cesar_shift(char: str, length: int):
    isUpper: bool = char.isupper

    norm_int: int = ord(char.lower()) - ord(ALPHABET_FIRST_CHAR)
    shifted_int: int = (norm_int + length) % ALPHABET_LEN

    shifted_char: str = chr(shifted_int + ord(ALPHABET_FIRST_CHAR))
    if isUpper:
        shifted_char = shifted_char.upper()

    return shifted_char

def solve(key: str, encrypted: str):
    n: int = len(encrypted)
    m: int = len(key)

    # pad key to be the length of encrypted
    key *= (n+m-1)//m
    decrypted: str = ""
    
    c_i: str
    i: int = 0
    for c_i in encrypted:
        if not c_i.isalpha():
            decrypted += c_i
            continue
        decrypted += cesar_shift(c_i, ord(ALPHABET_FIRST_CHAR) - ord(key[i].lower()))
        i += 1

    return decrypted

def main():
    with open("./encrypted.txt", "r") as f:
        encrypted: str = f.read()

    key: str = "FCSC"

    decrypted: str = solve(key, encrypted)

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
