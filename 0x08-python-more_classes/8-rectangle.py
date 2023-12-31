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
    print_symbol = "#"

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
        string = ""

        if (self.__width == 0 or self.__height == 0):
            return (string)

        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if (i != self.__height - 1):
                string += "\n"

        return (string)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")

        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area

        Parameters:
            rect_1: first rectangle
            rect_2: second rectangle

        Returns:
            The biggest rectangle based on the area
        """

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)
