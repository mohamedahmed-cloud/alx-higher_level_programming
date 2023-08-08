#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = i
        if 97 <= ord(i) <= 123:
            x = chr(ord(i) - 32)
        print("{:s}".format(x), end="")
    print()
