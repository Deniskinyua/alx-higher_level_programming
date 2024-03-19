#!/usr/bin/python3
"""
Write a function that removes all characters c and c from a string
  - Should return a new string
  - Do not import any module
  - Do not use str.replace()
"""


def no_c(my_string):
    i = 0
    l_string = my_string[:]
    for letter in range(len(my_string)):
        if (my_string[letter] == 'C' or my_string[letter] == 'c'):
            l_string = l_string[:(letter - i)] + my_string[(letter + i):]
            i += 1
    return (l_string)
