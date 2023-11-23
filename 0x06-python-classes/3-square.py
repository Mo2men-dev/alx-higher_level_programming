#!/usr/bin/python3
"""
This module defines a simple Square class.

Module-level documentation goes here.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__: Inits the Square object with an optional size parameter.
        area: Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square object.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Parameters:
            None

        Returns:
            int: The area of the square.
        """
        return self.__size**2
