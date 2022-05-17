#!/usr/bin/python3
"""Module MagicClass"""


import math


class MagicClass:
    """define a Magic Class object"""

    def __init__(self, radius):
        """Initialize radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Calcul area of a circle with a radius"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calcul circumference of a circle with a radius"""
        return 2 * math.pi * self.__radius
