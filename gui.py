# gui.py

import tkinter as tk
from solver import solve
from generator import generate_sudoku


class SudokuGUI:

  def __init__(self, root):

    self.root = root
    self.root.title("Sudoku Solver + Generator")

    self.cells = [[None for _ in range(9)] for _ in range(9)]

    self.create_grid()
    self.create_buttons()

  def create_grid(self):

    frame = tk.Frame(self.root)
    frame.pack()

    for r in range(9):
      for c in range(9):

        bg = "#ffffff"
        if (r // 3 + c // 3) % 2 == 0:
          bg = "#f0f0f0"

        entry = tk.Entry(
            frame,
            width=3,
            font=("Arial", 18),
            justify="center",
            bg=bg
        )

        entry.grid(row=r, column=c, padx=1, pady=1)

        self.cells[r][c] = entry

  def get_board(self):

    board = []

    for r in range(9):
      row = []
      for c in range(9):

        val = self.cells[r][c].get()

        if val == "":
          row.append(0)
        else:
          row.append(int(val))

      board.append(row)

    return board

  def set_board(self, board):

    for r in range(9):
      for c in range(9):

        self.cells[r][c].delete(0, tk.END)

        if board[r][c] != 0:
          self.cells[r][c].insert(0, str(board[r][c]))

  def solve_board(self):

    board = self.get_board()

    if solve(board):
      self.set_board(board)
    else:
      print("No solution found")

  def generate_board(self, difficulty="medium"):

    board = generate_sudoku(difficulty)
    self.set_board(board)

  def clear_board(self):

    for r in range(9):
      for c in range(9):
        self.cells[r][c].delete(0, tk.END)

  def create_buttons(self):

    frame = tk.Frame(self.root)
    frame.pack(pady=10)

    tk.Button(frame, text="Solve", command=self.solve_board).grid(
        row=0, column=0)

    tk.Button(frame, text="Clear", command=self.clear_board).grid(
        row=0, column=1)

    tk.Button(frame, text="Generate Easy",
              command=lambda: self.generate_board("easy")).grid(row=0, column=2)

    tk.Button(frame, text="Generate Medium",
              command=lambda: self.generate_board("medium")).grid(row=0, column=3)

    tk.Button(frame, text="Generate Hard",
              command=lambda: self.generate_board("hard")).grid(row=0, column=4)


if __name__ == "__main__":

  root = tk.Tk()
  app = SudokuGUI(root)
  root.mainloop()
