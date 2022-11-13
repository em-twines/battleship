from ship import Ship
import numpy as np

class Destroyer(Ship):
    def __init__(self):
        self.size = 2
        self.health = 2
        self.location = np.array        
        self.new_board = np.zeros((21,21), np.int32)


        super().__init__("Destroyer")
