import numpy as np


class Board:
    PATTERN_RULES = ['h', 'v', 'd1', 'd2']

    def __init__(self, player1, player2):
        self._grid = np.zeros((3, 3))
        self.player_info = {-1: player1,
                            1: player2,
                            0: Player("","")}
        self.curr_player_id = -1
        self.slots_left = 9
        self.game_over = False

    def put_mark(self, pos):
        if self.valid(pos):
            self._grid[pos] = self.curr_player_id
            self.update_turn()
            return True
        else:  # position already occupied
            print("Position already occupied! Please choose some other position")
            return False

    def valid(self, pos):
        return not self._grid[pos]

    def check_win(self):
        win = 0  # no winner
        for r in self.PATTERN_RULES:
            win = self.rule(r)
            if win != 0:
                self.game_over = True
                break
        if self.slots_left == 0:
            print("slots zero")
            self.game_over = True
        return win

    def draw(self):
        """
        checks positions with no player
        :return:
        """
        return (self._grid == 0).sum() > 0

    def rule(self, direction='h'):
        """
        :return: player id who won, 0 imply no win
        """
        axis = {'h': 1,
                'v': 0,
                'd1': None,
                'd2': None}
        grid = self._grid
        if direction == 'd1':
            grid = grid * np.eye(grid.shape[0])
        elif direction == 'd2':
            grid = grid * np.flip(np.eye(grid.shape[0]), axis=1)
        total = np.sum(grid, axis=axis[direction], keepdims=True)/3
        if 1 in total:
            return 1
        elif -1 in total:
            return -1
        else:
            return 0

    def update_turn(self):
        self.curr_player_id = self.curr_player_id*-1
        self.slots_left -= 1

    def __repr__(self):
        out = np.array([[""]*3]*3)
        for i in range(3):
            for j in range(3):
                out[i,j] = self.player_info.get(self._grid[i,j]).mark
        return f'{out}'

    @property
    def get_curr_player(self):
        return self.player_info[self.curr_player_id]


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
