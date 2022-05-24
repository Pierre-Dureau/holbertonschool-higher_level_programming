#!/usr/bin/python3
def magic_string(count=[]):
    count += [1]
    return str("Holberton, " * len(count))[:-2]
