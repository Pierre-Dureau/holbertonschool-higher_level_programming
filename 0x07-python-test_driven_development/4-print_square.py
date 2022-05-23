#!/usr/bin/python3
"""
    This is the print_square Module
    This module supplies one function print_square()
"""


def print_square(size):
    """Print a square with a size
        an error will occuredif size is not an int > 0"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size != 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
