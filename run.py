

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
format_board(board)