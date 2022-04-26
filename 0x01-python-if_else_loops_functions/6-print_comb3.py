#!/usr/bin/python3
for i in range(1, 10):
    print("{:02d}, ".format(i), end="")
for i in range(10, 100):
    if i % 10 > i / 10:
        if i != 89:
            print("{:d}, ".format(i), end="")
        else:
            print("89")
