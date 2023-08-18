#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    n = len(my_list)
    ans = [False] * n
    for i in range(n):
        ans[i] = True if my_list[i] % 2 == 0 else False
    return ans