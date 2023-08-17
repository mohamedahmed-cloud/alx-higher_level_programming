#!/usr/bin/python3

def no_c(my_string):
    # print(my_string)
    str = ""
    for i in my_string:
        str += i if i not in "cC" else ""
    return str
