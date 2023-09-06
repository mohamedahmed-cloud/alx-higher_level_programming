#!/usr/bin/python3
"""
    0-add_integer: add_integer()
"""


def add_integer(a, b=98):
    """
        add_integer return sum of two integer

        args:
            a : first number
            b : second number
        return:
            return sum of two number.
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")

    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    ans = a + b
    if ans == float("inf") or ans == -float("inf"):
        return 98

    return int(a) + int(b)
