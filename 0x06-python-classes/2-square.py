#!/usr/bin/python3
# Write a class Square that defines a square by based on 1-square.py


class Square:
    # passing private attributes

    def __init__(self, size=0):
        # def

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
