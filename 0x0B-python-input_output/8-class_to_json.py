#!/usr/bin/python3
"""Module class to json"""


def class_to_json(obj):
    """returns the dictionary description"""
    return obj.__dict__
