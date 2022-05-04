#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary

    new_dict = a_dictionary.copy()

    for i in new_dict:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
