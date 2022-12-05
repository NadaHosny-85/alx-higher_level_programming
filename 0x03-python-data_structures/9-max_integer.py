#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    max_num = 0
    if (list_len == 0):
        return (None)
    for num in my_list:
        if (num > max_num):
            max_num = num
        else:
            continue
    return (max_num)
