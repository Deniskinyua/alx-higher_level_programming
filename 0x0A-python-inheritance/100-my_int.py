#!/usr/bin/python3
"""
class MyInt inherits from int
"""


class MyInt(int):
    """rebel"""
    def __new__(x, *args, **kwargs):
        """instantiate class"""
        return super(MyInt, x).__new__(x, *args, **kwargs)

    def __eq__(self, other):
        """chek != to --> =="""
        return int(self) != other

    def __ne__(self, other):
        """check == to --> !="""
        return int(self) == other
