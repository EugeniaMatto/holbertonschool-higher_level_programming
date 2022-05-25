#!/usr/bin/python3
"""
Module to task 2
"""


def matrix_divided(matrix, div):
    """
    task 2, divides all elements of a matrix.
    """
    if (type(div) != float and type(div) != int):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    le = matrix[0]
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")
        if i != 0 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix" +
                            " must have the same size")
        for j in matrix[i]:
            if (type(j) != float and type(j) != int):
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")
    new = matrix.copy()
    return list(map(lambda x:
                    list(map(lambda z: round((z / div), 2), x)), matrix))
