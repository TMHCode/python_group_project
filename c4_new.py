import PySimpleGUI as sg

# Game constants
ROW_COUNT = 6
COL_COUNT = 7

# Create the game grid
grid = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

# Create the layout for the game window
layout = [[sg.Button(grid[r][c], button_color=('white', 'black'), size=(4, 2), key=(r, c)) for c in range(COL_COUNT)]
          for r in range(ROW_COUNT)]

# Create the game window
window = sg.Window('Connect 4', layout)

# Game variables
current_player = 'R'

# Game loop
while True:
    # Get the button click event
    event, values = window.read()
    if event is None:
        break

    # Get the row and column of the button clicked
    row, col = event

    # Update the grid and window
    for r in range(ROW_COUNT):
        if grid[r][col] == ' ':
            grid[r][col] = current_player
            window[(r, col)].update(current_player)
            break

    # Toggle the current player
    if current_player == 'R':
        current_player = 'Y'
    else:
        current_player = 'R'

# Close the window
window.close()