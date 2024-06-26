#!/usr/bin/python3
""" Class Square """


class Square:
    """ Private """

    def __init__(self, size=0):
        """
        Use size
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
