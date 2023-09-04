#!/usr/bin/python3

from math import pi
def area(r):
	if type(r) in [list, set, dict, str, bool, complex]:
		raise TypeError("Must Be real Number")
	if r < 0:
		raise ValueError("Must Be >= 0")
	area = pi * (r ** 2)
	return area
