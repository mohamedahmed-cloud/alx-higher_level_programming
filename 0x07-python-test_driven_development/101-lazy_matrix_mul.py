#!/usr/bin/python3
"""
lazy_matrix_mul - Implementation Matrix Multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - Implementation of matrix mul

    args:
        m_a: first matrix to multiple
        m_b: second matrix to multiple

    return:
        return the new matrix after multiplication.
    """

    # check empty array
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # check type of m_a and m_b
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    check_2D(m_a, "m_a")
    check_2D(m_b, "m_b")

    check_one_one_type(m_a, "m_a")
    check_one_one_type(m_b, "m_b")
    check_same_size(m_a, "m_a")
    check_same_size(m_b, "m_b")

    arr1_a, arr1_b = len(m_a), len(m_a[0])
    arr2_a, arr2_b = len(m_b), len(m_b[0])
    if arr1_b != arr2_a:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(arr2_b)] for i in range(arr1_a)]

    # print(np.dot(m_a, m_b))
    return np.dot(m_a, m_b)


def check_2D(curr_matrix, message):
    for i in curr_matrix:
        if type(i) is not list:
            raise TypeError(f"{message} must be a list of lists")


def check_one_one_type(curr_matrix, message):
    for i in curr_matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(f"{message}\
 should contain only integers or floats")


def check_same_size(curr_matrix, message):
    first = len(curr_matrix[0])
    for i in curr_matrix:
        if first != len(i):
            raise TypeError(f"each row of {message} must be of the same size")
