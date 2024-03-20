#!/usr/bin/python3
"""
Add 2 tuples
  - Returns a tuple with 2 integers:
    - 1st element should be the addition of the first element of each argument
    - 2nd element should be the addition of the second element of each argument
  - You are not allowed to import any module
  - You can assume that the two tuples will only contain integers
  - If a tuple is smaller than 2, use the value 0 for each missing integer
  - If a tuple is bigger than 2, use only the first 2 integers
"""


def add_tuple(tuple_a=(), tuple_b=()):

    # Define lengths:
    length_Tuple_a = len(tuple_a)
    length_Tuple_b = len(tuple_b)

    if length_Tuple_a == 0:
        ta = 0
        tb = 0
    elif length_Tuple_a == 1:
        ta = tuple_a[0]
        tb = 0
    else:
        ta = tuple_a[0]
        tb = tuple_a[1]

    if length_Tuple_b == 0:
        aa = 0
        bb = 0
    elif length_Tuple_b == 1:
        aa = tuple_b[0]
        bb = 0
    else:
        aa = tuple_b[0]
        bb = tuple_b[1]

    return(ta + aa, tb + bb)
