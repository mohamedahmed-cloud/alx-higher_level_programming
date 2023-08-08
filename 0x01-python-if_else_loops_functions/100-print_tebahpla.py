#!/usr/bin/python3
for i in range(1, 27):
    if i % 2 == 1:
        print(chr(123 - i), end="")
        continue
    print(chr(91 - i), end="")
