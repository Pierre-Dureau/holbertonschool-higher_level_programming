#!/usr/bin/python3
"""Handle error"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as rep:
            the_page = rep.read()
            print(the_page.decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
