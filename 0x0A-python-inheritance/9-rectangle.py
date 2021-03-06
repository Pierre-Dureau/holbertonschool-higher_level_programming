#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry():
    """BaseGeometry class"""

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return Area"""
        return self.__width * self.__height

    def __str__(self):
        """Print size"""
        return f'[Rectangle] {self.__width}/{self.__height}'
