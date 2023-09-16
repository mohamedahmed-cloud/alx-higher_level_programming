#!/usr/bin/python3
from sys import argv
module = __import__(argv[1][:-3])
function = getattr(module, argv[1][2:-3], None)

print(module.__doc__)
print(function.__doc__)

