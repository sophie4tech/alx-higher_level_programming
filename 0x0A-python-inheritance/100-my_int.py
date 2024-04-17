#!/usr/bin/python3
"""
Defines the class MyInt
"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
