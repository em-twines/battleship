from ship import Ship
class Aircraft_Carrier(Ship):
    def __init__(self):
        self.size = 5
        super().__init__("Aircraft Carrier")


