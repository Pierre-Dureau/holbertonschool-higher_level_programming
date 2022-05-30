#!/usr/bin/python3
def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited from the specified class"""
    return issubclass(type(obj), a_class)
