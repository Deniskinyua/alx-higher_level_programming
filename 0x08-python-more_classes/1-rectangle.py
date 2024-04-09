#!/usr/bin/python3
"""
Write a class Rectangle defining a rectangle based on 0-rectangle.py
"""


class Rectangle:
    """class constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """private instance attribute width"""
    @property
    def width(self):
        return self.width

    """setter for width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    """private instance attribute height"""
    @property
    def height(self):
        return self.height

    """Setter for height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
