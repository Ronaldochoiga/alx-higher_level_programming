#!/usr/bin/python3
"""
uses the git hub api in help of username and password to show the different commits from a n account
"""
import requests
from sys import argv


if __name__ == "__main__":
    i = 0
    try:
        res = requests.get("https://api.github.com/repos/{}/{}/commits".
                           format(argv[2], argv[1])).json()
        for commit in res:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            i += 1
            print("{}: {}".format(sha, author))
            if i == 10:
                break
    except:
        print("Not a valid PARAMETER")
