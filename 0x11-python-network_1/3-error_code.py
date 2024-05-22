#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
