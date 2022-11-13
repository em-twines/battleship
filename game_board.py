import keyboard
import numpy as np

from player import Player


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
        turn_hits_1 = self.create_blank_board()
        turn_hits_2 = self.create_blank_board()
        # turn_hits_1 = np.zeros((21,21),np.int32)
        # turn_hits_2 = np.zeros((21,21),np.int32)
        place_holder = True
        while place_holder == True:
        # while (np.sum(turn_hits_1) < 434 ) and (np.sum(turn_hits_2) < 434):
            round += 1
            print(f'Round: {round}')
            
            
            print(f'''Here is your opponent's board, as you know it, {self.player_1.name}: 
{turn_hits_1}:''')
            turn_hits_to_add_1 = self.play_turn(self.player_1, board_pl_2)   
            turn_hits_1 = np.add(turn_hits_1, turn_hits_to_add_1)

            
            print(f'''Here is your opponent's board, as you know it, {self.player_2.name}: 
{turn_hits_2}:''')
            turn_hits_to_add_2 = self.play_turn(self.player_2, board_pl_1)   

                 
            # if turn_hits_to_add_2.all != 0:
            #     self.take_damage(self.player_2.destroyer, turn_hits_to_add_2)
            #     self.take_damage(self.player_2.submarine, turn_hits_to_add_2)
            #     self.take_damage(self.player_2.battleship, turn_hits_to_add_2)
            #     self.take_damage(self.player_2.aircraft_carrier, turn_hits_to_add_2)
            turn_hits_2 = np.add(turn_hits_2, turn_hits_to_add_2)
           


# , ship_1, ship_2, ship_3, ship_4
    def play_turn(self, player_1, board):
        guess_x = input(f'{player_1.name}: choose your coordinate horizontally (1-20), then press "enter":')
        guess_x = int(guess_x)
        guess_y = input(f'{player_1.name}: choose your coordinate vertically (1-20), then press "enter":')     
        guess_y = int(guess_y)
        turn_board = np.zeros((21,21),np.int32)
        if board[guess_y][guess_x] == 2:
            turn_board[guess_y][guess_x] = 2
            # ship_1_location = ship_1.location
            # ship_2_location = ship_2.location
            # ship_3_location = ship_3.location
            # ship_4_location = ship_4.location
            
            if self.player_1.destroyer.board[guess_y][guess_x] == 2:
            # # on_board = np.argwhere(self.player_1.destroyer.board == 2)        
            # [guess_y, guess_x] in on_board
            # if [guess_y, guess_x] in on_board:
                self.player_1.destroyer.health -= 1
                print(f'Your {self.player_1.destroyer.name} now has {self.player_1.destroyer.health} health left!')

            elif self.player_1.submarine.board[guess_x][guess_y] == 1:
                self.player_1.submarine.health -= 1
                print(f'Your {self.player_1.submarine.name} now has {self.player_1.submarine.health} health left!')

            elif self.player_1.battleship.board[guess_x][guess_y] == 1:
                self.player_1.battleship.health -= 1
                print(f'Your {self.player_1.battleship.name} now has {self.player_1.battleship.health} health left!')
            
            elif self.player_1.aircraft_carrier.board[guess_x][guess_y] == 1:
                self.player_1.aircraft_carrier.health -= 1
                print(f'Your {self.player_1.aircraft_carrier.name} now has {self.player_1.aircraft_carrier.health} health left!')

            print("It's a hit!")
        else: 
            print("It's a miss!")
        return turn_board
        

        


    # def take_damage(self, ship, hits_board, guess_x, guess_y):
    #     # hits_board = hits_board.flatten() 
    #     # ship_location = ship.location
    #     # ship_location = ship_location.flatten()
    #     # hits_board_non_zero = np.nonzero(hits_board) 
    #     # connection = hits_board_non_zero[0]
    #     # if ship_location[connection] == 2:
    #     if ship.location[guess_x][guess_y] == 1
    #         ship.health -= 1
    #         print(f'Your {ship.name} now has {ship.health} health left!')



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

(Press "space" to continue.)''')

        keyboard.wait("Space")

        print('''
The first player will make their guess, and if they hit any of the spaces containing an enemy ship, 
that position will change from "0" to "1." Be the first to sink all 4 ships to win!

(Press "space" to continue.)
''')
        keyboard.wait("Space")



    def display_rules(self):
        print('''
The Destroyer is 2 spaces long.
The Submarine is 3.
The Battleship is 4.
And the Aircraft Carrier is 5.
Sink all four ships to win!''')
      
        


    def show_board(self, player_1, player_2):
        print(f'''{player_1.name}, your board is ready. {player_2.name}, please look away. 
{player_1.name}, press "space" when you are ready to see your board in secret.''')
        keyboard.wait("Space")
        
        # self.player_1.define_board()
        board = self.player_1.create_and_compare_matrices()
        print('Press "space" when you are ready to continue.')
        keyboard.wait("Space")
        print('''
        
        
        
















        
        ''')
        return board







    def display_winner(self):
        pass 









    def create_blank_board(self):
        board = np.array([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype = np.float16)
        return board




    # def display_ships(self, board_c, board_e, player, player_2):
    #     player.define_board()
    #     input(f

        
       
    
    


