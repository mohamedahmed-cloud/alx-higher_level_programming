#!/usr/bin/python3
from sys import argv
module = __import__(argv[1][:-3])

print(module.__doc__)