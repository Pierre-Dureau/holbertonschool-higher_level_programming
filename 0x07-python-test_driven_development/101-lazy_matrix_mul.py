#!/usr/bin/python3
"""
    This is the lazy_matrix_mul Module
    This module supplies one function lazy_matrix_mul()
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrix
        or an error if arguments are not int or float
        or if each row of the matrix are not the same size"""

    return (np.matmul(m_a, m_b))
