#!/usr/bin/python3
"""
Function -> prints a text with 2 new lines after each of the
characters --> '.', '?' and ':'
"""


def text_indentation(text):
    """--> print text with 2 new lines after the three characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for t in text:
        if flag == 0:
            if t == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if t == '?' or t == '.' or t == ':':
                print(t)
                print()
                flag = 0
            else:
                print(t, end="")
