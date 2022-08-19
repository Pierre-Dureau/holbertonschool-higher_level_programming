#!/usr/bin/python3
"""fetches an URL"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    print("Body response:")
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(f"\t- type: {type(the_page)}")
        print(f"\t- content: {the_page}")
        print(f'\t- utf8 content: {the_page.decode("utf8")}')
