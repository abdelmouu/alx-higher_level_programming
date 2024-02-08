#!/usr/bin/python3
"""
This module defines a text file-reading function
"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
