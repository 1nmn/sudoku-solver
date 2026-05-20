# generator.py

import random
import copy
from solver import solve, is_valid


def empty_board():
  return [[0 for _ in range(9)] for _ in range(9)]


# Generate a fully solved board
def generate_full_board():

  board = empty_board()
  solve(board)
  return board


# Count solutions (stop early if more than 1)
def count_solutions(board):

  board = copy.deepcopy(board)
  count = 0

  def backtrack(b):

    nonlocal count

    if count > 1:
      return

    empty = None

    for r in range(9):
      for c in range(9):
        if b[r][c] == 0:
          empty = (r, c)
          break
      if empty:
        break

    if not empty:
      count += 1
      return

    r, c = empty

    for num in range(1, 10):

      if is_valid(b, r, c, num):
        b[r][c] = num
        backtrack(b)
        b[r][c] = 0

  backtrack(board)
  return count


def remove_numbers(board, removals):

  while removals > 0:

    r = random.randint(0, 8)
    c = random.randint(0, 8)

    if board[r][c] == 0:
      continue

    backup = board[r][c]
    board[r][c] = 0

    # ensure unique solution
    if count_solutions(board) != 1:
      board[r][c] = backup
    else:
      removals -= 1


def generate_sudoku(difficulty="medium"):

  board = generate_full_board()

  if difficulty == "easy":
    remove_numbers(board, 30)

  elif difficulty == "medium":
    remove_numbers(board, 40)

  elif difficulty == "hard":
    remove_numbers(board, 50)

  return board
