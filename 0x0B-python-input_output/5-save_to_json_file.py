#!/usr/bin/python3

"""Module for save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be written to file
        filename: file to write object to

    Returns:
        None"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
