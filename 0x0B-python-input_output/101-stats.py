#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C),
    prints those statistics since the beginning:
    Total file size: File size: <total size>

    where is the sum of all previous (see input format above)
    Number of lines by status code:

    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

    if a status code doesn’t appear, don’t print anything for
    this status code

    format: <status code>: <number>

    status codes should be printed in ascending order
"""


import sys


initial = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
status_dict = initial.copy()
size = 0


def print_data():
    print(f"File size: {size}")
    for key, value in status_dict.items():
        if value:
            print(f"{key}: {value}")


try:
    cnt = 0
    for line in sys.stdin:
        cnt += 1

        all = line.split()
        try:
            status = all[-2]
            status_dict[int(status)] += 1
        except Exception:
            pass
        try:
            size += int(all[-1])
        except Exception:
            pass

        if cnt != 0 and cnt % 10 == 0:
            print_data()
            cnt = 0
            status_dict = initial.copy()
            size = 0
    print_data()
except KeyboardInterrupt:
    print_data()
    raise
