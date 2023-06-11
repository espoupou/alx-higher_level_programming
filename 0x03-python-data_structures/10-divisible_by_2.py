#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = list()
    for i in my_list:
        l.append(False if i % 2 else True)
    return l
