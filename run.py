from random import randint


"""
Creates 5x5 game board 
"""
board = []
for x in range(5):
    board.append(["0"] * 5)

def format_board(board):
    for i in board:
        print(" ".join(i))


"""
Game intro 
"""
print("Welcome to Battleship!")
print("Board size: 5x5. Number of ships: 1. Number of missiles: 3. \n")
print("Top left corner is row: 0, column: 0. Please enter co-ordinates from 0-4\n")
format_board(board)


""" 
Places ship in random location on board
"""
def rand_column(board):
    return randint(0, len(board) -1)

def rand_row(board):
    return randint(0, len(board) -1)

ship_column = rand_column(board)
ship_row = rand_row(board)


""" 
Allows player to guess a location
"""
guess_row = input("Guess Row: \n")
guess_column = input("Guess Column: \n")