#!/usr/bin/python3
"""
Defines a class and inherited class-checking function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance or inherited 
    instance of a_class, otherwise return false"""
    if isinstance(obj, a_class):
        return True
    return False
