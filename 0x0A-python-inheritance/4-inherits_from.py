#!/usr/bin/python3
"""
Defines an inherited class-checking function inherits_from
"""

def inherits_from(obj, a_class):
    """return true if the  object is an inherited instance
    of a_class Otherwise return false"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
