#!/usr/bin/python3
"""student class module"""


class Student:
    """
    student class

    Attributes:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of the student

    Methods:
        to_json: returns the dictionary representation of the student instance
    """
    def __init__(self, first_name, last_name, age):
        """initializes the student instance

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
