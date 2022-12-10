#!/usr/bin/python3
def roman_to_int(roman_string):
    if ((roman_string is None) or (type(roman_string) is not str)):
        return (0)
    romans_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                    "D": 500, "M": 1000}
    str_len = len(roman_string)
    num = 0
    for i in range(str_len):
        if (roman_dict.get(roman_string[i], 0) == 0):
            return (0)
        if (i != (str_len - 1) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            num += roman_dict[roman_string[i]] * -1
        else:
            num += roman_dict[roman_string[i]]
    return (num)
