#!/usr/bin/python3
"""print 10 last commits of a repo"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    r = r.json()
    i = 0
    for commit in r:
        print("{}: {}".format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
        i += 1
        if i == 10:
            break
