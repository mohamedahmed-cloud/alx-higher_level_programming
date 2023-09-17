#!/usr/bin/python3
"""
pascal_triangle - implementation of pascal_triangle
"""


def pascal_triangle(n):
    """
    args:
        n - the depth of pascal_triangle
    """
    res = [[1]]
    for i in range(1, n):
        curr = [1]
        for j in range(1, i):
            curr.append(res[i - 1][j - 1] + res[i - 1][j])
        curr.append(1)
        res.append(curr)
    return res
