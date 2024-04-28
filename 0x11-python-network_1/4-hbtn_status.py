#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
with `requests` module
"""
if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
