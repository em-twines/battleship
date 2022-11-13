from ship import Ship
import numpy as np

class Aircraft_Carrier(Ship):
    def __init__(self):
        self.size = 5
        self.health = 5
        self.location = np.array
        self.new_board = np.zeros((21,21), np.int32)

        super().__init__("Aircraft Carrier")

        

