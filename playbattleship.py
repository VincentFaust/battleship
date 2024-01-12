
from battleship import Battleship
import random


def main():
    winner = False
    print("Welcome to the game of BATTLESHIP!\n"
             "The objective of this game is to sink all of your opponent's boats.\n"
             "Each player has five (5) boats. Each boat has a name and a size.\n"
             "Here are the boat names and sizes:\n"
             "Aircraft Carrier 5\n"
             "BATTLESHIP 4\n"
             "Submarine 3\n"
             "Destroyer 3\n"
             "Patrol Boat 2")
    game = Battleship()
    random.seed()
    turn = random.randint(1, 2)  
    
    while not(winner):
        if turn == 1:  
            row_col = input("Please enter your guess (Row Column): ").split()
            row, col = int(row_col[0]), int(row_col[1])
            game.check_player_guess(row, col)
            if not(game.get_status()):
                print(f"{game._player.getName()} wins!\n")
                break
            game.check_computer_guess()
            if not(game.get_status()):
                print("Computer wins!\n")
                break
        else:    
            game.check_computer_guess()
            if not(game.get_status()):
                print("Computer wins!\n")
                break
            row_col = input("Please enter your guess (Row Column): ").split()
            row, col = int(row_col[0]), int(row_col[1])
            game.check_player_guess(row, col)
            if not(game.get_status()):
                print(f"{game._player.getName()} wins!\n")
                break


if __name__ == '__main__':
    main()

'''Two player game.
   if not(game.get_status()):
        #Player wins.
        break
   else:
        choice = input("Are you done with your move?")
        #Get yes or no here and then go to a blank screen and prompt for the next player
        #to begin their turn. This way, neither player sees the other players' board.
 '''
