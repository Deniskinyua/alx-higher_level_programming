#!/usr/bin/python3
"""
Print all integers of a list, in reverse order
    - One integer per line
    - Do not import any module
    - Assume that the list only cotains integers
    - Do not cast
    - MUST use str.format() to print
"""


def print_reversed_list_integer(my_list=[]):
    reversed_my_list = (my_list[::-1])
    my_list_length = len(my_list)

    for num in range(my_list_length):
        print("{:d}".format(reversed_my_list[num]))
