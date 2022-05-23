#!/usr/bin/python3
"""
    This is the matrix_divided Module
    This module supplies one function matrix_divided()
"""


def matrix_divided(matrix, div):
    """Return the matrix divided by div in a new matrix
        or an error if arguments are not int or float
        if each row of the matrix are not the same size
        id div is not a number and != 0"""

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        + "of integers/floats")

    if all(isinstance(ele, list) for ele in matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists) "
                        + "of integers/floats")

    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        + "of integers/floats")

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                + "of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda x:
                list(map(lambda y: round(y / div, 2), x)), matrix))
