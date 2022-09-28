#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
"""
def class_to_json(obj):
    """ A function that returns the dictionary description with simple data structure

    Args:
        obj ([object]): [serializable instance of a class]
    
    Returns: [dict]: [attributes of the given instance]
    """
    return vars(obj)