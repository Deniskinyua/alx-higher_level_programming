#!/usr/bin/python3
"""
Function: def pascal_triangle(n)
Return: a lists of lists of integers repping Pascal's triangle of n
Return: empty list of n <= 0
Given: n is always an intger
Donts: import any module
"""


def pascal_triangle(n):
    """method"""
    if n <= 0:
        return []

    res = []
    for elem in range(n):
        if elem == 0:
            res.append([1])
            continue
        if elem == 1:
            res.append([1, 1])
            continue
        row = []
        """init row"""
        for item in range(elem + 1):
            row.append(item)
        for item in range(1, elem):
            row[0] = 1
            row[elem] = 1
            row[item] = res[elem - 1][item] + res[elem - 1][item - 1]
        res.append(row)

    return res
