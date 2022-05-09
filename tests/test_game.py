
import unittest
import pytest

from tictacslow.board import Board


class GameTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_check_win(self):
        self.board.reset_board()

        self.board.make_move(2, (1,1))
        self.board.make_move(1, (2,1))
        self.board.make_move(2, (0,1))
        self.board.make_move(2, (1,2))
        self.board.make_move(1, (2,2))
        self.board.make_move(1, (0,2))
        self.board.make_move(1, (1,0))
        self.board.make_move(2, (2,0))
        self.board.make_move(1, (0,0))
        self.assertEqual(self.board.check_win(), 3)

        self.board.reset_board()

        self.board.make_move(2, (1,1))
        self.board.make_move(2, (2,1))
        self.board.make_move(2, (0,1))
        self.board.make_move(2, (1,2))
        self.board.make_move(1, (2,2))
        self.board.make_move(1, (0,2))
        self.board.make_move(1, (1,0))
        self.board.make_move(2, (2,0))
        self.board.make_move(1, (0,0))
        self.assertEqual(self.board.check_win(), 2)

        self.board.reset_board()

        self.board.make_move(1, (1,1))
        self.board.make_move(2, (2,1))
        self.board.make_move(2, (0,1))
        self.board.make_move(2, (1,2))
        self.board.make_move(1, (2,2))
        self.board.make_move(1, (0,2))
        self.board.make_move(1, (1,0))
        self.board.make_move(2, (2,0))
        self.board.make_move(1, (0,0))
        self.board.print_board()
        self.assertEqual(self.board.check_win(), 1)

    def test_move_gen(self):
        self.board.reset_board()

        self.board.make_move(2, (0,0))
        self.board.make_move(1, (0,1))
        self.board.make_move(2, (0,2))
        self.board.make_move(2, (1,0))
        self.board.make_move(1, (1,1))
        self.board.make_move(1, (1,2))
        self.board.make_move(1, (2,0))
        self.board.make_move(2, (2,1))
        self.assertEqual(len(self.board.move_gen()), 1)

        self.board.reset_board()

        self.board.make_move(2, (0,0))
        self.board.make_move(2, (1,0))
        self.board.make_move(1, (1,1))
        self.board.make_move(1, (2,0))
        self.board.make_move(2, (2,1))
        self.board.make_move(1, (2,2))
        self.assertEqual(len(self.board.move_gen()), 3)
