#!/usr/bin/python3
"""Module Student"""


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs:
            dic = {}
            for a in self.__dict__:
                if a in attrs:
                    dic[a] = self.__dict__[a]
            return dic
        else:
            return self.__dict__
