#!/usr/bin/python3
import json
"""
A function that creates an Object from a 'JSON file'
"""


def load_from_json_file(filename):
    """ A function that creates an Object from a 'JSON file'

    Args:
        filename ([json]): [A json file to create the python object]
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.load(filename)