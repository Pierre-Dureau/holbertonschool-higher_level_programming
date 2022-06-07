#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.__width != 0 and self.__height != 0:
            s = ('\n' * self.__y) + \
                (' ' * self.__x + '#' * self.__width + '\n') * self.__height
            print(s[:-1])

    def __str__(self):
        """Return an unofficial string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update arguments"""
        if len(args) != 0:
            attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Get the dictionary representation"""
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}

