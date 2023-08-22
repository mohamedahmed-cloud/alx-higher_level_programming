#!/usr/bin/python3
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
