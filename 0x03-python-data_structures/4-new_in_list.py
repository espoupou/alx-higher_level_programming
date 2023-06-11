#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l = my_list[:]
    if 0 <= idx < len(my_list):
        l[idx] = element
    return l
