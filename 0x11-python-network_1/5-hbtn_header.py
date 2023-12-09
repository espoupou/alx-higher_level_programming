#!/usr/bin/python3
"""
displays the value of a variable in the response
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
