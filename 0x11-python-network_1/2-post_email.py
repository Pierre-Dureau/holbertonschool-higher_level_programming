#!/usr/bin/python3
"""Post Request with email in parameter"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == '__main__':
    value = {'email': argv[2]}
    data = urlencode(value).encode()
    req = Request(argv[1], data)
    with urlopen(req) as rep:
        the_page = rep.read()
        print(the_page.decode('utf-8'))
