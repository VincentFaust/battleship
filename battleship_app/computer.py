import random

class Computer(object):
    NUM_SHIPS = 5

    def __init__(self):      
        self._ships = [0]*10
        self._board = [[" "]*10]*10
        self._opponent_board = [[" "]*10]*10
        self._ship_names = ['Aircraft Carrier (5)', 'Battleship (4)', 'Submarine (3)', 'Destroyer (3)', 'Patrol Boat (2)']
        self._ship_dict = {}


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
            print(key,value)
            if value != 0:
                return False
        return True
    

    def sink_ship(self, ship_num): 
        for ship_name in self._ship_names:
            if ship_name[0] == ship_num:
                print(f"Computer says: You sunk my {ship_name}!")
                break
    

    def initialize_ships(self):  
        for i in range(self.NUM_SHIPS):
            self._ships.append(0)
        

    def initialize_boards(self):  

        for ship in self._ship_names:
            
            valid_placement = False
            while valid_placement == False:

                ship_length = int(ship[-2])
                self._ship_dict[ship[0]] = ship_length
                direction = random.choice(['V','H'])

             
                if direction == 'V':
                    row = random.randint(0, len(self._board)-1)
                    col = random.randint(0, len(self._board)-1-ship_length)

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
                    row = random.randint(0, len(self._board)-1-ship_length)
                    col = random.randint(0, len(self._board)-1)
                    
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

        print('Computer board:')
        for line in self._board:
            print(line)
    

    def display_boards(self):
        print("Computer's Board\n*************")
        print("%-3s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s\n" % ("  ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
        print("%-3s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s%-2s\n" % ("  ", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"))
        for i in range(10):
            print(i, " |", end="")
            for j in range(10):
                print(self._board[i][j], " ", end="")
            print()
    
        print("Computer's Opponent Board\n*************")
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
