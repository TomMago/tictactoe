import numpy as np

class Board:

    def __init__(self):
        self.board = np.zeros((3,3)) # 0 free, 1 player 1, 2 player 2
        self.to_move = 1 # player 1


    def check_win(self):
        """Check who wins the game

           Returns:
                int: The winner of the game. 0 the game did not end, 1 if player one wins, 2 if player two wins, 3 if the game is a draw.
        """
        rows_p1 = np.sum(self.board == 1, axis=0) == 3
        columns_p1 = np.sum(self.board == 1, axis=1) == 3
        diagonal1_p1 = np.array([self.board[2,0], self.board[1,1], self.board[0,2]]) == 1
        diagonal2_p1 = np.array([self.board[0,0], self.board[1,1], self.board[2,2]]) == 1


        rows_p2 = np.sum(self.board == 2, axis=0) == 3
        columns_p2 = np.sum(self.board == 2, axis=1) == 3
        diagonal1_p2 = np.array([self.board[2,0], self.board[1,1], self.board[0,2]]) == 2
        diagonal2_p2 = np.array([self.board[0,0], self.board[1,1], self.board[2,2]]) == 2


        if sum(rows_p1) >= 1 or sum(columns_p1) >= 1 or sum(diagonal1_p1) >= 3 or sum(diagonal2_p1) >= 3:
            winner = 1
        elif sum(rows_p2) >= 1 or sum(columns_p2) >= 1 or sum(diagonal1_p2) >= 3 or sum(diagonal2_p2) >= 3:
            winner = 2
        elif np.sum(self.board == 0) == 0:
            winner = 3
        else:
            winner = 0

        return winner

    def make_move(self, player, coordinates):
        """Make a move one the board

           Args:
                player (int): The player to place a move
                coordinates (int, int): Coordinates to place the move
        """
        if not self.get_square(coordinates):
            self.board[coordinates] = player
            self.to_move += (-1)**(self.to_move + 1)
        else:
            print("Square already occupied")

    def get_square(self, coordinates):
        """Get the content of a square

           Args:
                coordinates (int, int): Coordinates to place the move

           Returns:
                int: the content of the square: 0 free, 1 player one, 2 player two
        """
        return self.board[coordinates]

    def print_board(self):
        print("y\\x  0   1   2")
        print("   -------------")
        print("0  |",int(self.board[0,0]), "|", int(self.board[1,0]), "|", int(self.board[2,0]),"|")
        print("   -------------")
        print("1  |",int(self.board[0,1]), "|", int(self.board[1,1]), "|", int(self.board[2,1]),"|")
        print("   -------------")
        print("2  |",int(self.board[0,2]), "|", int(self.board[1,2]), "|", int(self.board[2,2]),"|")
        print("   -------------")

    def reset_board(self):
        self.board = np.zeros((3,3))
        self.to_move = 1

    def move_gen(self):
        moves = np.argwhere(self.board == 0)
        return moves
