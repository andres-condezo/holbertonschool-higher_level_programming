#!/usr/bin/python3
"""A module for build Squares"""


class Square:
    '''A Square builder class with its atributes'''

    def __init__(self, size):
        '''
        Build a squares with a private instance atribute
        Args:
        size (int): The size of the square
        '''
        self.__size = size
