from game_board import Game_board

#temp
from player import Player
player_1 = Player("Player 1")
player_2 = Player("Player 2")

game_board = Game_board()

game_board.run_game(player_1, player_2)

