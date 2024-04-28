#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys import argv
import requests

if __name__ == "__main__":
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)

    print(req.text)
