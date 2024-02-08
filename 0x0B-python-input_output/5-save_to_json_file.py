#!/usr/bin/python3
"""
This module defines a JSON file-writing function
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    import json

    with open(filename, 'w') as fd:
        new = json.dumps(my_obj)
        fd.write(new)
