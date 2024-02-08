#!/usr/bin/python3
"""
from json_string to object
"""


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""
    import json

    return (json.loads(my_str))
