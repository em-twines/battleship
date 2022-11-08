from ship import Ship
class Submarine(Ship):
    def __init__(self):
        self.size = 3
        super().__init__("Submarine")

