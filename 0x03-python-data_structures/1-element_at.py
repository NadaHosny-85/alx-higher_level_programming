#!/usr/bin/python3
def element_at(my_list, idx):
    list_count = len(my_list)
    if (idx > list_count - 1):
        return (None)
    elif (idx < 0):
        return (None)
    else:
        return (my_list[idx])
