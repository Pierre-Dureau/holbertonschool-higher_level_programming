#!/usr/bin/python3
"""
    This is the say_my_name Module
    This module supplies one function say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """Print the first and last name
        an error will occured if there are not string"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
