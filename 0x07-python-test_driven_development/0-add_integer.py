#!/usr/bin/python3
'''A module defining the funtion add_integer'''


def add_integer(a, b=98):
    '''
    add_integer: funtion to add two integers or floats

    Args:
        a (int, float): First parameter
        b (int, float): Second parameter

    Returns:
        a + b

    '''

    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')

    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
