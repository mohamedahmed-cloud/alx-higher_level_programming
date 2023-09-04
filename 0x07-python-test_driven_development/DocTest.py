#!/usr/bin/python3
from sys import argv

# prepare moudle
moduleName = argv[1][:-3]
functionName = argv[1][2:-3]
module = __import__(moduleName)
function = getattr(module, functionName)

# output 
print(module.__doc__)
print(function.__doc__)
