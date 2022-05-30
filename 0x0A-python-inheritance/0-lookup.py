#!/usr/bin/python3
"""Module lookup"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return list(dir(obj))
