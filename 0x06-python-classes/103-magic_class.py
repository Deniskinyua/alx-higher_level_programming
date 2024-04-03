#!/usr/bin/python3
"""
Class MagicClass
"""
import math


class MagicClass:
    """
    The class
    """
    def __init__(self, radius=0):
        """
        Initialization
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Determine Area
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Circumference
        """
        return (2 * math.pi * self.__radius)
