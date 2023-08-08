#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        ans = ""
        if i % 3 == 0:
            ans += "Fizz"
        if i % 5 == 0:
            ans += "Buzz"
        if not ans:
            print(i, end=' ')
            continue
        print("{:s}".format(ans), end=" ")
