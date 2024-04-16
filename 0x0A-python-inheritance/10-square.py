#!/usr/bin/python3
"""
Class Square inherits from 9-rectangle.py
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Constructor"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area"""
        return self.__size ** 2
