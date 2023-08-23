#!/usr/bin/python3

import functools
x = functools.reduce(lambda a,b :a + b, range(1,101))
print(x)

