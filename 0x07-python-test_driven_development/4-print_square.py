#!/usr/bin/python3
"""This is the hello module."""

def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): size of the square.

    Returns:
        Nothing.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)
