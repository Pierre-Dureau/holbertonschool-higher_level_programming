#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    check = 0
    for i in a_dictionary:
        if i == key:
            a_dictionary[i] = value
            check = 1
    if check == 0:
        a_dictionary[key] = value

    return a_dictionary
