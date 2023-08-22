#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    sub = 0
    for i in my_list:
        mul += i[0] * i[1]
        sub += i[1]
    return mul / sub
