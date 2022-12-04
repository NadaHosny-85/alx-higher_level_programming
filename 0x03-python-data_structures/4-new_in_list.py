#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    list_len = len(my_list)
    if (idx > list_len - 1):
        return (list_copy)
    elif (idx < 0):
        return (list_copy)
    else:
        list_copy[idx] = element
        return (list_copy)
