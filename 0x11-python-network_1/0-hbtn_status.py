#!/usr/bin/python3
""" fetch https://intranet.hbtn.io/status """
from urllib.request import urlopen, Request


if __name__ == "__main__":
    req = Request(
        url='https://alx-intranet.hbtn.io/status',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
