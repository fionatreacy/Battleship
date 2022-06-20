from random import randint

board = []
"""
Creates 5x5 game board
"""
for x in range(5):
    board.append(["0"] * 5)


def format_board(board):
    for i in board:
        print(" ".join(i))


print("Welcome to Battleship!")
print("Number of missiles: 3. Board size: 5x5. \n")
print("Top left corner is row: 0, column: 0. \n")
format_board(board)
"""
Prints game intro + instructions
"""


def rand_column(board):
    return randint(0, len(board) - 1)


def rand_row(board):
    return randint(0, len(board) - 1)


ship_column = rand_column(board)
ship_row = rand_row(board)
"""
Places ship in random location on board
"""


for attempts in range(5):
    """
    Repeats the game until all attempts have been used or player wins
    """
    print("Attempt: ", attempts + 1)

    guess_row = int(input("Guess Row 0-4 : \n"))
    guess_column = int(input("Guess Column 0-4 : \n"))


    if ship_row == guess_row and ship_column == guess_column:
        """
        The following compares players guess to the ships location and gives
        a message if the player hits, misses, or has repeated a guess.
        """
        print("You've sunk the Battleship!")
        board[ship_row][ship_column] = "X"
        print(format_board(board))

    else:
        if (guess_column > 5 or guess_row > 5):
            print("Those are land co-ordinates, try again.")
            print(format_board(board))
        elif (guess_column < 0 or guess_row < 0):
            print("Those are land co-ordinates, try again.")
            print(format_board(board))
        elif board[guess_row][guess_column] == "-":
            print("You've guessed that one already, try again.")
            print(format_board(board))
        else:
            print("You missed! Try again.")
            board[guess_row][guess_column] = "-"
            print(format_board(board))

    if attempts == 6:
        print("Game Over")
