import random


def find_empty(board):
  for r in range(9):
    for c in range(9):
      if board[r][c] == 0:
        return r, c
  return None


def is_valid(board, row, col, num):

  # Row check
  if num in board[row]:
    return False

  # Column check
  for i in range(9):
    if board[i][col] == num:
      return False

  # 3x3 box check
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

  nums = list(range(1, 10))
  random.shuffle(nums)   # IMPORTANT: makes generator work

  for num in nums:

    if is_valid(board, row, col, num):

      board[row][col] = num

      if solve(board):
        return True

      board[row][col] = 0

  return False