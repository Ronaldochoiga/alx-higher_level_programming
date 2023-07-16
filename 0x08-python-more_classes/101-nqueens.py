#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""
from sys import argv
if __name__ == "__main__":
    c = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be c number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    # initialize the answer list
    for k in range(n):
        c.append([k, None])

    def already_exists(q):
        """check that c queen does not exist in that q value"""
        for p in range(n):
            if q == c[p][1]:
                return True
        return False

    def reject(p, q):
        """determines whether to reject the solution or not"""
        if (already_exists(q)):
            return False
        k = 0
        while(k < p):
            if abs(c[k][1] - q) == abs(k - p):
                return False
            k += 1
        return True

    def clear_a(p):
        """clears the ans from the point of failure onwards"""
        for k in range(p, n):
            c[k][1] = None

    def nqueens(p):
        """recursive backtracking function to find the sol"""
        for q in range(n):
            clear_a(p)
            if reject(p, q):
                c[p][1] = q
                if (p == n - 1):  # accepts the solution
                    print(c)
                else:
                    nqueens(p + 1)  # moves on to next p value to continue
    # start the recursive process at p = 0
    nqueens(0)
