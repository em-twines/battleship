from game_board import Game_board

#temp
from player import Player
player_1 = Player("Player 1")
player_2 = Player("Player 2")

game_board = Game_board()

game_board.run_game()



# next steps: 
    # Get player input of coordinates to attack.
    # learn how to compare matrices. Blank(b) against player board (a).
    # if location chosen == 1 in matrix a, show that position as 1 in matrix b.
    # learn how to aggregate 1's in matrix. if matrix b aggregate == 9, then player wins.
