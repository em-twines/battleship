from ship import Ship

class Player: 
    def __init__(self, name):
        self.name = name
        self.destroyer = Ship()
        self.submarine = Ship()
        self.battleship = Ship()
        self.aircraft_carrier = Ship()

        self.ship_spaces_remaining = int


    def attack(self, list):
        pass

    def place_ships(self):
        pass 