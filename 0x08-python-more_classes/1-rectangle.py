#!/usr/bin/python3
"""
Module that defines a rectangle

Class:
    Rectangle: Defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle

    Attributes:
        width: width of the rectangle
        height: height of the rectangle

    Methods:
        __init__: Initializes a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
