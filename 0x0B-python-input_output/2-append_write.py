#!/usr/bin/python3
"""Append to a file module"""


def append_write(filename="", text=""):
    """
    Append to a file module

    Args:
        filename (str): the name of the file
        text (str): the text to append to the file

    Returns:
        int: the number of characters added
    """
    with open(filename, 'a') as f:
        return f.write(text)
