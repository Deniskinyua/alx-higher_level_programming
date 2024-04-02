#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for i in range(e):
        try:
            print("{}".format(my_list[e]), end="")
            elements = elements + 1
        except IndexError:
            continue
    print(" ")
    return elements
