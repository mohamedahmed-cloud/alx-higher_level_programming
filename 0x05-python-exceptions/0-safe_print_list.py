#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    for i in my_list:
        cnt += 1
    try:
        print("".join(map(str, my_list[:x])))
        return min(x, cnt)
    except ValueError:
        return min(x, cnt)
