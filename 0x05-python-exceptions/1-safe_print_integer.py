#!/usr/bin/python3
def safe_print_integer(value):
    check = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        check = False
    return check
