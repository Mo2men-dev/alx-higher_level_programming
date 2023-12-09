#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
