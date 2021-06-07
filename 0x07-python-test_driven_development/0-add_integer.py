#!/usr/bin/python3
'''a funtion module'''


def add_integer(a, b=98):
    '''
    add_integer: funtion add two integers or floats

    Arg:
        a (int, float): First parameter
        b (int, float): Second parameter

    return a + b

    '''

    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')

    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
