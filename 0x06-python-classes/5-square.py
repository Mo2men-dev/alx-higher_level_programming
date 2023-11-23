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
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        my_print: Prints the square pattern using '#'.
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
        self.size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Parameters:
            None

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Parameters:
            None

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square pattern using '#'.

        Parameters:
            None

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
