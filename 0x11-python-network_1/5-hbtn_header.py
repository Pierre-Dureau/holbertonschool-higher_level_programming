#!/usr/bin/python3
"""Display header information"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    r = requests.post(url)
    print(r.headers['X-Request-Id'])
