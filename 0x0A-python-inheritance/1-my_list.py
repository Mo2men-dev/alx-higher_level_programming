#!/usr/bin/python3
"""Module to create a class MyList that inherits from list"""


class MyList(list):
    """
    Class MyList that inherits from list
    """
    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        print(sorted(self))
