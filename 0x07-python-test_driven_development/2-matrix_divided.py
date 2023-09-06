#!/usr/bin/python3
"""
matrix_divided - divide 2 d array on div number.
"""


def matrix_divided(matrix=None, div=None):
    """
    matrix_divided: divide 2D array on div number.

    args:
        matrix: 2D array Divide element on it.
        div: number.

    return:
        return the new matrix without changine old one.
    """
    if matrix is None:
        return None
    elif div is None:
        return matrix

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    last = len(matrix[0])
    for i in matrix:
        if len(i) != last:
            raise TypeError("Each row of the \
matrix must have the same size")

    # Divide by Zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    new_matrix = [row[:] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix
