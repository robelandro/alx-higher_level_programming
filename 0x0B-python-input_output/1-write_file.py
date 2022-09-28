#!/usr/bin/python3
"""
A function that write a text into a file.
"""


def write_file(filename="", text=""):
    """ A function that write a text into a file

    Args:
        filename (str): [the file which the string will be written].
        text (str): [the text that will be written in the file].
    """
    written = 0
    with open(filename, mode="w", encoding="utf-8") as my_file:
        written = my_file.write(text)

    return written
