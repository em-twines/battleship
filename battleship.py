from ship import Ship
class Battleship(Ship):
    def __init__(self):
        self.size = 4
        super().__init__("Battleship")
