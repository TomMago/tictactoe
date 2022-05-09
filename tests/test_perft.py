
import unittest
import pytest
import copy
from tictacslow.board import Board


class GameTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def _perft(self, current_board):
        number_moves = 0
        if not current_board.check_win() == 0:
            return 1
        for move in current_board.move_gen():
            new_board = copy.deepcopy(current_board)
            new_board.make_move(new_board.to_move, tuple(move))
            number_moves += self._perft(new_board)
        return number_moves

    def test_perft(self):
        self.board.reset_board()

        self.board.make_move(2, (0,0))
        self.board.make_move(1, (0,1))
        self.board.make_move(1, (0,2))
        self.board.make_move(1, (1,0))
        self.board.make_move(2, (1,1))
        self.board.make_move(1, (1,2))
        self.board.make_move(2, (2,0))
        self.board.make_move(1, (2,1))
        self.assertEqual(self._perft(self.board), 1)


        self.board.reset_board()

        self.board.make_move(2, (0,0))
        self.board.make_move(1, (0,1))
        self.board.make_move(1, (0,2))
        self.board.make_move(1, (1,0))
        self.board.make_move(2, (1,1))
        self.board.make_move(1, (1,2))
        self.board.make_move(2, (2,0))
        self.assertEqual(self._perft(self.board), 2)

        self.board.reset_board()

        self.board.make_move(2, (0,0))
        self.board.make_move(1, (0,1))
        self.board.make_move(1, (0,2))
        self.board.make_move(1, (1,0))
        self.board.make_move(2, (1,1))
        self.board.make_move(1, (1,2))
        self.assertEqual(self._perft(self.board), 5)
