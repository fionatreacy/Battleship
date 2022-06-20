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
Compare players guess to the ships location and gives a message if the player hits, misses, or has repeated a guess.
"""
for attempts in range(3):
    print("Attempts", attempts + 1)
    """ 
    Repeats the game until all attempts have been used or player wins
    """
    """ 
    Allows player to guess a location
    """
    guess_row = int(input("Guess Row: \n"))
    guess_column = int(input("Guess Column: \n"))
    
    if ship_row == guess_row and ship_column == guess_column:
        print("You've sunk the Battleship!")
        board[ship_row][ship_column] = "X"
        print(format_board(board))

    else:
        if (guess_column > 5 or guess_row > 5) or (guess_column <0 or guess_row < 0):
            print("Those are land co-ordinates, please enter a number from 0-4")
            print(format_board(board))
        elif board[guess_row][guess_column] == "-":
            print("You've guessed that one already, try again.")
            print(format_board(board))
        else:
            print("You missed! You have X attempts left")
            board[guess_row][guess_column] = "-"
            print(format_board(board))