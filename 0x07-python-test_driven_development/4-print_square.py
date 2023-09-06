#!/usr/bin/python3
"""
print_square - print square by #
"""


def print_square(size):
    """
        print_square: print square by type #
        args:
            size: the length of the square
        return:
            return the square with area size * size consist of #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return ""

    print((("#" * size + "\n") * size)[:-1])
