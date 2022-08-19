#!/usr/bin/python3
"""Display header information"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == '__main__':
    req = Request(argv[1])
    with urlopen(req) as response:
        print(response.info()['X-Request-Id'])
