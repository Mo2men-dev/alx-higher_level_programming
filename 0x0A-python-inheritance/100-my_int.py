#!/usr/bin/python3
"""
Module that defines a class MyInt that inherits from int
and reverses the operators == and !=
"""


class MyInt(int):
    """Class that inherits from int and reverses == and != operators"""

    def __init__(self, value):
        """Initializes the class"""
        self.value = value

    def __eq__(self, value):
        """Reverses == operator"""
        return self.value != value

    def __ne__(self, value):
        """Reverses != operator"""
        return self.value == value
