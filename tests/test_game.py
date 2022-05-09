
import unittest
import pytest

from tictacslow.game import Game


class GameTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_check_win(self):
        self.game.make_move(2, (1,1))
        self.game.make_move(1, (2,1))
        self.game.make_move(2, (0,1))
        self.game.make_move(2, (1,2))
        self.game.make_move(1, (2,2))
        self.game.make_move(1, (0,2))
        self.game.make_move(1, (1,0))
        self.game.make_move(2, (2,0))
        self.game.make_move(1, (0,0))
        self.assertEqual(self.game.check_win(), 3)

        self.game.reset_board()

        self.game.make_move(2, (1,1))
        self.game.make_move(2, (2,1))
        self.game.make_move(2, (0,1))
        self.game.make_move(2, (1,2))
        self.game.make_move(1, (2,2))
        self.game.make_move(1, (0,2))
        self.game.make_move(1, (1,0))
        self.game.make_move(2, (2,0))
        self.game.make_move(1, (0,0))
        self.assertEqual(self.game.check_win(), 2)

        self.game.reset_board()

        self.game.make_move(1, (1,1))
        self.game.make_move(2, (2,1))
        self.game.make_move(2, (0,1))
        self.game.make_move(2, (1,2))
        self.game.make_move(1, (2,2))
        self.game.make_move(1, (0,2))
        self.game.make_move(1, (1,0))
        self.game.make_move(2, (2,0))
        self.game.make_move(1, (0,0))
        self.game.print_board()
        self.assertEqual(self.game.check_win(), 1)
