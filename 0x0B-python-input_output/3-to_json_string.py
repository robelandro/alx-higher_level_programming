#!/usr/bin/python3
import json
"""
A function that returns the json representation of an object(string).
"""


def to_json_string(my_obj):
    """ A function that returns the json representation of an object(string)

    Args:
        my_obj ([string]): [the string which will be converted into a json object]

    Returns:
        [json]: [json reperesentation of the given string]
    """
    return json.dumps(my_obj)