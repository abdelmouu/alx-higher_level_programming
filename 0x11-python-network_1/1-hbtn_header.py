#!/usr/bin/python3
"""
Displays the value of the X-Request-Id header variable from a given URL
"""
import urllib.request
import sys


if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print('Usage: {} <url>'.format(sys.argv[0]))
    sys.exit(1)

with urllib.request.urlopen(url) as response:
    header = response.getheaders()

request_id = None
for header_name, header_value in header:
    if header_name == 'X-Request-Id':
        request_id = header_value
        break

if request_id:
    print(request_id)
