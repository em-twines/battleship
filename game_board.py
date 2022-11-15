import keyboard
import numpy as np
import time


class Game_board:

    def __init__(self):
        name = "Game Board"


    def run_game(self, player_1, player_2):
        self.display_welcome()
        player_1_board = self.show_board(player_1, player_2)
        player_2_board = self.show_board(player_2, player_1)
        round = 0
        turn_hits_1 = self.create_blank_board()
        turn_hits_2 = self.create_blank_board()
       
        while (player_1.health) and (player_2.health > 0):

            round += 1
            print(f'''
            
Round: {round}''')

            turn_hits_1 = self.play_turn(player_1, player_2, turn_hits_1, player_2_board)
            turn_hits_2 = self.play_turn(player_2, player_1, turn_hits_2, player_1_board)

           
        if (player_1.health) <= 0:
            print(f'{player_2.name} is the winner! Thanks to both our players today and congratulations to {player_2.name}!')
        elif (player_2.health) <= 0:
            print(f'{player_1.name} is the winner! Thanks to both our players today and congratulations to {player_1.name}!')
        else:
            print("It's a tie! Thanks for playing!")










    def play_turn(self, player_1, player_2, turn_hits_1, player_2_board):
                       
            print(f'''Here is your opponent's board, as you know it, {player_1.name}: 
{turn_hits_1}:''')
            turn_hits_to_add_1, guess_y, guess_x = self.input_and_eval_guess(player_1, player_2_board)
           
            if turn_hits_to_add_1[guess_y][guess_x] == turn_hits_1[guess_y][guess_x]:
                turn_hits_to_add_1[guess_y][guess_x] = 0
                print(f'{player_2.name} has {player_2.health} left!')
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
            time.sleep(1)
            return turn_hits_1   
           






    def input_and_eval_guess(self, player_1, player_2_board):
        working = False
        while working == False:
            guess_x = input(f'{player_1.name}: choose your coordinate horizontally (1-20), then press "enter":')
            try:
                guess_x = int(guess_x)
            except ValueError:
                print("Oops! I didn't understand that guess!")
                continue
            if 0 <= guess_x <= 21:
                pass
            else: 
                print("Oops! I didn't understand that guess!")
                continue

            guess_y = input(f'{player_1.name}: choose your coordinate vertically (1-20), then press "enter":')     
            try:
                guess_y = int(guess_y)
            except ValueError:
                print("Oops! I didn't understand that guess!")
                continue
            if 0 <= guess_y <= 21:
                pass
            else: 
                print("Oops! I didn't understand that guess!")
                continue
            turn_board = np.zeros((21,21),np.int32)
            if player_2_board[guess_y][guess_x] == 2:
                turn_board[guess_y][guess_x] = 2
                
            else: 
                turn_board[guess_y][guess_x] = 1
                print("It's a miss!")
            working = True
            return turn_board, guess_y, guess_x
            







    def take_damage(self, player_1, player_2, ship):
      
        if ship.health > 0:
            print("It's a hit!")
            time.sleep(1)
            ship.health -= 1
            player_2.health -= 1
            print(f"{player_2.name}'s {ship.name} now has {ship.health} health left!")
            
            time.sleep(1)
            if ship.health == 0:
                print(f"{player_1.name} sank your {ship.name}!")
            print(f'{player_2.name} has {player_2.health} health left!')
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
that position will change from "0" to "2." If they miss, that position will change to a "1." Be the first to sink all 4 ships to win!

(Press "space" to continue.)
''')
        keyboard.wait("Space")






    def display_rules(self):
        print('''
The Destroyer is 2 spaces long.
The Submarine is 3 spaces long.
The Battleship is 4 spaces long.
And the Aircraft Carrier is 5 spaces long.
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
        [20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype = np.int32)
        return board




    


