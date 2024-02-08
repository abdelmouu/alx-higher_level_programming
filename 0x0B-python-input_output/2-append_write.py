#!/usr/bin/python3
"""
This module defines a file-appending function.
"""


def read_lines(filename="", nb_lines=0):
    """Appends a string to the end of a UTF8 text file"""
    with open(filename) as fd:

        if nb_lines <= 0:
            for line in fd:
                print(line, end="")
        else:
            for i in range(nb_lines):
                print(fd.readline(), end="")
