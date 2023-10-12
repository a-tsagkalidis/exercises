import sys


def check_usage(plaintext: list) -> None:
    """
    Checks the validity of the command line argument
    that is beeing passed by the user
    """
    if len(plaintext) != 2:
        print(f"Usage: {plaintext[0]} key")
        exit()

    if not plaintext[1].isdigit():
        print(f"Usage: {plaintext[0]} key")
        exit()


def rotate(char: str, key: int) -> str:
    """
    Returns a shifted value of a letter according to the
    key value. E.g. 'a' becomes 'b' in case of key=1, or
    'a' becomes 'n' in case of key=13. If the character isn't
    a letter, it is returned as it is.
    """
    if key > 26:
        key -= 26 * (key // 26)
    if ord(char) + key > 90 and char.isupper():
        key -= 26
    if ord(char) + key > 122 and char.islower():
        key -= 26
    if char.isalpha():
        return chr(ord(char) + key)
    else:
        return chr(ord(char))


if __name__ == "__main__":
    check_usage(sys.argv)
    for character in input("plaintext: "):
        print(rotate(character, int(sys.argv[1])), end="")
