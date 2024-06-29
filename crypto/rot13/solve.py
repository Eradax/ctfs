"""
The text is encrypted using the rot13 cipher which works by rotating each
character 13 steps in the alphabet. To reverse this we will be rotating -13 steps (since 13 + (-13) = 0).
"""
# This assumes the english alphabet
ALPHABET_LEN: int = 26
ALPHABET_FIRST_CHAR: str = 'a'

def cesar_shift(char: str, length: int):
    isUpper: bool = char.isupper()

    norm_int: int = ord(char.lower()) - ord(ALPHABET_FIRST_CHAR)
    shifted_int: int = (norm_int + length) % ALPHABET_LEN

    shifted_char: str = chr(shifted_int + ord(ALPHABET_FIRST_CHAR))
    if isUpper:
        shifted_char = shifted_char.upper()

    return shifted_char

def solve(enc: str, rot: int) -> str:
    decrypted: str = ""
    for char in enc:
        if not char.isalpha():
            decrypted += char
            continue
        decrypted += cesar_shift(char, -13)

    return decrypted

def main() -> None:
    with open("./encrypted.txt") as f:
        enc: str = f.read()

    decrypted: str = solve(enc, -13)

    print("The decrypted string is:")
    print(decrypted)

if __name__ == "__main__":
    main()
