import PySimpleGUI as sg

## Game constants
ROW_COUNT = 6
COL_COUNT = 7

# Set the size and color scheme of the window
sg.ChangeLookAndFeel('DarkAmber')  # Add a touch of color
sg.SetOptions(font=('Helvetica', 18))


## Functions
# function for checking win conditions
def check_win(grid, player):
    # Check horizontal win
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT - 3):
            if grid[r][c] == player and grid[r][c + 1] == player and grid[r][c + 2] == player and grid[r][c + 3] == player:
                return True

    # Check vertical win
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT):
            if grid[r][c] == player and grid[r + 1][c] == player and grid[r + 2][c] == player and grid[r + 3][c] == player:
                return True

    # Check diagonal win (top-left to bottom-right)
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT - 3):
            if grid[r][c] == player and grid[r + 1][c + 1] == player and grid[r + 2][c + 2] == player and grid[r + 3][c + 3] == player:
                return True

    # Check diagonal win (bottom-left to top-right)
    for r in range(3, ROW_COUNT):
        for c in range(COL_COUNT - 3):
            if grid[r][c] == player and grid[r - 1][c + 1] == player and grid[r - 2][c + 2] == player and grid[r - 3][c + 3] == player:
                return True

    return False


# function for checking if the board is full (draw)
def check_full(grid):
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if grid[r][c] == ' ':
                return False
    return True


# function that creates the PySimpleGUI layout
def create_layout():
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text('Connect Four', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                *[[sg.Button(' ', button_color=('white', 'black'), size=(5, 2), pad=(0, 0), key=(r, c)) for c in range(COL_COUNT)] for r in range(ROW_COUNT)],
                [sg.Push(), sg.Button('Quit', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(50, 15), border_width=8),
                    sg.Button('New Game', size=(14, 2), pad=(50, 15), border_width=10), sg.Push()],
                [sg.VPush()]
            ]


# function that creates the PySimpleGUI window
def create_window():
    return sg.Window('Connect 4', layout, size=(1100, 700), resizable=True, element_justification='center')

## Setting up start variables
# Create the game grid
grid = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

# Create the layout for the game window
layout = create_layout()

# Create the game window
window = create_window()

# Game variables
current_player = 'P1'

## Game loop
while True:
    # Get the button click event
    event, values = window.read()
    if event is None:
        break

    if event == 'Quit':
        break

    if event == 'New Game':
        grid = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]
        window.close()
        layout = create_layout()
        window = create_window()
        current_player = 'P1'
        continue

    # Get the row and column of the button clicked
    row, col = event

    # Update the grid and window if the column is not full
    if grid[0][col] == ' ':
        for r in range(ROW_COUNT - 1, -1, -1):
            if grid[r][col] == ' ':
                grid[r][col] = current_player
                if current_player == 'P1':
                    window[(r, col)].update(button_color=('white', '#6F3AFC'))
                else:
                    window[(r, col)].update(button_color=('white', '#FCF060'))
                break

        # Check if the current player has won
        if check_win(grid, current_player):
            sg.popup('Player ' + current_player + ' wins!')
            break

        # Check if the board is full
        if check_full(grid):
            sg.popup('The board is full!')
            break

        # Toggle the current player
        if current_player == 'P1':
            current_player = 'P2'
        else:
            current_player = 'P1'

## Close the window
window.close()
