#!/usr/bin/python3
"""
    this uses your username and password as in the github api
    and in the return  a user id is diplayed on the screen
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    r_json = r.json()
    if r_json == {}:
        print("None")
    else:
        print("{}".format(r_json.get('id')))
