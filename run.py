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
guess_row = int(input("Guess Row: \n"))
guess_column = int(input("Guess Column: \n"))

print(ship_row)
print(ship_column)

""" 
Compare players guess to the ships location and gives a message if the player hits or misses.
"""
if ship_row == guess_row and ship_column == guess_column:
    print("You've sunk the Battleship!")
    board[ship_row][ship_column] = "X"
    print(format_board(board))

elif guess_column > 5 or guess_row > 5:
    print("Those are land co-ordinates, please enter a number from 0-4")
    print(format_board(board))
else:
    print("You missed! You have X attempts left")
    board[guess_row][guess_column] = "-"
    print(format_board(board))
