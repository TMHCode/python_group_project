# define the grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# define the players
players = ['X', 'O']

# define the number of rows and columns in the grid
num_rows = len(grid)
num_columns = len(grid[0])

# define a function to print the grid
def print_grid():
    for row in grid:
        print(' '.join(row))

# initialize the current player to the first player
current_player = players[0]

# initialize the game over flag to False
game_over = False

# initialize the number of moves made to 0
num_moves = 0

# define a function to switch players
def switch_player():
    global current_player
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]

# define a function to check if a move is valid
def is_valid_move(column):
    return grid[0][column] == '.'

# define a function to make a move
def make_move(column):
    # find the first empty row in the specified column
    for row in range(num_rows-1, -1, -1):
        if grid[row][column] == '.':
            # make the move
            grid[row][column] = current_player
            return

# define a function to check if a player has won
def check_win():
    # check for horizontal wins
    for row in range(num_rows):
        for col in range(num_columns - 3):
            if grid[row][col] == current_player and grid[row][col+1] == current_player and grid[row][col+2] == current_player and grid[row][col+3] == current_player:
                return True

    # check for vertical wins
    for row in range(num_rows - 3):
        for col in range(num_columns):
            if grid[row][col] == current_player and grid[row+1][col] == current_player and grid[row+2][col] == current_player and grid[row+3][col] == current_player:
                return True

    # check for diagonal wins
    for row in range(num_rows - 3):
        for col in range(num_columns - 3):
            if grid[row][col] == current_player and grid[row+1][col+1] == current_player and grid[row+2][col+2] == current_player and grid[row+3][col+3] == current_player:
                return True

    # if no wins are found, return False
    return False

# define the main game loop
while not game_over:
	# print the grid
	print_grid()
	# prompt the user for a move
	column = int(input('Enter column: '))

	# check if the move is valid
	if not is_valid_move(column):
		print('Invalid move, try again')
		continue

	# make the move
	make_move(column)

	# increment the number of moves made
	num_moves += 1

	# check if the current player has won
	if check_win():
		print(f'Player {current_player} wins!')
		game_over = True
		continue

	# check if the game is a draw
	if num_moves == num_rows * num_columns:
		print('The game is a draw!')
		game_over = True
		continue

	# switch players
	switch_player()
	# print the final grid
	print_grid()
	print("___________________\n\n")