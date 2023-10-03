#!/usr/bin/python3
"""
    the script displays the json after send a request to a given ip address
    this return is only made showing the id and the name of the requester
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    except ValueError:
        print("Not a valid JSON")
