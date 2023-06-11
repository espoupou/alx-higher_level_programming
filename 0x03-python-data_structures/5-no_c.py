#!/usr/bin/python3
def no_c(my_string):
    l = ""
    for i in my_string:
        l += i if i != 'c' and i != 'C' else ""
    return l
