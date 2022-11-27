import unittest

from board import *
from movement import *


class Tests(unittest.TestCase):

    # Each test holds a board with a different layout/ structure
    # Movements are tested on each board and take missing tiles into account

    def test_1(self):

        # Testing for movements on a board that has no missing tiles.

        board = Board(10, 10)


        # EXAMPLE IMAGE FOR COORDINATE SYSTEM - refer to "ODD-Q VERTICAL LAYOUT"
        # https://www.redblobgames.com/grids/hexagons/

        # VALIDATE MOVEMENT WITH NO MISSING TILES

        a = Movement(0, 0, 1, 0)
        b = Movement(3, 0, 6, 2)
        c = Movement(6, 1, 5, 1)
        d = Movement(5, 3, 1, 5)
        e = Movement(0, 3, 1, 2)
        f = Movement(3, 5, 6, 4)
        g = Movement(2, 2, 1, 1)
        h = Movement(3, 4, 1, 3)

        self.assertTrue(a.move_diagonal())
        self.assertTrue(b.move_diagonal())
        self.assertTrue(c.move_diagonal())
        self.assertTrue(d.move_diagonal())
        self.assertTrue(e.move_diagonal())
        self.assertTrue(f.move_diagonal())
        self.assertTrue(g.move_diagonal())
        self.assertTrue(h.move_diagonal())

        i = Movement(1, 1, 1, 2)
        j = Movement(4, 1, 5, 4)
        k = Movement(3, 3, 1, 1)
        m = Movement(7, 5, 7, 2)
        n = Movement(4, 0, 0, 4)

        self.assertFalse(i.move_diagonal())
        self.assertFalse(j.move_diagonal())
        self.assertFalse(k.move_diagonal())
        self.assertFalse(m.move_diagonal())
        self.assertFalse(n.move_diagonal())

        o = Movement(0, 0, 0, 1)
        p = Movement(2, 1, 2, 5)
        q = Movement(7, 4, 7, 3)
        r = Movement(4, 4, 4, 0)

        self.assertTrue(o.move_vertical())
        self.assertTrue(p.move_vertical())
        self.assertTrue(q.move_vertical())
        self.assertTrue(r.move_vertical())

        self.assertFalse(a.move_vertical())
        self.assertFalse(b.move_vertical())
        self.assertFalse(c.move_vertical())

        s = Movement(0, 0, 0, 11)
        t = Movement(15, 4, 15, 2)

        self.assertFalse(s.move_vertical())
        self.assertFalse(t.move_vertical())

        u = Movement(0, 0, 13, 3)
        v = Movement(7, 5, 20, 8)

        self.assertFalse(u.move_diagonal())
        self.assertFalse(v.move_diagonal())

        # ALL TESTS PASS.


    def test_2(self):
        # Tests movements on a board with some missing tiles
        board = Board(8, 6)

        board.remove_tile(3, 2)
        a = Movement(3, 1, 3, 3)
        self.assertFalse(a.move_diagonal())
        self.assertFalse(a.move_vertical())

        board.remove_tile(7, 2)
        b = Movement(1, 5, 6, 3)
        self.assertTrue(b.move_diagonal())
        self.assertFalse(b.move_vertical())

        board.remove_tile(6, 3)
        self.assertFalse(b.move_diagonal())
        self.assertFalse(b.move_vertical())

        board.remove_tile(1, 4)
        c = Movement(2, 4, 6, 2)
        self.assertTrue(c.move_diagonal())
        self.assertFalse(c.move_vertical())


if __name__ == '__main__':
    unittest.main()
