#!/usr/bin/python3
"""
Class Square:
"""


class Square:
    """
    Class attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Class constructor
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculating the area
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
        Return
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for m in range(self.__size)]))

    @property
    def position(self):
        """
        Return: square in 2D
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set pos
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
