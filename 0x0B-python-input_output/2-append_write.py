#!/usr/bin/python3
"""
A function that appends a text into a file.
"""


def append_write(filename="", text=""):
    """ A function that appends a text into a file

    Args:
        filename (str): [the file which the string will be appended].
        text (str): [the text that will be appended in the file].
    """
    appended = 0
    with open(filename, mode="a", encoding="utf-8") as my_file:
        appended = my_file.write(text)

    return appended
