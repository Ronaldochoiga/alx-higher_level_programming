#!/usr/bin/python3
"""
    the script sends a request to url and returns the response x-request-id
"""

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print('{}'.format(resp.info().get('X-Request-id')))
