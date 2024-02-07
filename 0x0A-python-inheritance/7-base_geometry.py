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

    def integer_validator(self, name, value):
        """validates a value as an integer"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
