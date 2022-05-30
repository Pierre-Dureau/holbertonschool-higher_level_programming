#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
