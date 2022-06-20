

"""
create board 
"""
board = []
for x in range(5):
    board.append(["0"] * 5)

def format_board(board):
    for i in board:
        print(i)

print("Let's play Battleship!")
print("Board size: 5x5. Number of ships: 1. Number of missiles: 3. \n")
print("Top left corner is row: 0, column: 0. Please enter co-ordinates from 0-4\n")
format_board(board)