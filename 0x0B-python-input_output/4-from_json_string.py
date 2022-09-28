#!/usr/bin/python3
import json
"""
A function that returns a python data from a json file.
"""


def from_json_string(my_str):
    """ 
        A function that returns a python data from a json file.
    Args:
        my_str ([json]): [json file which will be converted to a python data.]

    Returns:
        [dict]: [A python dictionary]
    """
    return json.loads(my_str)