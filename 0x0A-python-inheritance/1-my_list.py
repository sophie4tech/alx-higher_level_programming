#!/usr/bin/python3
"""
Defines an inherited list class MyList
"""

class MyList(list):
    """subclass of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
