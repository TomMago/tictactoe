
from board import Board
from engine import Engine
import numpy as np

class Game:

    def __init__(self):
        self.board = Board()
        self.use_engine = 2 # 0: no engine, 1: engine player one, 2: engine player two
        self.engine = Engine(self.use_engine)



    def play_game(self):
        self.board.print_board()
        while not self.board.check_win():
            print("Player ", self.board.to_move, " enter a move:")
            if self.board.to_move == self.use_engine:
                print("Engine calculating ...")
                self.engine.negamax(self.board,True, 1)
                coordinates = tuple(self.engine.best_move)
            else:
                coordinates = input("x y: ")
                coordinates = np.array(coordinates.split()).astype(np.int64)
            self.board.make_move(self.board.to_move, (coordinates[0], coordinates[1]))
            self.board.print_board()
        if self.board.check_win() == 1:
            print("Player 1 wins!")
        elif self.board.check_win() == 2:
            print("Player 2 wins!")
        elif self.board.check_win() == 3:
            print("Draw!")

g = Game()
g.play_game()
