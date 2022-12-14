#!/usr/bin/python3
"""
Module 3-Rectangle
Defines class Rectangle with private attributes

"""


class Rectangle:
    """
    Class Rectangle definition

    Arg:
        width: width of a Rectangle

    Function:
        __init__(self, width)

    """

    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle

        Attribute:
            width

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter

        Returns width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value (int): sets width to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter

        Returns height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value (int): sets height to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates area of rectangle

        Returns: area

        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates perimeter of rectangle

        Returns:
            - perimeter
            - else 0 if width or height is 0

        """
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.width + self.height)

        return perimeter

    def __str__(self):
        """
        Prints square as #'s

        """
        if self.width == 0 or self.height == 0:
            return ""
        str = "\n".join(["#" * self.__width for rows in range(self.__height)])

        return str
