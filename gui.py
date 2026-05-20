import tkinter as tk
from solver import solve  # your backtracking solver

class SudokuGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Sudoku Solver")

    self.cells = [[None for _ in range(9)] for _ in range(9)]

    self.create_grid()
    self.create_buttons()

  def create_grid(self):
    frame = tk.Frame(self.root)
    frame.pack()

    for i in range(9):
      for j in range(9):
        entry = tk.Entry(frame, width=3, font=("Arial", 18), justify="center")
        entry.grid(row=i, column=j)

        self.cells[i][j] = entry

  def get_board(self):
    board = []

    for i in range(9):
      row = []

      for j in range(9):
        val = self.cells[i][j].get()

        if val == "":
          row.append(0)
        else:
          row.append(int(val))

      board.append(row)

    return board

  def set_board(self, board):
    for i in range(9):
      for j in range(9):
        self.cells[i][j].delete(0, tk.END)

        if board[i][j] != 0:
          self.cells[i][j].insert(0, str(board[i][j]))

  def solve_sudoku(self):
    board = self.get_board()

    if solve(board):
      self.set_board(board)
    else:
      print("No solution found")

  def create_buttons(self):
    frame = tk.Frame(self.root)
    frame.pack(pady=10)

    solve_btn = tk.Button(frame, text="Solve", command=self.solve_sudoku)
    solve_btn.grid(row=0, column=0)

    clear_btn = tk.Button(frame, text="Clear", command=self.clear_board)
    clear_btn.grid(row=0, column=1)

  def clear_board(self):
    for i in range(9):
      for j in range(9):
        self.cells[i][j].delete(0, tk.END)


if __name__ == "__main__":
  root = tk.Tk()
  app = SudokuGUI(root)
  root.mainloop()
