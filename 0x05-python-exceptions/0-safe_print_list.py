#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print("".join(map(str, my_list[:x])))
        return min(x, len(my_list))
    except ValueError:
        return min(x, len(my_list))
