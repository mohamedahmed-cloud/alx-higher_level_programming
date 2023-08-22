#!/usr/bin/python3
def roman_to_int(roman_string):

    all = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
           "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
           "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
           "", "M", "MM", "MMM"]
    if isinstance(roman_string, (int, float)) or roman_string is None:
        return 0

    def find_order(curr):
        if "I" in curr or "V" in curr:
            return 1
        elif "X" in curr or "L" in curr:
            return 10
        elif "C" in curr or "D" in curr:
            return 100
        elif "M" in curr:
            return 1000

    curr = ""
    ans = 0

    for i in roman_string:
        curr += i
        if curr not in all:
            ans += (all.index(curr[:-1]) % 10) * find_order(curr[:-1])
            curr = curr[-1]

    ans += (all.index(curr) % 10) * find_order(curr)
    return ans
