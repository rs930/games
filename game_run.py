from tictactoe_2 import *

if __name__ == "__main__":
    p1 = Player('player1', 'X')
    p2 = Player('player2', 'O')
    board = Board(p1,p2)
    # test_pos = [(1,1), (0,1), (1,0), (1,2), (0,2), (2,0), (0,0), (2,2), (2,1)]
    while not board.game_over:
        print(board)
        pos = input(f"Choose position {board.get_curr_player.name}: ")
        pos = tuple(map(int, pos))
        board.put_mark(pos)
        winner = board.check_win()

    if not winner:
        print("It's a draw!!")
    else:
        print("{} won the game!!".format(board.player_info[winner].name))


