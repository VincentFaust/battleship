# Battleship Game 

# Project Overview

This Battleship game is a Python-based implementation of the classic board game. The game is played against a computer opponent. Each player has a fleet of ships that they must hide on a 10x10 grid. The players then take turns guessing the locations of the opponent's ships. The objective is to sink all of the opponent's ships. 

This project also was a 100 point extra credit assignment for an intro to computer science class I took back in spring '22. The only outlining structure we had to follow in order to get credit was to use private variables (not really a thing in python) and utilize setters and getters. 

I completed it and finished with the highest grade in the class. 


# Codebase 

`battleship.py`
Contains the Battleship class, which is the central game controller. It manages the game flow, including initializing the game state, processing player and computer guesses, and determining the end of the game

`computer.py`
Implements the Computer class, representing the computer opponent in the game. This class handles the computer's ship placements, guesses, and responses to the player's actions

`player.py`
The main script to run the Battleship game. It initializes the game, handles the turn-based logic, and manages interactions between the player and computer.

`playbattleship.py`
The main script to run the Battleship game. It initializes the game, handles the turn-based logic, and manages interactions between the player and computer.

# Getting Started 

`Initialization` Run play battleship.py to start the game. 

`Setup` Enter your name and position your fleet on the grid.

`Game Loop`
    Players take turns guessing grid coordinates to find and sink the opponent's ships.
    After each guess, the board is updated to reflect hits and misses.

`Winning the Game` The game ends when all ships of either player or the computer are sunk. The first to sink all opponent's ships wins.* 

*The above directions are also printed to the console when you start up a game. 


# Future Considerations 
Since this was originally an assignment, I included the computers board display for ease of use for my computer. So for play purposes, it makes sense to remove it from view. 