#!/usr/bin/python3
"""
Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
