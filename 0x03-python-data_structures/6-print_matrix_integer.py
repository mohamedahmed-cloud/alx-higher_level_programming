#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix = matrix or [[]]

    for i in matrix:
        print(" ".join(map(str, i)).format(*i))
