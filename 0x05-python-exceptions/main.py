#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = ["y", "y"]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:s}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:s}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 10)
print("nb_print: {:s}".format(nb_print))