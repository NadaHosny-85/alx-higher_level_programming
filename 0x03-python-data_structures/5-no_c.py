#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    modified_str = ""
    for i in range(str_len):
        if ((my_string[i] != 'c')
                and (my_string[i] != 'C')):
            modified_str += my_string[i]
    return (modified_str)
