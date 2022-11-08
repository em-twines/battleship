# from ship import Ship
from player import Player
# from aircraft_carrier import Aircraft_Carrier

class Game_board:

    def __init__(self):
        # self.player_1 = Player("Player_1")
        # self.player_2 = Player("Player_2")
        name = "Game_Board"


    def display_rules(self):
        pass

    def display_current_board(self, player):
        # print(player.current_board)
        pass


    def run_game(self):
        player_1 = Player("Player_1")
        player_2 = Player("Player_2")
        player_1.define_board()
        
        player_1.place_ships(player_1.destroyer)
        player_1.place_ships(player_1.submarine)
        player_1.place_ships(player_1.battleship)
        player_1.place_ships(player_1.aircraft_carrier)
        print(player_1.current_board)

        player_2.define_board()
        player_2.place_ships(player_2.destroyer)
        player_2.place_ships(player_2.submarine)
        player_2.place_ships(player_2.battleship)
        player_2.place_ships(player_2.aircraft_carrier)
        print(player_2.current_board)

    def display_winner(self):
        pass 



