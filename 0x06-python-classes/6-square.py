#!/usr/bin/python3
"""Square module: for build Squares"""


class Square:
    '''
    Square: A Square builder class that define a square by:
        Private instance attribute: size
        Private instance attribute: position
        Instantiation with optional size
        Public instance method: def area
        Public instance method: def my_print
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize a squares with a size private instance atribute

        Args:
            size (int): The size of the square, with a optional value of 0
            position (tuple): A tuple of 2 positive integers

        Atributes:
            size (int): The size of the square
            position (tuple): A tuple of 2 positive integers
        '''

        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''position property: Return the position atribute'''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        position setter property: Asign the value to the position atribute

        Args:
            value (tuple): A tuple of 2 positive integers

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        '''

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

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
        else:
            if self.position[1] > 0:
                print('\n' * self.position[1])

            for row in range(self.size):
                print(' ' * self.position[0], end='')

                for column in range(self.size):
                    if column == self.size - 1:
                        print('#')
                    else:
                        print('#', end='')
