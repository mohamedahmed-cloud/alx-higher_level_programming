#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics

"""


while True:
    status_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
    size = 0
    for i in range(10):
        all = input().split()
        status = all[-2]
        size += int(all[-1])
        status_dict[int(status)] += 1

    print(f"File size: {size}")
    for key, value in status_dict.items():
        if value:
            print(f"{key}: {value}")
