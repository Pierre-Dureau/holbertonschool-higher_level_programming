#!/usr/bin/python3
"""
    This is the text_indentation Module
    This module supplies one function text_indentation()
"""


def text_indentation(text):
    """Print the text with 2 new lines after specific char
        an error occured if the text is not a string"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    for c in text:
        if c == ' ' and count == 0:
            continue
        if c != '?' and c != '.' and c != ':':
            if count != 0 or c != ' ':
                print(c, end="")
        else:
            print(c, end="")
            print()
            print()
            count = 0
            continue
        count += 1
