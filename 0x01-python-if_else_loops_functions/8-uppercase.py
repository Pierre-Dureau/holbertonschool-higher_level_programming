#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            x = ord(c) - 32
        else:
            x = ord(c)
        y = chr(x)
        s = s + y
    print("{:s}".format(s))
