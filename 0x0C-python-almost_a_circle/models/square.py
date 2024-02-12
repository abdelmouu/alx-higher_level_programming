#!/usr/bin/python3
"""
this is an inheritance of Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Args:
        * size: size of the square
        * x: position
        * y: position
        * id: id of square
    """
    elem = 0

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new Square instance. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Gets the size of the square."""
        return (self.width)

    @size.setter
    def size(self, size):
        """ Sets the size of the square, updating width and height."""
        self.width = size
        self.height = size

    def __str__(self):
        """ Returns a string representation of the Square."""
        args = [self.id, self.x, self.y, self.width]
        return ("[Square] ({}) {}/{} - {}".format(*args))

    def update(self, *args, **kwargs):
        """ Updates the instance attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments."""
        lista = ['id', 'width', 'x', 'y']
        if args is not None and len(args) != 0:
            cont = 0
            for arg in args:
                if cont < 4:
                    setattr(self, lista[cont], arg)
                    cont += 1
        else:
            for key, value in kwargs.items():
                for elem in lista:
                    if elem == key:
                        setattr(self, key, value)
                if key == 'size':
                    setattr(self, 'width', value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.
        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        new = {}
        value = 0
        lista = ['id', 'size', 'x', 'y']
        for cont in range(len(lista)):
            if lista[cont] == 'size':
                value = getattr(self, 'width')
            else:
                value = getattr(self, lista[cont])
            new[lista[cont]] = value
        return (new)
