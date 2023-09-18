#!/usr/bin/python3


import decimal, json
print(json.loads('1.1', parse_float=decimal.Decimal))
