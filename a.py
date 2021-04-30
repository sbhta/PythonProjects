import random

# creating the board
board = []
for y in range(5):
    board.append(["X"] * 5)

# creating the winning pos
board[random.randint(0, 4)][random.randint(0, 4)] = "O"

# printing the board
for row in board:
    print(" ".join(row))
