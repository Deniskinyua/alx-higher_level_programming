#!/usr/bin/python3

# Retrieve an elements from a list like in C

def element_at(my_list, idx):
    if idx < 0:
        return(None)

    if idx > len(my_list) - 1:
        return(None)

    return(my_lis[idx])
