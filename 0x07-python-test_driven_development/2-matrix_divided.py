#!/usr/bin/python3
'''A module defining the funtion matrix_divided'''


def matrix_divided(matrix, div):
    '''
    matrix_divided: A function that divides all elements of a matrix.

    Args:
        matrix (int, float): a list of lists of integers or floats.
        div (int, float): A number to be the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix it's not of the same size
        TypeError: If div it's not a number (integer or float)
        ZeroDivisionError: If div it's equal to 0

    Returns:
        A new matrix.

    '''

    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if not all(isinstance(el, (int, float) for el in matrix))

    if not isinstance(div, (int, float)):
        raise TypeError(
            'div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')
