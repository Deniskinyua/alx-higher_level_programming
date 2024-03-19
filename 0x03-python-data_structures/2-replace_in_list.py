#!/usr/bin/python3
# Replace an element in a list at a specific position

def replace_in_list(my_list, idx, element):
    list_length = len(my_list)

    if idx < 0:
        return (my_list)

    elif idx > list_length - 1:
        return (my_list)

    my_list[idx] = element
    return (my_list)
