#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len = len(argv)
    sum = 0
    if len != 1:
        for i in range(1, len):
            sum += int(argv[i])

    print(sum)
