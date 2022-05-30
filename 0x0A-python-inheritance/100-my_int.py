#!/usr/bin/python3
"""MyInt Module"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, my_int):
        """Initialize"""
        self.my_int = my_int

    def __eq__(self, other):
        """Equal"""
        if type(other) is int:
            return self.my_int != other

    def __ne__(self, other):
        """Non Equal"""
        if type(other) is int:
            return self.my_int == other
