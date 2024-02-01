#!/usr/bin/python3
"""This module contains a function that adds 2 integers"""


def add_integer(a, b=98):
    """This function adds 2 integers
    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        int: the sum of a and b
    Raises:
        TypeError: if a or b are not integers or floats
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
