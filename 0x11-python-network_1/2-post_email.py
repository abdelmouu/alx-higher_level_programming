#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the response body
"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({
                        'email': argv[2]
                    }).encode('ascii')
    req = Request(argv[1], data)

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
