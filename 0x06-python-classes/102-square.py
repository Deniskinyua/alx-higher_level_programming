#!/usr/bin/python3
"""
Compare 2 squares
"""


class Square:
    """
    The class
    """

    def __init__(self, size=0):
        """
        Initializing the class with a constructor
        """
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def __lt__(self, other):
        """
        Less than (<)
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        Less than or equal to (<=)
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        Greater Than (>)
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        Greater Than or Equal To(>=)
        """
        return (self.area() >= other.area())

    def __eq__(self, other):
        """
        ==
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        is not Equal (!=)
        """
        return (self.area() != other.area())

    def area(self):
        """
        Determine the square's area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Get size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size
        """
        if ((type(value) is int) or (type(value) is float)):
            if (value < 0):
                raise (ValueError("size must be >= 0"))
            else:
                self.__size = value
        else:
            raise (TypeError("size must be a number"))
