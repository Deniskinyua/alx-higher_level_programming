#!/usr/bin/python3
"""
class MyList inherits from list:
"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
