#!/usr/bin/python3
"""object to JSON string conversion module"""


import json


def to_json_string(my_obj):
    """
    converts object to JSON string

    Args:
        my_obj: object to be converted

    Returns:
        JSON string
    """
    return json.dumps(my_obj)
