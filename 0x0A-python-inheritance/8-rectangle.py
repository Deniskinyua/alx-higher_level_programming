#!/usr/bin/python3
"""
Class Rectangle inherits from BaseGeometry (7-base_geometry.py)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """constructor"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
