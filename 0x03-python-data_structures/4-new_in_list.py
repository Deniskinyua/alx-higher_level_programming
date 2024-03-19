#!/usr/bin/python3

"""
Replace an element at index idx, without modifying the original list
  - If idx is negative, the function should return a copy of the origina list
  - idx out of range? the function should return a copy of the original ist
  - Do not import any module
  - Do not use try/except
"""


def new_in_list(my_list, idx, element):
    # Creating a copy
    my_list_copy = my_list

    if idx < 0:
        return (my_list_copy)
    if idx > my_list_length - 1:
        return (my_list_copy)
    my_list_copy[idx] = element
    return my_list_copy
