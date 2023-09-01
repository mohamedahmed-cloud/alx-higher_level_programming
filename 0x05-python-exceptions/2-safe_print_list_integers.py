#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    cnt = 0
    for i in my_list:
        cnt += 1

    try:
        if x <= cnt:
            value = int("".join(str(x) for x in my_list if isinstance(x, int)))
            cnt = sum(1 for x in my_list if isinstance(x, int))
            print("{:d}".format(value))
            return min(x, cnt)
        else:
            raise IndexError("list index out of range")

    except IndexError:
        raise
