i#!/usr/bin/python
"""
Write a function that removes all characters c and c from a string
  - Should return a new string
  - Do not import any module
  - Do not use str.replace()
"""


def no_c(my_string):
    new_string = my_string.translate({ord("c"): None})
    n_string = new_string.translate({ord("C"): None})
    return(n_string)
