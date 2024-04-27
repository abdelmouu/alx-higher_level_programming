#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the response body
"""
import urllib.request
import urllib.parse
import sys


if len(sys.argv) > 2:
    url = sys.argv[1]
    email = sys.argv[2]
else:
    print('Usage: {} <url> <email>'.format(sys.argv[0]))
    sys.exit(1)

params = urllib.parse.urlencode({'email': email})
url_with_params = '{}?{}'.format(url, params)

with urllib.request.urlopen(url_with_params, data=None) as response:
    body = response.read()

print(body.decode('utf-8'))
