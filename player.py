
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
        # get x-direction starting position
        starting_position_x = randint(1, (self.board_size - ship_instance.size + 1))
        starting_position_y = randint(1, self.board_size)

        
        # gives coordinate to start changing if changing on x axis: 
        # coordinate_to_begin = self.current_board[starting_position_y][starting_position_y]
        x_span_until = starting_position_x + ship_instance.size
        # self.current_board[starting_position_y [starting_position_x: x_span_until]] = 1


        # x = 0
        # while x < starting_position_x:
        #     np.put(self.current_board,(starting_position_y, x), 0)
        #     x += 1
        # while starting_position_x < x_span_until:
            # new_array = print(self.current_board[[starting_position_y, starting_position_x]])
            # [self.current_board[starting_position_y, starting_position_x] = np.array([starting_position_y, starting_position_x])
            # np.put(self.current_board, [starting_position_y, starting_position_x], [0, 1])
        for y in range(21):
            for x in range (21):
                if starting_position_x < x_span_until:
                    if y == starting_position_y and x == starting_position_x:
                            self.current_board[y][x] = 1
                            starting_position_x += 1
                    

                
            # if y > 0:
            #     if y == starting_position_y:
            #         self.current_board[y] = 1 
            #     else: 
            #         y == 0           
            # for x in range(21):
            #     while 1 < x < starting_position_x:
            #         self.current_board[x] = 0
            #         x += 1
            #     while starting_position_x <= x <= x_span_until:
            #         self.current_board[x] = 1
            #         x += 1
            # np.put(self.current_board, [starting_position_y, starting_position_x], 1)
            # starting_position_x += 1
        # while starting_position_x <= self.board_size:
        #     np.put(new_array,(starting_position_y, x), 0)
        #     starting_position_x += 1


        print(self.current_board)






    def place_ships(self):
        deciding_int = randint(0, 1)
        if deciding_int == 0:
            self.place_ships_x()
        else: 
            self.place_ships_y()







        # aircraft_carrier_x = randint(0, (20- self.aircraft_carrier.size))
        # battlship_x = randint(0, (20- self.battleship.size))
        # submarine_x = randint(0, (20- self.submarine.size))