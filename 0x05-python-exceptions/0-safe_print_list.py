#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        return int("".join(map(str, my_list[:x])))
    except ValueError:
        return "".join(my_list[:x])
