#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes.

Module-level documentation goes here.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__: Init the Square object with optional size and position param
        area: Calculates and returns the area of the square
        size (property): Getter and setter methods for the size attribute
        position (prop): Getter and setter method for the position attribute
        my_print: Prints the square pattern using '#' with the position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square object.

        Parameters:
            size (int, optional): The size of the square. Default 0.
            position (tuple, optional): position of the square Default (0, 0)

        Raises:
            TypeError: size not int or position is not a tuple of 2 +ve int
            ValueError: size less than 0 or a coord in position is less than 0

        Returns:
            None
        """
        self.size = size
        self.position = position

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
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """
        Prints the square pattern using '#' with the specified position.

        Parameters:
            None

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Parameters:
            None

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
            ValueError: If coordinate in the provided value is less than 0.

        Returns:
            None
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
