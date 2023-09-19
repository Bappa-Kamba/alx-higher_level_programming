#!/usr/bin/python3
"""
Module contains class Square

Inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines class Square; inherits from class Rectangle
    Inherited Attributes:
        `id`, `width`, `height`, `x`, `y`
    Methods:
    `__init__(self, width, height, x=0, y=0, id=None)`
    `area(self)`
    getters:

    setters:

    Attributes:
        __size
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Calls the super class with `id`, `x`, `y`, `width` and `height`
        this super call will use the logic of the `__init__` of the
        Rectangle class.
        The `width` and `height` must be assigned to the value of `size`

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloaded method;

        returns Square in the format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        returns the value of `size`
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        assigns `value` to `width` and `height` (in the order)
        """
        self.width = value
        self.height = value

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
                    self.size = value
                elif i == 2:
                    self.x = value
                else:
                    self.y = value
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of a `Square`.
        This dictionary must contain:
            `id`, `size`, `x` and `y`.
        """
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y

        return dict
