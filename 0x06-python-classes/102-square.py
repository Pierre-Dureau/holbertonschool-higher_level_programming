#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize"""
        self.__size = size

    def area(self):
        """Area of the square"""
        return self.__size**2

    def __eq__(self, other):
        """Equal"""
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        """Less than"""
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Less equal"""
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
