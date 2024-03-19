i#!/usr/bin/python
"""
Write a function that removes all characters c and c from a string
  - Should return a new string
  - Do not import any module
  - Do not use str.replace()
"""


def no_c(my_string):
    new_string = list(my_string)
    length_of_array = len(new_string)
    r_string = []
    n_string = []

    for c in range(length_of_array):
        if new_string[c] != 'c':
            r_string.append(new_string[c])

    for C in range(len(r_string)):
        if r_string[C] != 'C':
            n_string.append(r_string[C])
    return ("".join(n_string))
