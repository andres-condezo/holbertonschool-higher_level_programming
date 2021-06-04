#!/usr/bin/python3
"""Square module: for build Squares"""


class Square:
    '''Square: A Square builder class with its atributes'''

    def __init__(self, size=0):
        '''
        Build a squares with a private instance atribute

        Args:
            size (int): The size of the square, with a optional value of 0

        Atributes:
            size (int): The size of the square
        '''

        self.size = size

    @property
    def size(self):
        '''size setter property: Return the size atribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        size setter property: Asign the value to the size atribute

        Args:
            value (int): The size of the square

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is lower than 0
        '''

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        '''
        area: Public instance method to calculate the area of the square

        Returns:
            The current square area
        '''
        return self.__size ** 2
