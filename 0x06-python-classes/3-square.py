#!/usr/bin/python3
""" Class Square """


class Square:
    """ Defining private instance """

    def __init__(self, size=0):
        """
        Using size as passed
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Return
        """

        return self.__size ** 2
