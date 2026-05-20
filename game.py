# game.py

import pygame
from solver import solve, is_valid
from generator import generate_sudoku

pygame.init()

WIDTH = 540
WIN = pygame.display.set_mode((WIDTH, WIDTH + 60))
pygame.display.set_caption("Sudoku Solver (Pygame)")

FONT = pygame.font.SysFont("Arial", 35)
SMALL = pygame.font.SysFont("Arial", 25)

board = generate_sudoku("medium")

selected = None
running = True


def draw_grid():

  gap = WIDTH // 9

  for i in range(10):

    thick = 3 if i % 3 == 0 else 1

    pygame.draw.line(WIN, (0, 0, 0), (0, i*gap), (WIDTH, i*gap), thick)
    pygame.draw.line(WIN, (0, 0, 0), (i*gap, 0), (i*gap, WIDTH), thick)


def draw_numbers():

  gap = WIDTH // 9

  for r in range(9):
    for c in range(9):

      num = board[r][c]

      if num != 0:

        text = FONT.render(str(num), True, (0, 0, 0))
        WIN.blit(text, (c*gap + 18, r*gap + 10))


def draw_buttons():

  pygame.draw.rect(WIN, (200, 200, 200), (0, WIDTH, WIDTH, 60))

  solve_text = SMALL.render("SOLVE", True, (0, 0, 0))
  check_text = SMALL.render("CHECK", True, (0, 0, 0))
  clear_text = SMALL.render("CLEAR", True, (0, 0, 0))
  gen_text = SMALL.render("GENERATE", True, (0, 0, 0))

  WIN.blit(solve_text, (20, WIDTH+20))
  WIN.blit(check_text, (120, WIDTH+20))
  WIN.blit(clear_text, (230, WIDTH+20))
  WIN.blit(gen_text, (340, WIDTH+20))


def get_clicked(pos):

  x, y = pos

  if y > WIDTH:
    return None

  gap = WIDTH // 9

  return y // gap, x // gap


def check_board():

  for r in range(9):
    for c in range(9):
      num = board[r][c]

      if num == 0:
        continue

      board[r][c] = 0
      valid = is_valid(board, r, c, num)
      board[r][c] = num

      if not valid:
        return False

  return True


def solve_board():
  solve(board)


def clear_board():
  global board
  board = [[0]*9 for _ in range(9)]


def generate():
  global board
  board = generate_sudoku("medium")


while running:

  WIN.fill((255, 255, 255))

  draw_numbers()
  draw_grid()
  draw_buttons()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:

      pos = pygame.mouse.get_pos()

      if pos[1] > WIDTH:

        if 0 < pos[0] < 100:
          solve_board()

        elif 100 < pos[0] < 200:
          print("Valid:", check_board())

        elif 200 < pos[0] < 320:
          clear_board()

        elif 320 < pos[0] < 520:
          generate()

      else:
        selected = get_clicked(pos)

    elif event.type == pygame.KEYDOWN and selected:

      r, c = selected

      if event.unicode.isdigit():

        num = int(event.unicode)

        if 1 <= num <= 9:
          board[r][c] = num

  pygame.display.update()

pygame.quit()
