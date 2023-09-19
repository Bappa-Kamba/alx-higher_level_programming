#!/usr/bin/python3
"""
Module contains class Rectangle

Inherits from Base;
Inits superclass' id
Contains private width, height, x, y
"""
from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Methods:
    __init__(self, width, height, x=0, y=0, id=None)
    area(self)
    getters:
        width(self) -> __width
        height(self) -> __height
        x(self) -> __x
        y(self) -> __y
    setters:
        width(self, value)
        height(self, value)
        x(self, value)
        y(self, value)

    Attributes:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instance attributes with the values.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter method for width
        """
        return self.__width

    @property
    def height(self):
        """
        getter method for height
        """
        return self.__height

    @property
    def x(self):
        """
        getter method for x
        """
        return self.__x

    @property
    def y(self):
        """
        getter method for y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        setter method for width
        validates `value` before assigning
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter method for height
        validates `value` before assigning
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        setter method for x
        validates `value` before assigning
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        setter method for y
        validates `value` before assigning
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area value of the `Rectangle` instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the `Rectangle` instance with the character `#`,
        takes into account the values of `x` and `y` and add spaces before
        the `#`s both horizontally and vertically respectively.

        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """
        returns rectangle in the format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return f"[Rectangle] " + \
            f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute:
            1st argument should be the `id` attribute,
            2nd argument should be the `width` attribute,
            3rd argument should be the `height` attribute,
            4th argument should be the `x`attribute,
            5th argument should be the `y` attribute,
        if `*args` is present and not empty, skip `**kwargs`.
        """
        if args and not None:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of a `Rectangle`.
        This dictionary must contain:
            `id`, `width`, `height`, `x` and `y`.
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y

        return dict
