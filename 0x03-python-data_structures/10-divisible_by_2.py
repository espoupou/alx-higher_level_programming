#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    table = list()
    for i in my_list:
        table.append(False if i % 2 else True)
    return table
