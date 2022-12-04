#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    modified_str = ""
    for i in str_len - 1:
        if (my_string[i] == 'c' || my_string[i] == 
            'C'):
            continue
        else:
            modified_str.append(my_string[i])
