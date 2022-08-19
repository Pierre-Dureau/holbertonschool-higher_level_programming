#!/usr/bin/python3
"""Post Request with email in parameter"""
import requests
from sys import argv

if __name__ == '__main__':
    data_to_send = {'email': argv[2]}
    r = requests.post(argv[1], data=data_to_send)
    print(r.text)
