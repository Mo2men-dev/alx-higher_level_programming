#!/usr/bin/python3
"""object_to_json module"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure

    Args:
        obj: object to be serialized

    Returns:
        dictionary description with simple data structure
    """
    return obj.__dict__
