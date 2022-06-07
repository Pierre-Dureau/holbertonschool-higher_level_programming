#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return an unofficial string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Get the size"""
        return self.width

    @size.setter
    def size(self, size):
        """Set the size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update arguments"""
        if len(args) != 0:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Get the dictionary representation"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
