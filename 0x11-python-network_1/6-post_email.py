#!/usr/bin/python3
"""
    this script uses url and email to send a request
    with the email as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(r.text))
