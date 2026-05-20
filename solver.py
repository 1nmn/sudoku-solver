board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(board):

    for i, row in enumerate(board):

        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j, num in enumerate(row):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(num, end=" ")

        print()


def find_empty(board):
    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:
                return row, col

    return None


def is_valid(board, row, col, num):

    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):

            if board[i][j] == num:
                return False

    return True


def solve(board):

    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(board, row, col, num):

            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


print("Original Board:")
print_board(board)

if solve(board):

    print("\nSolved Board:")
    print_board(board)

else:
    print("No solution exists.")
