#!/usr/bin/python3
"""Defining a square based on 3-square.py"""


class Square:
    """
    Defining the class attributes
    """
    def __init__(self, size=0):
        """
        initializing the square
        """
        self.size = size

    def area(self):
        """
        Calculating the area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
