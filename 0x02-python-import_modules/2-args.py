#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len = len(argv)
    i = 0
    if len == 1:
        print("0 arguments.")
    else:
        if len == 2:
            print("{:d} argument:".format(len - 1))
        else:
            print("{:d} arguments:".format(len - 1))
        for s in argv:
            if i != 0:
                print("{:d}: {:s}".format(i, s))
            i += 1
