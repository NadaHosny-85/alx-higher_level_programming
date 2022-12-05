#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_checked = []
    for num in my_list:
        if (num % 2 == 0):
            list_checked.append(True)
        else:
            list_checked.append(False)
    return (list_checked)
