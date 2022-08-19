#!/usr/bin/python3
"""Post Request and get the id & name of the result"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        data_to_send = {'q': argv[1]}
    else:
        data_to_send = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data_to_send)
    try:
        content = r.json()
        if len(content) > 0:
            print("[{}] {}".format(content['id'], content['name']))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
