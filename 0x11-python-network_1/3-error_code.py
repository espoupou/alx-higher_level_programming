#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        req = request.Request(
            url=sys.argv[1],
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
