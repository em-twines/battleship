
from ship import Ship
from destroyer import Destroyer
from submarine import Submarine
from battleship import Battleship
from aircraft_carrier import Aircraft_Carrier

import numpy as np
large_width = 400
np.set_printoptions(linewidth=large_width)

class Player: 
    def __init__(self, name):
        self.name = name
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.battleship = Battleship()
        self.aircraft_carrier = Aircraft_Carrier()
        self.ship = Ship("Ship")
        self.current_board = []
        self.ship_spaces_remaining = int
        self.board_size = 20

        self.board_e = np.array
  
    


    def create_and_compare_matrices(self):
        board_e = np.full((21,21), np.float16)
   
        while (np.count_nonzero(board_e == 4) != 2) or (np.count_nonzero(board_e == 2)) != 16:
            board_a = np.zeros((21,21), np.float16)
            board_b = np.zeros((21,21), np.float16)
            board_c = np.zeros((21,21), np.float16)
            board_d = np.zeros((21,21), np.float16)
            board_e = np.zeros((21,21), np.float16)
            board_f = np.zeros((21,21), np.float16)
            board_g = np.zeros((21,21), np.float16)
            board_a = self.destroyer.place_ships()
            board_b = self.submarine.place_ships()
            board_c = self.battleship.place_ships()
            board_d = self.aircraft_carrier.place_ships()
            board_g = np.add(board_a, board_b)
            board_f = np.add(board_c, board_d)
            board_e = np.add(board_g, board_f)

        
        print(board_e)
        return(board_e)
            


