#!/usr/bin/python3

def max_integer(my_list=[]):

    x = my_list[0] if len(my_list) > 0 else None

    if x is None:
        return x

    for i in my_list:
        x = i if i > x else x
    return x
