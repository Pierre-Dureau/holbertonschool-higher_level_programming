#!/usr/bin/python3
"""Module log parsing"""
from sys import stdin


def printStatus(size, statuscode):
    """Print size of file + status codes"""
    print(f"File size: {size}")
    for key, value in statuscode.items():
        if value != 0:
            print(f"{key}: {value}")


statuscode = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
size = 0
nbline = 0

try:
    for line in stdin:
        line_split = line.split()
        if len(line_split) >= 2:
            nbline += 1
            if line_split[-2] in statuscode:
                statuscode[line_split[-2]] += 1
            size += int(line_split[-1])
        else:
            continue
        if nbline % 10 == 0:
            printStatus(size, statuscode)
    printStatus(size, statuscode)
except KeyboardInterrupt:
    printStatus(size, statuscode)
