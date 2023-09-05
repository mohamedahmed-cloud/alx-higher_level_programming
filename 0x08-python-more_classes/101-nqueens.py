#!/usr/bin/python3

from sys import argv
"""
    Implement for a n Queen problem using backtrack.
"""

if __name__ == "__main__":
    """
        main function
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(0)
    elif argv[1].isdigit() is False:
        print("N must be a number")
        exit(0)
    elif int(argv[1]) < 4:
        print("N must be at least 4")
        exit(0)
    print("Can't Solve Unit Yet.")
