#!/usr/bin/python3

# Retrieve an elements from a list like in C

def element_at(my_list, idx):
    length_of_list = len(my_list)

    if idx < 0:
        return (None)

    if idx > length_of_list - 1:
        return (None)

    return (my_list[idx])
