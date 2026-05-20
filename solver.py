# solver.py

import random


def find_empty(board):
  for r in range(9):
    for c in range(9):
      if board[r][c] == 0:
        return r, c
  return None


def is_valid(board, row, col, num):

  # row
  if num in board[row]:
    return False

  # col
  for i in range(9):
    if board[i][col] == num:
      return False

  # box
  br = (row // 3) * 3
  bc = (col // 3) * 3

  for r in range(br, br + 3):
    for c in range(bc, bc + 3):
      if board[r][c] == num:
        return False

  return True


def solve(board):

  empty = find_empty(board)
  if not empty:
    return True

  r, c = empty

  nums = list(range(1, 10))
  random.shuffle(nums)

  for num in nums:
    if is_valid(board, r, c, num):

      board[r][c] = num

      if solve(board):
        return True

      board[r][c] = 0

  return False
