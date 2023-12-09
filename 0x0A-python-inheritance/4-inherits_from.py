#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited from"""
    return issubclass(obj, a_class) and type(obj) != a_class
