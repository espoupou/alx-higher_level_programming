#!/usr/bin/python3
import sys

if __name__ == "__main__":
    s = 0

    for arg in sys.argv[1:]:
        s += int(arg)
    print("{}".format(s))
