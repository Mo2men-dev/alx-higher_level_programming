#!/usr/bin/python3
"""
This module defines a simple Square class.

Module-level documentation goes here.
"""


class Square:
    '''
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__: Initializes the Square object.
    '''

    def __init__(self, size):
        '''
        Initializes the Square object.

        Parameters:
            size (int): The size of the square.

        Returns:
            None
        '''
        self.__size = size
