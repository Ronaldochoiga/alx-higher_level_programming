#!/usr/bin/python3
""" The scrpt uses utf-8, email and url to POST
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("{}".format(html.decode('utf-8')))
