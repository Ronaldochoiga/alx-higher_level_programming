#!/usr/bin/python3
"""N Queens Module.

Contains the N Queens problem solver.
"""
import sys


def error_exit(message="", code=1):
    """Handles exit.

    Args:
        message (str): the message to display on stdout.
        code (int): the exit code.
    """
    print(message)
    exit(code)


def test_pos(board, a):
    """Tests if queen can be placed at the current pos.

    Args:
        board (list): the chessboard.
        a (int): the height par.
    """
    for i in range(a):
        if board[a][1] is board[i][1]:
            return False
        if abs(board[a][1] - board[i][1]) == a - i:
            return False
    return True


def rec_backtrack(board, a):
    """track the possibility.

    Args:
        board (list): the chessboard.
        a (int): the height parameter.
    """
    if a is N:
        print(board)
    else:
        for b in range(N):
            board[a][1] = b
            if test_pos(board, a):
                rec_backtrack(board, a + 1)


if len(sys.argv) is not 2:
    error_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except:
    error_exit("N must be a number")

if N < 4:
    error_exit("N must be at least 4")

board = [[a, 0] for a in range(N)]
rec_backtrack(board, 0)
