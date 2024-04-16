#!/usr/bin/python3
"""
Class Rectangle inherits from 7-base_geometry
"""


class BaseGeometry:
    """method : area"""
    def area(self):
        raise Exception("area() is not implemented")
    """method : integer_validator"""
    def integer_validator(self, name, value):
        """validation"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class : Rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
