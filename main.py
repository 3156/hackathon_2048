import tkinter as tk
import math

canvas = None

SQUARE_LENGTH = 100
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 8
TILE_X_COUNT = 2
TILE_Y_COUNT = 6
LENGTH_X = SQUARE_LENGTH * TILE_X_COUNT + BORDER_WIDTH * TILE_X_COUNT
LENGTH_Y = SQUARE_LENGTH * TILE_Y_COUNT + BORDER_WIDTH * TILE_Y_COUNT
CELL_COLOR = '#cbbeb5'
BORDER_COLOR = '#b2a698'

def set_field():
  canvas.create_rectangle(POSITION["x"], POSITION["y"], LENGTH_X + POSITION["x"], LENGTH_Y + POSITION["y"], fill='#cbbeb5', width=BORDER_WIDTH, outline=BORDER_COLOR)

  for i in range(TILE_X_COUNT - 1):
    x = POSITION["x"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    canvas.create_line(x, POSITION["y"], x, LENGTH_Y + POSITION["y"], width=BORDER_WIDTH, fill=BORDER_COLOR)
  for i in range(TILE_Y_COUNT - 1):
    y = POSITION["y"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    canvas.create_line(POSITION["x"], y, LENGTH_X + POSITION["x"], y, width=BORDER_WIDTH, fill=BORDER_COLOR)

def create_canvas():
  root = tk.Tk()
  root.geometry(f"""{LENGTH_X + POSITION["x"] * 2}x{LENGTH_Y + POSITION["y"] * 2}""")
  root.title("2048")
  canvas = tk.Canvas(root, width=(LENGTH_X + POSITION["x"]), height=(LENGTH_Y + POSITION["y"]))
  canvas.place(x=0, y=0)

  return root, canvas

def set_number(num, x, y):
  center_x = POSITION["x"] + BORDER_WIDTH * x + BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
  center_y = POSITION["y"] + BORDER_WIDTH * y + BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2
  canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill=CELL_COLOR, width=0)
  canvas.create_text(center_x, center_y, text=num, justify="center", font=("", 70), tag="count_text")

def operate(event):
  print(event.keysym)

def play():
  global canvas
  root, canvas = create_canvas()
  set_field()
  set_number("2", 0, 3)
  set_number("4", 2, 1)
  root.bind("<Key>", lambda event: operate(event))
  root.mainloop()

play()
