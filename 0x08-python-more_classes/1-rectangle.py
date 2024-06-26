#!/usr/bin/python3
"""
Write a class Rectangle defining a rectangle based on 0-rectangle.py
"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """class constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: height/return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : height --> return height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
