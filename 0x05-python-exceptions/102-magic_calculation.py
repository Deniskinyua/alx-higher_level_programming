#!/usr/bin/python3
def magic_calculation(a, b):
    elem = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                elem += (a ** b) / i
        except:
            elem = b + a
            break
    return elem
