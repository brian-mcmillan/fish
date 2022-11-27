import random
from tkinter import *
from tiles import *
from random import randint

# CONSTANTS - (refactor this as stdin/ part of croupier class later on)
ROWS = int(input("Rows: "))
COLUMNS = int(input("Columns: "))

# COLOR PALETTE
WATER_COLOR = '#80b2ff'
ICE_COLOR = '#f4fffe'
WATER2_COLOR = '#062759'

# WINDOW SETTINGS
WINDOW = Tk()
WINDOW.title("Hey, That's my fish!")
WIDTH = COLUMNS * 60 + 30
HEIGHT = ROWS * 60 + 30
WIDTHALT = WIDTH + 75
HEIGHTALT = HEIGHT + 100
WINDOW.geometry("{}x{}".format(WIDTHALT, HEIGHTALT))
WINDOW.config(bg=WATER2_COLOR)

# CANVAS SETTINGS
CANVAS = Canvas(WINDOW, width=WIDTH, height=HEIGHT)
CANVAS.config(bg=WATER_COLOR)

# HEXAGONAL CONSTANTS
HEX_WIDTH = 90
HEX_HEIGHT = 60
y_offset = 30
x_offset = 60
STARTING_COORDINATES = [30, 0, 60, 0, 90, 30, 60, 60, 30, 60, 0, 30]

ACCUM = 0

# INITIALIZE DICTIONARY OF TILES AND DICTIONARY OF TAGS
hexagons = Tiles()
TILES = Tiles()
