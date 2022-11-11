from player import Player
import keyboard
import numpy as np


class Game_board:

    def __init__(self):
        self.player_1 = Player("Player_1")
        self.player_2 = Player("Player_2")
        name = "Game_Board"



    def run_game(self):
        self.display_welcome()
        board_pl_1 = self.show_board(self.player_1, self.player_2)
        board_pl_2 = self.show_board(self.player_2, self.player_1)
        round = 0
        while (np.sum(board_pl_1) > 0 ) and (np.sum(board_pl_1) > 0):
            turn_hits_1 = self.play_turn(self.player_1, self.player_2, board_pl_1)
            board_pl_1 = np.add(board_pl_1, turn_hits_1)

            turn_hits_2 = self.play_turn(self.player_2, self.player_1, board_pl_2)
            board_pl_2 = np.add(board_pl_2, turn_hits_2)

            print(f'Round: {round}')
            round += 1



    def play_turn(self, player_1, player_2, board):
        guess_x = input(f'{player_1.name}: choose your coordinate horizontally (1-20): ')
        guess_x = int(guess_x)
        guess_y = input(f'{player_1.name}: choose your coordinate vertically (1-20): ')     
        guess_y - int(guess_y)
        turn_board = np.empty(21, np.int32)
        if board[guess_x][guess_y] == 1:
            turn_board[guess_x][guess_y] = 1
        return turn_board
        





    def display_welcome(self):
        
        print('''
Welcome to Battleship!!!

Before we get started, let's review the rules. 
Each player will receive a randomized game board with their ships placed in secret locations. 
Players will guess coordinates (x,y), trying to identify the position (horizontal or vertical) of their opponent's ships.

The Destroyer is 2 spaces long.
The Submarine is 3.
The Battleship is 4.
And the Aircraft Carrier is 5.

(Press "enter" to continue.)''')

        keyboard.wait("Return")

        print('''
The first player will make their guess, and if they hit any of the spaces containing an enemy ship, 
that position will change from "0" to "1." Be the first to sink all 4 ships to win!

(Press "enter" to continue.)
''')
        keyboard.wait("Return")



    def display_rules(self):
        print('''
The Destroyer is 2 spaces long.
The Submarine is 3.
The Battleship is 4.
And the Aircraft Carrier is 5.
Sink all four ships to win!''')
      
        


    def show_board(self, player_1, player_2):
        print(f'''{player_1.name}, your board is ready. {player_2.name}, please look away. 
{player_1.name}, press "enter" when you are ready to see your board in secret.''')
        keyboard.wait("Return")
        
        self.player_1.define_board()
        board = self.player_1.create_and_compare_matrices(self.player_1.destroyer, self.player_1.submarine, self.player_1.battleship, self.player_1.aircraft_carrier, self.player_1.board_e)
        print("Press 'enter' when you are ready to continue.")
        keyboard.wait("Return")
        print('''
        
        
        
















        
        ''')
        return board







    def display_winner(self):
        pass 









    def display_current_board(self, player):
        # print(player.current_board)
        pass





    # def display_ships(self, board_c, board_e, player, player_2):
    #     player.define_board()
    #     input(f

        
       
    
    


