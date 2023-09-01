#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    cnt = length = 0

    for i in my_list:
        length += 1

    value = [b for b in my_list if isinstance(b, int)]

    for i in value:
        cnt += 1

    if value:
        value = int("".join(map(str, value[:x])))
    else:
        value = 0

    try:
        if x <= length:
            if value:
                print("{:d}".format(value))
            return min(x, cnt)
        else:
            print(value, end="")
            raise IndexError("list index out of range")

    except IndexError:
        raise
