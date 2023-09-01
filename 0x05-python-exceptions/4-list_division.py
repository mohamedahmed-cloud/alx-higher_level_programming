#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n1 = len(my_list_1)
    n2 = len(my_list_2)
    result = [0] * max(n1, n2)

    for i in range(max(n1, n2)):
        try:
            result[i] = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result[i] = 0 if result[i] == 0 else result[i]
    return result
