#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        return result
