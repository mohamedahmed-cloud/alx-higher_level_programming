#!/usr/bin/python3
# from functools import reduce
def best_score(a_dictionary):
    ans = ""
    m = -float("inf")
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > m:
            m = value
            ans = key
    return ans
    # or using reduce
    # m = reduce(lambda x, y: x if (x[1] > y[1]) else y, [[key, value]
    # for key, value in a_dictionary.items()])
    # return m[0]
