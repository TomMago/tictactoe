import copy

class Engine:
    def __init__(self, player):
        self.best_move = None
        self.player = player

    def negamax(self, game, first_call, color):
        result = game.check_win()
        if result:
            if result == 3:
                value = 0
            elif result == self.player + (-1)**(self.player + 1):
                value = -1 * color
            elif result == self.player:
                value = 1 * color
            return value

        value = -999999
        for move in game.move_gen():
            child = copy.deepcopy(game)
            child.make_move(child.to_move, tuple(move))
            current_value = -self.negamax(child, False, -color)
            if current_value > value:
                value = current_value
                if first_call:
                    self.best_move = move
        return value
