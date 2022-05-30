#!/usr/bin/python3
def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it’s possible"""
    try:
        setattr(obj, attr, value)
    except Exception:
        raise TypeError("can't add new attribute")
