#!/usr/bin/python3

from sys import argv

className = argv[-1][2:-3].capitalize()
module = __import__(argv[-1][:-3])
Rectangle = getattr(module, className)

print(module.__doc__)
print(Rectangle.__doc__)