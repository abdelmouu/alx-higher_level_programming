#!/usr/bin/python3
"""
Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """this class represents a base geometry"""
 
    def __init__(self):
        """init mmethod"""
        pass

    def area(self):
        """method for calculating the area of a shape."""
        raise Exception("area() is not implemented")
