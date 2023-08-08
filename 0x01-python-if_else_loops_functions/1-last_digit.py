#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
mul = 1
if number < 0:
    mul *= -1
if last_digit * mul > 5:
    print(f"Last digit of {number :d} is {last_digit * mul:d} and\
 is greater than 5")
elif last_digit * mul == 0:
    print(f"Last digit of {number :d} is {last_digit * mul:d} and is 0")
elif last_digit * mul < 6:
    print(f"Last digit of {number :d} is {last_digit * mul:d} and is less\
 than 6 and not 0")
