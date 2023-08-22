#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda x: [y ** 2 for y in x], matrix))
    return new_matrix
