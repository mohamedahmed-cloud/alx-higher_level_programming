#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix = matrix or [[]]

    for i in matrix:
        print(*i)
