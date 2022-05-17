#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize"""
        self.size = size
        self.position = position

    def area(self):
        """Area of the square"""
        return self.__size**2

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""
        if type(value) is not tuple and len(value) != 2 \
            and type(value[0]) is not int and type(value[1]) is not int \
                and value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for s in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for diez in range(self.__size):
                    print("#", end="")
                print()
