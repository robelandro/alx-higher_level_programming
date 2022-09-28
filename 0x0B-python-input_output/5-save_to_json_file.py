#!/usr/bin/python3
import json
"""
A function that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ A function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj ([dict]): [python object to create the json file]
        filename ([json]): [json file which will be created]
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, filename)