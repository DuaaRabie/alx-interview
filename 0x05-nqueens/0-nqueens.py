#!/usr/bin/python3
""" N Queen challenge solution """


import sys


def print_solution(board):
    """Prints the solution in the required format."""
    solution = []
    for row in board:
        solution.append([i for i in range(len(board)) if i == row])
    print(solution)


def is_valid(board, row, col):
    """Checks if it's valid to place a queen at (row, col)."""
    for i in range(row):
        # Check column conflict and diagonal conflicts
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n):
    """Solves the N Queens problem using backtracking."""
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """Solves the N Queens problem."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Start the backtracking process with an empty board
    board = [-1] * n
    solve_nqueens(board, 0, n)


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)


if __name__ == "__main__":
    main()
