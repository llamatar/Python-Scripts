import numpy as np

# define the size of the game board
ROWS = 6
COLUMNS = 7

# create an empty game board
board = np.zeros((ROWS, COLUMNS))

# initialize the game
current_player = 1
game_over = False

# define the possible directions for a winning sequence
directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

# define the function to check for a win
def check_win(r, c):
    # check the four possible directions for a win
    for dr, dc in directions:
        sequence = []
        for i in range(-3, 4):
            row = r + i * dr
            col = c + i * dc
            if row >= 0 and row < ROWS and col >= 0 and col < COLUMNS:
                sequence.append(board[row][col])
        # check if the current player has four in a row
        if sequence.count(current_player) == 4:
            return True
    return False

# define the main game loop
while not game_over:
    # display the current game board
    print(board)

    # get the current player's move
    col = int(input("Player {}: choose a column (0-6): ".format(current_player)))
    if col < 0 or col >= COLUMNS:
        print("Invalid column, please choose a column between 0 and {}.".format(COLUMNS - 1))
        continue


    # place the current player's piece on the board
    placed = False
    for r in range(ROWS):
        if board[r][col] == 0:
            board[r][col] = current_player
            placed = True
            break
    if not placed:
        print("Column is full, please choose a different column.")
        continue
    
    # check if the current player has won
    if check_win(r, col):
        print("Player {} wins!".format(current_player))
        game_over = True
        break
    
    # switch to the other player
    current_player = 1 if current_player == 2 else 2

# check for a tie
if not game_over:
    print("It's a tie!")
