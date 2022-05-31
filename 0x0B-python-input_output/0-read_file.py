#!/usr/bin/python3
"""Module read file"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
