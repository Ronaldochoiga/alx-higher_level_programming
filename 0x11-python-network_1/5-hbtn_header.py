#!/usr/bin/python3
"""
    the script takes url, sends request and returns the X-Request-id from the response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers['X-Request-Id']))
