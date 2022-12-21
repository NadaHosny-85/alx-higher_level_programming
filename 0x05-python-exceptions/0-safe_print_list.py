#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_elem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            count_elem += 1
    print("")
    return (count_elem)
