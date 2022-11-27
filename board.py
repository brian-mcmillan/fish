import random
from tkinter import *
from tiles import *
from random import randint
from window import *
from click import *


class Board:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.create_board(rows, columns)
        self.tag_hexagon(rows, columns)

    @staticmethod
    def create_hexagon(list_of_points):
        """
        Create a hexagon.
        :param list_of_points: a list of hex coordinates
        :return: hexagon
        """

        hexagon = CANVAS.create_polygon(list_of_points, fill=ICE_COLOR, outline=WATER_COLOR)
        CANVAS.pack()

        hexagons.add(hexagon, list_of_points)
        return hexagon

    @staticmethod
    def tag_hexagon(rows, columns):
        """
        Gives each hexagon a key and value.
        Key -> row x col posn
        Value -> list of points defined when hex was created
        :param rows: amount of rows
        :param columns: amount of cols
        """
        rows = rows - 1
        columns = columns - 1
        key = [-1, -1]
        for value in hexagons.values():
            if key[1] < rows:
                key[1] += 1
            elif key[1] == rows:
                key[1] = 0
            if key[0] < columns and key[1] == 0:
                key[0] += 1
            TILES.add(tuple(key), value)


    def get_rows(self, rows, add_x=0, add_y=0):
        """
        Create hexagon rows
        :param rows: amount of rows
        :param add_x: amount to increment x value by for creation of next hexagon
        :param add_y: amount to increment y value by for creation of next hexagon
        """

        list_of_points = []
        index = 0
        for coordinate in STARTING_COORDINATES:
            if index % 2 != 0:
                coordinate += add_y
            else:
                coordinate += add_x
            index += 1
            list_of_points.append(coordinate)

        self.create_hexagon(list_of_points)

        if rows == 1:
            return
        else:
            self.get_rows(rows - 1, add_x, add_y + 60)



    def get_columns(self, columns, add_x=0, add_y=0):
        """
        Create hexagon columns
        :param columns: amount of cols
        :param add_x: amount to increment x value by for creation of next hexagon
        :param add_y: amount to increment y value by for creation of next hexagon
        """
        accum = 0
        while columns != 1:
            add_x += x_offset
            if accum % 2 == 0:
                add_y += y_offset
            else:
                add_y -= y_offset

            self.get_rows(ROWS, add_x, add_y)
            columns -= 1
            accum += 1
        return


    def create_board(self, rows, columns):
        """
        Create hexagon board
        :param rows: amount of rows
        :param columns: amount of cols
        """
        self.get_rows(rows)
        self.get_columns(columns)
        return

    @staticmethod
    def change_color(list_of_points, fill, outline):
        """Purpose: Change color of hexagon to signify it has been removed
           Contract: list_of_points -> IMG"""
        hexagon = CANVAS.create_polygon(list_of_points, fill=fill, outline=outline)
        CANVAS.pack()

    def remove_tile(self, column, row):
        """Remove a specific tile from the board."""
        cxr = (column, row)
        if tuple(cxr) in TILES:
            self.change_color(TILES[cxr], WATER_COLOR, WATER_COLOR)
            del TILES[cxr]
        else:
            print("That tile does not exist.")

    def remove_random(self, amount):
        """Remove a random amount of tiles."""

        # Get amount of tiles
        tot = (len(TILES))

        # Choose a random tile amount of tiles for removal
        # If same tile is chosen more than once, pick again
        removed_tiles = []
        while amount > 0:
            random_column = random.randint(0, self.columns - 1)
            random_row = random.randint(0, self.rows - 1)
            random_cxr = (random_column, random_row)

            if random_cxr not in removed_tiles:
                removed_tiles.append(random_cxr)
                amount -= 1

        for tile in removed_tiles:
            # Remove the hexagon from the board
            self.change_color(TILES[tile], WATER_COLOR, WATER_COLOR)
            # Delete removed tiles from dictionary
            del TILES[tile]

        return



    # --in progress--# # working but needs more functionality

