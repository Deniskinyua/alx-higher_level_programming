#!/usr/bin/python3

"""
Print a matrix of integers
  - Do not import any module
  - Assume the list cotains only integers
  - Do not cast
  - Use str.format() to print
"""


def print_matrix_integer(matrix=[[]]):
    matrix_length = len(matrix)

    for lt in range(matrix_length):
        length = len(matrix[lt])
        for tl in range(length):
            if tl != 0:
                print(" ", end='')
            print("{:d}".format(matrix[lt][tl]), end='')
        print()
