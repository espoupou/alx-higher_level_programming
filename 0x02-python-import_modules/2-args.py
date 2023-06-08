#!/usr/bin/python3
import sys

if __name__ == "__main__":
    L = len(sys.argv)

    if L > 1:
        print("{} argument{}:".format(L - 1, 's' if l > 2 else ''))
    else:
        print("{} arguments.".format(0))

    for arg, i in zip(sys.argv[1:], range(1, L)):
        print("{}: {}".format(i, arg))
