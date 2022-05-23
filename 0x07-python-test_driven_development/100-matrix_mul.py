#!/usr/bin/python3
"""
    This is the matrix_mul Module
    This module supplies one function matrix_mul()
"""


def matrix_mul(m_a, m_b):
    """Return the multiplication of two matrix
        or an error if arguments are not int or float
        or if each row of the matrix are not the same size"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_b) != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    tab = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                tab[i][j] += m_a[i][k] * m_b[k][j]

    return tab
