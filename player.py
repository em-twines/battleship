
from random import randint
from ship import Ship
from destroyer import Destroyer
from submarine import Submarine
from battleship import Battleship
from aircraft_carrier import Aircraft_Carrier

import math
import numpy as np

class Player: 
    def __init__(self, name):
        self.name = name
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.battleship = Battleship()
        self.aircraft_carrier = Aircraft_Carrier()
        self.current_board = []
        self.ship_spaces_remaining = int
        self.board_size = 20

        # self.board_a = np.array
        # self.board_b = np.array
        # self.board_c = np.array
        
        # self.board_d = np.array
        self.board_e = np.array
        # self.board_f = np.array
        # self.board_final = np.array


   
    def define_board(self):
        self.current_board = np.array([
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
        # print(self.current_board)







    def attack(self, list):
        pass






    def place_ships_x(self, ship_instance):
        starting_position_x = randint(1, (self.board_size - ship_instance.size + 1))
        starting_position_y = randint(1, self.board_size)
        
        x_span_until = starting_position_x + ship_instance.size

        for y in range(21):
            for x in range (21):
                # if starting_position_x + x_span_until >= 20:
                #     starting_position_x = 20 - x_span_until
                # if starting_position_x + x_span_until :
                #overlaps with any 1's 
                # then move over until there are no 1's.
                # while self.current_board[y][x] == 0:
                if starting_position_x < x_span_until:
                    if y == starting_position_y and x == starting_position_x:
                        # if self.current_board[y][x] != 0:
                        self.current_board[y][x] = 1
                        starting_position_x += 1
                # else:
                #     self.current_board[y][x] = 0
                            # elif self.current_board[y][x] != 0:
                            #     self.current_board[y][x] = 1
                            #     starting_position_x += 1
    
        return self.current_board

                           
                    



    def place_ships_y(self, ship_instance):
        starting_position_y = randint(1, (self.board_size - ship_instance.size + 1))
        starting_position_x = randint(1, self.board_size)
        
        y_span_until = starting_position_y + ship_instance.size

        for y in range(21):
            for x in range (21):
                # if starting_position_y + y_span_until >= 20:
                #     starting_position_y = 20 - y_span_until
                # while self.current_board[y][x] != 0:
                if starting_position_y < y_span_until:
                    if y == starting_position_y and x == starting_position_x:
                        self.current_board[y][x] = 1
                        starting_position_y += 1
                # else: 
                #     self.current_board[y][x] = 0
                                # while self.current_board[y][x] != 0:
                # self.current_board[y][x] = 1
                # starting_position_y += 1
                                # x+= 1
        return self.current_board
                        
                                    #need to add here logic to account for if the ship will run half over the border.
                                    
                            

                    

    def place_ships(self, ship):
        deciding_int = randint(0, 1)
        if deciding_int == 0:
            result = self.place_ships_x(ship)
            return result
        else: 
            result = self.place_ships_y(ship)
        return result




    def create_and_compare_matrices(self, ship_1, ship_2, ship_3, ship_4, board_e):
        board_e = np.full((21,21), 10, np.int32)
        # np.argwhere(board_e < 2).all == False
        
        while (np.sum(board_e) != 434):
            board_e = np.empty(21)
            board_e = self.place_ships(ship_1)
            board_e = self.place_ships(ship_2)
            board_e = self.place_ships(ship_3)
            board_e = self.place_ships(ship_4)
            if np.sum(board_e) == 434:
                print(board_e)
                return(board_e)
            # first_comparison = np.intersect1d(board_a, board_b, assume_unique = True, return_indices = True)
            
            # board_c = np.add(board_a, board_b)
            # board_f = np.add(board_d, board_e)

            # board_final = np.add(board_c, board_f)
            # board_final_count = np.sum(board_final)
                        
        

        
            # if (board_c).any()>=2:
            #     board_a = self.place_ships(ship_1)
            #     board_b = self.place_ships(ship_2)

            # # second_comparison = np.intersect1d(board_d, board_e, assume_unique = True, return_indices = True)
            # else: 
            
            # if np.any(board_c >= 2):
            #     board_d = self.place_ships(ship_3)
            #     board_e = self.place_ships(ship_4)
            
            
            # final_comparison = np.intersect1d(board_c, board_f, assume_unique = True, return_indices = True)
         
    
        # board_3 = player.place_ships(player.battleship)
        # board_4 = player.place_ships(player.aircraft_carrier)





        # aircraft_carrier_x = randint(0, (20- self.aircraft_carrier.size))
        # battlship_x = randint(0, (20- self.battleship.size))
        # submarine_x = randint(0, (20- self.submarine.size))