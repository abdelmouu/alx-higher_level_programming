#!/usr/bin/python3
""" a module that represente a class Square """


class Square:
    """ a class Square that defines a square. """

    size: def __init__(self, size=0):
    """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        
        if not isinstance(size, int):
            raise TypeError(size must be an integer)
        if size < 0:
            raise ValueError(size must be >= 0)

        self.__size = size
