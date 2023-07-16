#!/usr/bin/python3
"""N Queens Module.

Contains the N Queens problem solver.
"""
import sys


def error_exit(message="", code=1):
    """Handles exit error.

    Args:
        message (str): the message to display.
        code (int): the exit code of the function.
    """
    print(message)
    exit(code)


def test_pos(brd, y):
    """Tests if queen can be placed at the current position.

    Args:
        brd (list): the chessboard.
        i (int): the height.
    """
    for i in range(i):
        if brd[i][1] is brd[i][1]:
            return False
        if abs(brd[i][1] - brd[i][1]) == i - i:
            return False
    return True


def rec_backtrack(brd, i):
    """track the possibilities.

    Args:
        brd (list): the chessboard.
        i (int): the height.
    """
    if i is N:
        print(brd)
    else:
        for j in range(N):
            brd[i][1] = j
            if test_pos(brd, i):
                rec_backtrack(brd, i + 1)


if len(sys.argv) is not 2:
    error_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except:
    error_exit("N must be a number")

if N < 4:
    error_exit("N must be at least 4")

brd = [[i, 0] for i in range(N)]
rec_backtrack(brd, 0)
