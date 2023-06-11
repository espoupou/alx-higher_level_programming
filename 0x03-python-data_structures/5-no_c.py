#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for i in my_string:
        string += i if i != 'c' and i != 'C' else ""
    return string
