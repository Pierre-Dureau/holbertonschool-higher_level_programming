#!/usr/bin.python3
"""
    This is the lazy_matrix_mul Module
    This module supplies one function lazy_matrix_mul()
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrix
        or an error if arguments are not int or float
        if each row of the matrix are not the same size"""

    try:
        return (np.dot(m_a, m_b))
    except Exception as e:
        print(e)
