#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if search < -1 or search >= len(my_list):
        return None

    new_list = []

    for i in range(0, len(my_list)):
        if i != search - 1:
            new_list.append(my_list[i])
        else:
            new_list.append(replace)

    return new_list
