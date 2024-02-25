#!/usr/bin/env python

from letters import lowercase_letters, uppercase_letters, lowercase_map, uppercase_map
from utils import get_shifted_index


def encrypt(plaintext, shift=0):
    """
    Uses the Caesar cipher to encrypt a plaintext message.
    :param plaintext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    encrypted = ""

    for char in plaintext:
        if char in lowercase_letters:
            encrypted += lowercase_letters[
                get_shifted_index(char, shift, lowercase_map)
            ]
        elif char in uppercase_letters:
            encrypted += uppercase_letters[
                get_shifted_index(char, shift, uppercase_map)
            ]
        else:
            encrypted += char

    return encrypted


if __name__ == "__main__":
    plaintext = input("Message to encrypt: ")
    shift = int(input("Shift: "))
    print(encrypt(plaintext, shift))
