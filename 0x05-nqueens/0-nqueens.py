#!/usr/bin/python3
""" N Queen challenge solution """


import sys


def print_solution(board):
    """Prints the board configuration where each row
    corresponds to the column position of the queen."""
    print([[i, board[i]] for i in range(len(board))])


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at (row, col)"""
    # Check for column conflicts
    for r in range(row):
        if board[r] == col or \
           board[r] - r == col - row or \
           board[r] + r == col + row:
            return False
    return True


def solve_nqueens(N, board, row):
    """Backtracking function to solve the N Queens problem."""
    if row == N:  # All queens are placed
        print_solution(board)  # Print the solution
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  # Place the queen
            solve_nqueens(N, board, row + 1)


def nqueens(N):
    """Solve the N Queens problem."""
    board = [-1] * N
    solve_nqueens(N, board, 0)


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()
