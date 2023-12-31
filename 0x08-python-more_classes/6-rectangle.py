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

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ("")
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")

        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
