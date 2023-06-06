#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        i = number % 10
    else:
        i = number % -10
        i *= -1
    print("{:d}".format(i))
    return (i)
