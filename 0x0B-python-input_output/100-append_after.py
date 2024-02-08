#!/usr/bin/python3
"""
This module defines a text file insertion function
"""


def append_after(filename="", search_string="", new_string=""):
"""Inserts text after each line containing a given string in a file"""
    result = ""
    with open(filename) as fd:
        for line in fd:
            result = result + line
            if search_string in line:
                result = result + new_string

    with open(filename, "w") as fd:
        fd.write(result)
