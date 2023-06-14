#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dico = list(a_dictionary.keys())
    dico.sort()
    for i in dico:
        print("{}: {}".format(i, a_dictionary.get(i)))
