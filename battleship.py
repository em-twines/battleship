from ship import Ship
class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship")
        self.size = 4