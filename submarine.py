from ship import Ship
class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine")
        self.size = 3