import random
from player import Player
from computer import Computer

class Battleship(object):
    def __init__(self):
        n = input("Player, please enter your name: ")
        self._player = Player()
        self._player.setName(n)
        self._player.initialize_ships()
        self._computer = Computer()
        self._computer.initialize_ships()
        self._player.initialize_boards()
        self._computer.initialize_boards()
        print("Boards and Ships initialized!")
        self._status = True


    def check_player_guess(self, row, col):
        row = int(row)
        col = int(col)
        is_hit = self._computer.getBoardEntry(row, col)
        if is_hit:
            self._player.setOpponentBoardEntry(row, col, 'H')
            print(f'Hit by {self._player.getName()}!')
            hit_ship = self._computer.find_ship(row, col)
            ship_got_sunk = self._computer.check_ship(hit_ship) 
            if ship_got_sunk:
                self._computer.sink_ship(hit_ship)
                all_sunk = self._computer.check_status()
                if all_sunk:
                    self._status = False
        else:
            self._player.setOpponentBoardEntry(row, col, "M")
            print(f"Miss by {self._player.getName()}!")
        self._player.display_boards()
  

    def check_computer_guess(self):
        row = random.randint(0,9)
        col = random.randint(0,9)
        is_hit = self._player.getBoardEntry(row, col)
        if is_hit:
            self._computer.setOpponentBoardEntry(row, col, "H")
            print("Hit by Computer!")
            hit_ship = self._player.find_ship(row, col)
            ship_got_sunk = self._player.check_ship(hit_ship) 
            if ship_got_sunk:
                self._player.sink_ship(hit_ship)
                all_sunk = self._player.check_status() 
                if all_sunk:
                    self._status = False
        else:
            print("Miss by Computer!")
            
            
    def get_status(self):
        return self._status 
