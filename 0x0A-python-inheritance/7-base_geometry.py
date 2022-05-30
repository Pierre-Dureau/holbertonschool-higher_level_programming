#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemente")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
