#!/usr/bin/python3
"""
Defines a class-checking function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if the object is exact an instance of the  class a_class, otherwise return false"""
    return (type(obj) == a_class)
