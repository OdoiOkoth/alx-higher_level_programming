#!/usr/bin/python3
"""print tyhe alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
