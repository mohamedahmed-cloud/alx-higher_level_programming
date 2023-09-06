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
    return np.matmul(m_a, m_b)
