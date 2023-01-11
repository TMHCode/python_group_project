import PySimpleGUI as sg

from scripts.menus import menu_main
from scripts.layouts import create_connect_four_layout


## Game constants
ROW_COUNT = 6
COL_COUNT = 7


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


# function that creates a new clean game board
def create_game():
    # Create the game grid
    grid_ = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

    # Create the layout for the game window
    layout_ = create_connect_four_layout(COL_COUNT, ROW_COUNT)

    # Create the game window
    window_ = sg.Window('Connect 4', layout_, size=(1100, 700), resizable=True, element_justification='center')

    # Game variables
    current_player_ = 'P1'
    return grid_, layout_, window_, current_player_


# main function
def main():

    # Set the font size of the window
    sg.SetOptions(font=('Helvetica', 18))

    ## Setting up start variables
    grid, layout, window, current_player = create_game()

    ## Game loop
    while True:
        # Get the button click event
        event, values = window.read()
        if event is None:
            break

        if event == 'Back':
            window.close()
            menu_main.main()
            break

        if event == 'New Game':
            # create a new clean game board
            window.close()
            grid, layout, window, current_player = create_game()
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
                # create a new clean game board
                window.close()
                grid, layout, window, current_player = create_game()
                continue

            # Check if the board is full
            if check_full(grid):
                sg.popup('The board is full!')
                # create a new clean game board
                window.close()
                grid, layout, window, current_player = create_game()
                continue

            # Toggle the current player
            if current_player == 'P1':
                current_player = 'P2'
            else:
                current_player = 'P1'

    ## Close the window
    window.close()


if __name__ == '__main__':
    main()
