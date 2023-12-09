#!/usr/bin/python3
"""Module that defines a square class"""


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """__init__ method that initializes size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method that returns area of Square"""
        return self.__size ** 2
