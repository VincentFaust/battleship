class Player(object):

    NUM_SHIPS = 5
    
    def __init__(self):
        self._ships = [0]*10
        self._board = [[" "]*10]*10
        self._opponent_board = [[" "]*10]*10
        self._name = ""
        self._ship_names = ['Aircraft Carrier (5)', 'Battleship (4)', 'Submarine (3)', 'Destroyer (3)', 'Patrol Boat (2)']
        self._ship_dict = {}
        

    def setName(self, n):
        self._name = n
        

    def getName(self):
        return self._name


    def find_ship(self, row, col):  
        return self._board[row][col]


    def check_ship(self, ship_num): 
        self._ship_dict[ship_num] -= 1
        if self._ship_dict[ship_num] == 0:
            return True
        else:
            return False


    def check_status(self): 
        for key, value in self._ship_dict.items():
            if value != 0:
                return False
        return True


    def sink_ship(self, ship_num): 
        for ship_name in self._ship_names:
            if ship_name[0] == ship_num:
                print(f"{self._name} says: You sunk my {ship_name}!")
                break


    def initialize_ships(self): 
        print("\nIt's time to place your boats!\nYou first select if you want to place the boat horizontally (H) or vertically (V). \nThen you select the location. The board is a 10 x 10 grid. \nThe top left location of the board is (0, 0), and the bottom right location is (9, 9). \nDepending on how you select your placement, you may not be able to place the boat in that position. \nIf you place a boat vertically, it will start at the location you specify and go downward from there. \nIf you place a boat horizontally, it will start at the location you specify and go rightward from there. \nPlease choose carefully as you place your boats. Once you place a boat, it cannot be moved.\n")

        for ship in self._ship_names:
            print(f'\nPlace your {ship}.')
            valid_placement = False
            while valid_placement == False:
                placement = input('Type a direction vector and a starting location.\nFor example: V 1 0 or H 4 5: ').split()

                if len(placement) == 3 :
                    ship_length = int(ship[-2])
                    direction = placement[0].upper()
                    row = int(placement[1])
                    col = int(placement[2])

                    self._ship_dict[ship[0]] = ship_length

                    if direction == 'V':
                        if ship_length <= len(self._board[row:]):
                            free_spaces = 0
                            for r in self._board[row:row+ship_length]:
                                if r[col] == " ":
                                    free_spaces += 1
                                
                            if free_spaces == ship_length:
                                valid_placement = True
                            
                                updated_board = []
                                for i in range(len(self._board)):
                                    updated_row = self._board[i].copy() 
                                    if row <= i < row+ship_length:
                                        updated_row[col] = ship[0]
                                    updated_board.append(updated_row)

                                self._board = updated_board.copy()

                            else:
                                print("Error - Invalid placement. Cannot place a ship on top of another ship.\n")
                        else:
                            print("Error - Invalid placement. Ship out of range of board.\n")

                    elif direction == "H":
                        
                        if ship_length <= len(self._board[row][col:]):

                            free_spaces = 0
                            for c in self._board[row][col:col+ship_length]:
                                if c == " ":
                                    free_spaces += 1
                                
                            if free_spaces == ship_length:
                                valid_placement = True
                                updated_board = []
                                for i in range(len(self._board)):
                                    updated_row = self._board[i].copy()
                                    if i == row:
                                        updated_row[col:col+ship_length] = ship[0]*ship_length
                                    updated_board.append(updated_row)
                                self._board = updated_board.copy()
                            else:
                                print("Error - Invalid placement. Cannot place a ship on top of another ship.\n")
                        else:
                            print("Error - Invalid placement. Ship out of range of board.\n")

                    else:
                        print("Error - Invalid direction. Enter 'V' or 'H'.")

                else:
                    print("Error - Invalid position. Must be V or H followed by a row and a column.\n")
                

    def initialize_boards(self):
        for i in range(self.NUM_SHIPS):
            self._ships.append(0)
    

    def display_boards(self):
        print("Player's Board\n*************")
        print("%-3s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s\n" % ("  ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
        print("%-3s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s\n" % ("  ", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"))
        for i in range(10):
            print(i, " |", end="")
            for j in range(10):
                print(self._board[i][j], " ", end="")
            print()
        
        print("Player's Opponent Board\n*************")
        print("%-3s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s\n" % ("  ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
        print("%-3s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s\n" % ("  ", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"))
        for i in range(10):
            print(i, " |", end="")
            for j in range(10):
                print(self._opponent_board[i][j], " ", end="")
            print()
        

    def getBoardEntry(self, r, c):  
        if self._board[r][c] == ' ':
            return False
        else:
            return True
        
        
    def setOpponentBoardEntry(self, r, c, v):  
        updated_board = []
        for i in range(len(self._opponent_board)):
            updated_row = self._opponent_board[i].copy()
            if i == r:
                updated_row[c] = v
            updated_board.append(updated_row)
        self._opponent_board = updated_board.copy()
