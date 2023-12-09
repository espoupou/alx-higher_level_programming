#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    try:
        r = requests.get('http://127.0.0.1:5050/status')
    except Exception as e:
        r = requests.get('https://intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n'
        '\t- content: {}'.format(type(t), t))
