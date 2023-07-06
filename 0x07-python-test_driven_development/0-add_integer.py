#!/usr/bin/python3
"""Module for add function
"""


def add_integer(a, b=98):
    """Add function

       Args:
          a (int): first number
          b (int): second number

      Return:
         a + b

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
