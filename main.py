import tkinter as tk
import math

canvas = None

SQUARE_LENGTH = 100
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 8
TILE_X_COUNT = 5
TILE_Y_COUNT = 3
LENGTH_X = SQUARE_LENGTH * TILE_X_COUNT + BORDER_WIDTH * TILE_X_COUNT
LENGTH_Y = SQUARE_LENGTH * TILE_Y_COUNT + BORDER_WIDTH * TILE_Y_COUNT
CELL_COLOR = '#cbbeb5'
BORDER_COLOR = '#b2a698'

tiles = []
positions = [[0] * TILE_X_COUNT for i in range(TILE_Y_COUNT)]

positions[0][1] = 2
positions[1][3] = 4
positions[2][2] = 8
positions[0][4] = 16

class Tile:
  def __init__(self, x, y, number):
    self.x = x
    self.y = y
    self.number = number

  def createTile(self):
    center_x = POSITION["x"] + BORDER_WIDTH * self.x + BORDER_WIDTH / 2 + SQUARE_LENGTH * self.x + SQUARE_LENGTH / 2
    center_y = POSITION["y"] + BORDER_WIDTH * self.y + BORDER_WIDTH / 2 + SQUARE_LENGTH * self.y + SQUARE_LENGTH / 2
    canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill=CELL_COLOR, width=0, tag='tile')
    canvas.create_text(center_x, center_y, text=self.number, justify="center", font=("", 70), tag="number")

def removeTiles():
  canvas.delete('tile')
  canvas.delete('number')
  del tiles[:]

def positionToTiles():
  removeTiles()
  for y, position_y in enumerate(positions):
    for x, position in enumerate(position_y):
      if position != 0:
        tiles.append( Tile(x, y, position) )

def showTiles():
  positionToTiles()
  for tile in tiles:
    tile.createTile()

def moveTiles(course):
  if course == 'Right':
    reverseMatrix()
  elif course == 'Up':
    switchMatrix()
  elif course == 'Down':
    switchMatrix()
    reverseMatrix()

  moveLeft()

  if course == 'Right':
    reverseMatrix()
  elif course == 'Up':
    switchMatrix()
  elif course == 'Down':
    reverseMatrix()
    switchMatrix()

  showTiles()


def switchMatrix():
  global positions
  _array = []
  for i in range(len(positions[0])):
    _array.append( [n[i] for n in positions] )
  positions = _array

def reverseMatrix():
  global positions
  _array = []
  for position_y in positions:
    position_y.reverse()
    _array.append( position_y )
  positions = _array

def moveLeft():
  global positions
  _array = []
  for position_y in positions:
    zero_count = position_y.count(0)
    _array.append( [i for i in position_y if i != 0] + [0 for i in range(zero_count)] )
  positions = _array




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

def operate(event):
  print(event.keysym)
  moveTiles(event.keysym)

def play():
  global canvas
  root, canvas = create_canvas()
  set_field()

  showTiles()

  root.bind("<Key>", lambda event: operate(event))
  root.mainloop()

play()
