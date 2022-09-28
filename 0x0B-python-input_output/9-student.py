#!/usr/bin/python3
"""
A class Student that defines a student by public instance attributes
"""


class Student:
    """ A class Student that defines a student by public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A function that returns the dictionary description with simple

        Returns:
            [dict]: [attributes of the given instance]
        """
        return vars(Student)
