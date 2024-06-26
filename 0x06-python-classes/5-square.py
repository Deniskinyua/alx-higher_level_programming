#!/usr/bin/python3
"""
Defining the class Square
"""


class Square:
    """
    Class attributes:
    """
    def __init__(self, size=0):
        """
        Initialize
        """
        self.size = size

    def area(self):
        """
        calculate the square's area
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

    def my_print(self):
        """
        Square
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
