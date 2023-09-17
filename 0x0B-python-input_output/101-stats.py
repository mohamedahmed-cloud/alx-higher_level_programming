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


def print_info():
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except Exception:
            pass

        try:
            file_size += int(pieces[-1])
        except Exception:
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
