#!/usr/bin/python3


"""Module for load_from_json_file"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”

    Args:
        filename: name of the file

    Returns:
        Object created from the JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
