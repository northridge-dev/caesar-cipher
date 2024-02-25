#!/usr/bin/env python

from letters import lowercase_letters, uppercase_letters, lowercase_map, uppercase_map
from utils import get_shifted_index


def decrypt(ciphertext, shift=0):
    """
    Decrypts a Caesar cipher encrypted message.
    :param ciphertext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    decrypted = ""
    for char in ciphertext:
        if char in lowercase_letters:
            decrypted += lowercase_letters[
                get_shifted_index(char, -shift, lowercase_map)
            ]
        elif char in uppercase_letters:
            decrypted += uppercase_letters[
                get_shifted_index(char, -shift, uppercase_map)
            ]
        else:
            decrypted += char
    return decrypted


if __name__ == "__main__":
    ciphertext = input("Message to decrypt: ")
    shift = int(input("Shift: "))
    print(decrypt(ciphertext, shift))
