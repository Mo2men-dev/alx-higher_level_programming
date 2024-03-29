#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): the file to read

    Returns:
        str: the content of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
