def printMatrix(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col, N):
    # Check row (left side)
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal (left side)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal (left side)
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQ(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1

            if solveNQ(board, col + 1, N):
                return True

            board[i][col] = 0

    return False


def main():
    N = int(input("Enter size of the chessboard: "))
    board = [[0] * N for i in range(N)]  # Initialize an N×N board with 0s

    if not solveNQ(board, 0, N):
        print("Solution does not exist")
        return False

    printMatrix(board, N)  # Print the solution
    return True


if __name__ == "__main__":
    main()
