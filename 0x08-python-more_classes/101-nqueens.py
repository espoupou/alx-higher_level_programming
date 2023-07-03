#!/usr/bin/python3
"""Module that resolves the N-Queen puzzle using backtracking

"""


def is_safe(queen_p, queen_n):
    """Method that determines if the queens can or can't kill each other

    Args:
        queen_p: array that has the queens positions
        queen_n: queen number

    Returns:
        True: when can kill
        False: when killing is possible
    """
    for i in range(queen_n):
        if queen_p[i] == queen_p[queen_n]:
            return False
        if abs(queen_p[i] - queen_p[queen_n]) == abs(i - queen_n):
            return False
    return True


def backtrack(queen_p, queen_n):
    """execute the Backtracking algorithm

    Args:
        queen_p: array that has the queens positions
        queen_n: queen number
    """

    if queen_n == len(queen_p):
        res = []
        for i in range(queen_n):
            res.append([i, queen_p[i]])
        print(res)
        return
    queen_p[queen_n] = -1

    while queen_p[queen_n] < len(queen_p) - 1:
        queen_p[queen_n] += 1
        if is_safe(queen_p, queen_n) is True:
            if queen_n is not len(queen_p):
                backtrack(queen_p, queen_n + 1)


if __name__ == '__main__':

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen_pos = [-1 for i in range(size)]

    backtrack(queen_pos, 0)
