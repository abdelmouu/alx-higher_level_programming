#!/usr/bin/python3
"""
This module defines a file-writing function.
"""


def number_of_lines(filename=""):
    """Writes a string to a UTF8 text file"""
    sum = 0
    with open(filename) as fd:
        for line in fd:
            sum += 1
    return (sum)
