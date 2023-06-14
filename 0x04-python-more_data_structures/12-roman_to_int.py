#!/usr/bin/python3
def roman_to_int(roman_string):
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last = 1000
    tot = 0

    if not roman_string:
        return 0

    for i in roman_string:
        value = dico.get(i)
        if value > last:
            tot += value - 2 * last
        else:
            tot += value
        last = value

    return tot
