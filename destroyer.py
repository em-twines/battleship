from ship import Ship
class Destroyer(Ship):
    def __init__(self):
        self.size = 2
        super().__init__("Destroyer")
