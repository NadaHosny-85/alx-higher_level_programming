#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if (number == 0):
        print(last_digit, end="")
        return (last_digit)
    elif (number < 0):
        last_digit = number % -10
        print(last_digit, end="")
        return (last_digit)
    else:
        last_digit = number % 10
        print(last_digit, end="")
        return (last_digit)
