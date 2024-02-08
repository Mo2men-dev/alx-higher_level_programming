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
        reload_from_json: replaces all attributes of the student instance
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

    def to_json(self, attrs=None):
        """returns the dictionary representation of the student instance

        Args:
            attrs (list): list of strings

        Returns:
            dict: dictionary representation of the student instance
        """
        dic = {}
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    dic[attr] = self.__dict__[attr]

        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the student instance

        Args:
            json (dict): dictionary representation of the student instance

        Returns:
            None
        """
        for key, value in json.items():
            if key in self.__dict__:
                setattr(self, key, value)
