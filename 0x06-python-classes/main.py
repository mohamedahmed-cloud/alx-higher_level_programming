#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

try:
    mc = MagicClass(4)
except Exception as e:
    print(e)