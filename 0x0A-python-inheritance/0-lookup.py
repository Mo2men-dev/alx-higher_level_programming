#!/usr/bin/python3
"""
This is a module that has a function that returns
an array of all atr and methods of an object
"""


def lookup(obj):
    """
    This function that returns list of atrs and methods of an object

    Args:
        obj (class): object to check

    Returns:
        list: list of atrs and methods
    """
    return [atr for atr in dir(obj)]
