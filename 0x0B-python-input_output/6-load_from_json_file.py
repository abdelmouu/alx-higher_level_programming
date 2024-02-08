#!/usr/bin/python3
"""
This module defines a JSON file-reading function
"""


def load_from_json_file(filename):
	"""Creates a Python object from a given JSON file"""
    import json
    with open(filename) as fd:
        obj = fd.read()
    return(json.loads(obj))
