#!/usr/bin/python3
for i in range(100):
    print("{0:02d}{', ' if i != 99 else ''}".format(i), end="")
print()
