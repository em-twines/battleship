from ship import Ship
import numpy as np

class Battleship(Ship):
    def __init__(self):
        self.size = 4
        self.health = 4
        self.location = np.array
        self.new_board = np.zeros((21,21), np.int32)

        super().__init__("Battleship")
