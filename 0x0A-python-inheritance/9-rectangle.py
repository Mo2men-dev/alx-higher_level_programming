#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """__init__ method that initializes width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method that returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ method that returns string representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
