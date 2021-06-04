#!/usr/bin/python3
"""Square module: for build Squares"""


class Square:
    '''A Square builder class with its atributes'''

    def __init__(self, size=0):
        '''
        Build a squares with a private instance atribute
        Args:
        size (int): The size of the square, with a optional value of 0
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
