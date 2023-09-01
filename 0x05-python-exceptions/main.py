#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = []
x = 0
nb_print = safe_print_list_integers(my_list, x)
print("{:d}".format(nb_print))