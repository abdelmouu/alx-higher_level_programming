#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
