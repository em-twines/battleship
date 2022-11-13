from ship import Ship
import numpy as np

class Submarine(Ship):
    def __init__(self):
        self.size = 3
        self.health = 3
        self.location = np.array
        self.new_board = np.zeros((21,21), np.int32)

        super().__init__("Submarine")

