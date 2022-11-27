from window import *
from board import *


class Movement:

    def __init__(self, start_c, start_r, end_c, end_r):
        self.start_posn = [start_c, start_r]
        self.end_posn = [end_c, end_r]
        self.cols_to_move = abs(self.end_posn[0] - self.start_posn[0])
        self.spaces_to_move = abs(self.end_posn[1] - self.start_posn[1])
        self.start_column = start_c
        self.start_row = start_r
        self.end_column = end_c
        self.end_row = end_r
        self.current_column = start_c

    def same_column(self):
        if self.start_column == self.end_column:
            return True
        else:
            return False

    def odd_column(self):
        if self.current_column % 2 != 0:
            return True
        return False

    def even_column(self):
        if self.current_column % 2 == 0:
            return True
        return False

    def same_row(self):
        if self.start_posn[1] == self.end_posn[1]:
            return True
        else:
            return False

    def same_position(self):
        if self.start_posn == self.end_posn:
            return True

    def does_start_posn_exist(self):
        for tile in TILES:
            if tile == tuple(self.start_posn):
                return True
            else:
                return False

    def does_end_posn_exist(self):
        for tile in TILES:
            if tile == tuple(self.end_posn):
                return True
            else:
                return False

    def pos_col_pos_row(self):
        # ++
        # POSITIVE COLUMN MOVEMENT (LEFT TO RIGHT), POSITIVE ROW MOVEMENT (UP TO DOWN)
        # IF EVEN ROW: HEX SUCCEEDED BY (+1 COL, +0 ROW) UNTIL IT REACHES TARGET DESTINATION
        # IF ODD ROW: HEX SUCCEEDED BY (+1 COL, +1 ROW) UNTIL IT REACHES TARGET DESTINATION
        if self.start_column < self.end_column and self.start_row < self.end_row:
            if self.current_column % 2 == 0:
                self.start_posn[0] += 1
                self.start_posn[1] += 0
            if self.current_column % 2 != 0:
                self.start_posn[0] += 1
                self.start_posn[1] += 1
            self.current_column += 1

    def pos_col_min_row(self):
        # +-
        # POSITIVE COLUMN MOVEMENT (LEFT TO RIGHT), NEGATIVE ROW MOVEMENT (DOWN TO UP)
        # IF EVEN ROW: HEX SUCCEEDED BY (+1 COL, -1 ROW) UNTIL IT REACHES TARGET DESTINATION
        # IF ODD ROW: HEX SUCCEEDED BY (+1 COL,  +0 ROW) UNTIL IT REACHES TARGET DESTINATION
        if self.start_column < self.end_column and self.start_row > self.end_row:
            if self.current_column % 2 == 0:
                self.start_posn[0] += 1
                self.start_posn[1] -= 1
            if self.current_column % 2 != 0:
                self.start_posn[0] += 1
                self.start_posn[1] += 0
            self.current_column += 1

    def min_col_pos_row(self):
        # -+
        # NEGATIVE COLUMN MOVEMENT (RIGHT TO LEFT), POSITIVE ROW MOVEMENT (UP TO DOWN)
        # IF EVEN ROW: HEX SUCCEEDED BY (-1 COL, -0 ROW) UNTIL IT REACHES TARGET DESTINATION
        # IF ODD ROW: HEX SUCCEEDED BY (-1 COL, +1 ROW) UNTIL IT REACHES TARGET DESTINATION
        if self.start_column > self.end_column and self.start_row < self.end_row:
            if self.current_column % 2 == 0:
                self.start_posn[0] -= 1
                self.start_posn[1] -= 0
            if self.current_column % 2 != 0:
                self.start_posn[0] -= 1
                self.start_posn[1] += 1
            self.current_column += 1

    def min_col_min_row(self):
        # --
        # NEGATIVE COLUMN MOVEMENT (RIGHT TO LEFT), NEGATIVE ROW MOVEMENT (DOWN TO UP)
        # IF EVEN ROW: HEX SUCCEEDED BY (-1 COL, -1 ROW) UNTIL IT REACHES TARGET DESTINATION
        # IF ODD ROW: HEX SUCCEEDED BY (-1 COL, -0 ROW) UNTIL IT REACHES TARGET DESTINATION
        if self.start_column > self.end_column and self.start_row > self.end_row:
            if self.current_column % 2 == 0:
                self.start_posn[0] -= 1
                self.start_posn[1] -= 1
            if self.current_column % 2 != 0:
                self.start_posn[0] -= 1
                self.start_posn[1] -= 0
            self.current_column += 1

    def one_space_diagonal(self):
        """Cover cases of a one space diagonal movement"""
        if self.start_column < self.end_column and self.start_row == self.end_row:
            self.start_posn[0] += 1
        if self.start_column > self.end_column and self.start_row == self.end_row:
            self.start_posn[0] -= 1
        if self.start_column < self.end_column and self.start_row != self.end_row:
            self.start_posn[0] += 1
            self.start_posn[1] -= 1
        if self.start_column > self.end_column and self.start_row != self.end_row:
            self.start_posn[0] -= 1
            self.start_posn[1] -= 1

    def move_vertical(self):
        """Checks to see if vertical movement is valid."""

        if self.same_column():
            for i in range(0, self.spaces_to_move + 1):  # range is not inclusive, so add 1
                for tile in TILES:
                    if tile == tuple(self.start_posn):
                        if self.same_position():
                            print('true')
                            return True
                        if self.end_posn[1] > self.start_posn[1]:
                            self.start_posn[1] += 1
                        if self.end_posn[1] < self.start_posn[1]:
                            self.start_posn[1] -= 1

        return False

    def move_diagonal(self):
        """Checks if a diagonal movement is valid."""

        # LAYOUT OF BOARD ASSUMES AN "ODD-Q" STYLE, WHERE COLUMNS FORM STRAIGHT LINES DOWN AND ARE OFFSET IF ODD
        if not self.same_column():
            for i in range(0, self.cols_to_move+1):
                for tile in TILES:
                    if tile == tuple(self.start_posn):
                        if self.same_position():
                            return True
                        if self.cols_to_move == 1:
                            self.one_space_diagonal()
                        if self.cols_to_move > 1:
                            #++
                            self.pos_col_pos_row()
                            #+-
                            self.pos_col_min_row()
                            #-+
                            self.min_col_pos_row()
                            #--
                            self.min_col_min_row()
        return False















