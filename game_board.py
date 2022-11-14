import keyboard
import numpy as np
import time
from player import Player


class Game_board:

    def __init__(self):
        # self.player_1 = Player("Player_1")
        # self.player_2 = Player("Player_2")
        name = "Game Board"




    def run_game(self, player_1, player_2):

        self.display_welcome()
        player_1_board = self.show_board(player_1, player_2)
        player_2_board = self.show_board(player_2, player_1)
        round = 0
        turn_hits_1 = self.create_blank_board()
        turn_hits_2 = self.create_blank_board()
       
        while (player_1.destroyer.health or player_1.submarine.health or player_1.battleship.health or player_1.aircraft_carrier.health > 0) and (player_2.destroyer.health or player_2.submarine.health or player_2.battleship.health or player_2.aircraft_carrier.health > 0):

            round += 1
            print(f'Round: {round}')

            #turn_hits_2 = opponent's board as known to player
            turn_hits_1 = self.play_turn(player_1, player_2, turn_hits_1, player_2_board)
            turn_hits_2 = self.play_turn(player_2, player_1, turn_hits_2, player_1_board)

           

        if (player_1.destroyer.health and player_1.submarine.health and player_1.battleship.health and player_1.aircraft_carrier.health) <= 0:
            print(f'{player_2.name} is the winner! Thanks to both our players today and congratulations to {player_2.name}')
        elif (player_2.destroyer.health and player_2.submarine.health and player_2.battleship.health and player_2.aircraft_carrier.health) <= 0:
            print(f'{player_1.name} is the winner! Thanks to both our players today and congratulations to {player_1.name}')
        else:
            print("It's a tie! Thanks for playing!")






    def play_turn(self, player_1, player_2, turn_hits_1, player_2_board):
                       
            print(f'''Here is your opponent's board, as you know it, {player_1.name}: 
{turn_hits_1}:''')
            turn_hits_to_add_1, guess_y, guess_x = self.input_and_eval_guess(player_1, player_2_board)
           
            if turn_hits_to_add_1[guess_y][guess_x] == turn_hits_1[guess_y][guess_x]:
                turn_hits_to_add_1[guess_y][guess_x] = 0
            elif turn_hits_to_add_1[guess_y][guess_x] == turn_hits_1[guess_y][guess_x]:
                turn_hits_to_add_1[guess_y][guess_x] = 0
           
            # if (1 == (np.nonzero(turn_hits_to_add_1)[0])) and (turn_hits_1[guess_y][guess_x] == 1):
            #     turn_hits_to_add_1[guess_y][guess_x] = 0
            # elif (2 == np.nonzero(turn_hits_to_add_1)[0]) and (turn_hits_1[guess_y][guess_x] == 2):
            #     turn_hits_to_add_1[guess_y][guess_x] = 0
            else: 
                turn_hits_1 = np.add(turn_hits_1, turn_hits_to_add_1)
                if player_2.destroyer.new_board[guess_y][guess_x] == 2:
                    self.take_damage(player_1, player_2, player_2.destroyer)
                elif player_2.submarine.new_board[guess_y][guess_x] == 2:
                    self.take_damage(player_1, player_2, player_2.submarine)
                elif player_2.battleship.new_board[guess_y][guess_x] == 2:
                    self.take_damage(player_1, player_2, player_2.battleship)
                elif player_2.aircraft_carrier.new_board[guess_y][guess_x] == 2:
                    self.take_damage(player_1, player_2, player_2.aircraft_carrier)

            return turn_hits_1
#             print(f'''Here is your opponent's board, as you know it, {self.player_2.name}: 
# {turn_hits_2}:''')





            # turn_hits_to_add_2, guess_y, guess_x = self.input_guess(self.player_2, board_pl_1)  

            #  ######can likely combine with or statement######
            # if (1 == np.nonzero(turn_hits_to_add_2)[0]) and (turn_hits_2[guess_y][guess_x] == 1):
            #     turn_hits_to_add_2[guess_y][guess_x] = 0
            # elif (2 == np.nonzero(turn_hits_to_add_2)[0]) and (turn_hits_2[guess_y][guess_x] == 2):
            #     turn_hits_to_add_2[guess_y][guess_x] = 0
            # else:
            #     turn_hits_2 = np.add(turn_hits_2, turn_hits_to_add_2)
                
    




    def input_and_eval_guess(self, player_1, player_2_board):
        working = False
        while working == False:
            guess_x = input(f'{player_1.name}: choose your coordinate horizontally (1-20), then press "enter":')
            try:
                guess_x = int(guess_x)
            except ValueError:
                print("Oops! I didn't understand that guess!")
                continue
            guess_y = input(f'{player_1.name}: choose your coordinate vertically (1-20), then press "enter":')     
            try:
                guess_y = int(guess_y)
            except ValueError:
                print("Oops! I didn't understand that guess!")
                continue
            turn_board = np.zeros((21,21),np.int32)
            if player_2_board[guess_y][guess_x] == 2:
                turn_board[guess_y][guess_x] = 2
                
            else: 
                turn_board[guess_y][guess_x] = 1
                print("It's a miss!")
                time.sleep(1)
            working = True
            return turn_board, guess_y, guess_x
            

    def take_damage(self, player_1, player_2, ship):
        # damage_matrix, guess_x, guess_y = self.input_guess()
                
        # if self.player_1.destroyer.new_board[guess_y][guess_x] == 2:

        if ship.health > 0:
            print("It's a hit!")
            time.sleep(1)
            ship.health -= 1
            print(f"{player_2.name}'s {ship.name} now has {ship.health} health left!")
            time.sleep(1)
            if ship.health == 0:
                print(f"{player_1.name} sank your {ship.name}!")

        # elif self.player_1.submarine.new_board[guess_y][guess_x] == 2:
        #     if self.player_1.submarine.health > 0:
        #         self.player_1.submarine.health -= 1
        #         print(f"{self.player_2.name}'s {self.player_1.submarine.name} now has {self.player_1.submarine.health} health left!")
        #         time.sleep(1)
        #         if self.player_1.submarine.health == 0:
        #             print(f"{self.player_2.name} sank your {self.player_1.submarine.name}!")
        #     else: print("Splash! It's already sunk!")

        # elif self.player_1.battleship.new_board[guess_y][guess_x] == 2:
        #     if self.player_1.battleship.health > 0:
        #         self.player_1.battleship.health -= 1
        #         print(f"{self.player_2.name}'s  {self.player_1.battleship.name} now has {self.player_1.battleship.health} health left!")
        #         time.sleep(1)
        #         if self.player_1.battleship.health == 0:
        #             print(f"{self.player_2.name} sank your {self.player_1.battleship.name}!")
        #     else: 
        #         print("Splash! It's already sunk!")

        # elif self.player_1.aircraft_carrier.new_board[guess_y][guess_x] == 2:
        #     if self.player_1.aircraft_carrier.health > 0:
        #         self.player_1.aircraft_carrier.health -= 1
        #         print(f"{self.player_2.name}'s  {self.player_1.aircraft_carrier.name} now has {self.player_1.aircraft_carrier.health} health left!")
        #         time.sleep(1)
        #         if self.player_1.aircraft_carrier.health == 0:
        #             print(f"{self.player_2.name} sank your {self.player_1.aircraft_carrier.name}!")
        #     else: 
        #         print("Splash! It's already sunk!")
        time.sleep(1)



        



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
        
        board = player_1.create_and_compare_matrices()
        print('Press "space" when you are ready to continue.')
        keyboard.wait("Space")
        print('''
        
        
        




        
















        
        ''')
        return board








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




    


