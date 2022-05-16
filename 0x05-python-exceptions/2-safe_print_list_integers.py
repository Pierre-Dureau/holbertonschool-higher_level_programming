#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    nonint = 0
    while count < x:
        try:
            try:
                print("{:d}".format(my_list[count]), end="")
            except:
                nonint += 1
            count += 1
        except IndexError:
            break
    print()
    return count - nonint
