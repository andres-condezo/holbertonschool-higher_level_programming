#!/usr/bin/python3
"""Square module: for build Squares"""


class Square:
    '''
    Square: A Square builder class that define a square by:
        property size
        property size setter
        Instantiation with optional size
        Public instance method: def area
        Public instance method: def my_print
    '''

    def __init__(self, size=0):
        '''
        Initialize a squares with a size private instance atribute

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

    def my_print(self):
        '''my_print: Prints in stdout the square with the character #'''

        if self.size == 0:
            print()

        for row in range(self.size):
            for column in range(self.size):
                if column == self.size - 1:
                    print('#')
                else:
                    print('#', end='')
