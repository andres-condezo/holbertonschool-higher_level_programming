#!/usr/bin/python3
"""Reactangle module"""


class Rectangle:
    """A class to create rectangle objects"""

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        return 2 * (self.width + self.height)
