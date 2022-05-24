#!/usr/bin/python3
def magic_string(count=[]):
    count += [1]
    return ("Holberton, " * len(count))[:-2]
