import PySimpleGUI as sg

from scripts.menus import main_menu
from scripts.layouts import create_connect_four_layout
from scripts.statistics.stats import save_score


## Game constants
ROW_COUNT = 6
COL_COUNT = 7


## Functions
# function for checking win conditions
def check_win(grid: list, player: int):
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
def check_full(grid: list):
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if grid[r][c] == ' ':
                return False
    return True


# function that creates a new clean game board
def create_game(p_names: list):
    # Create the game grid
    grid_ = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

    # Create the layout for the game window
    layout_ = create_connect_four_layout(COL_COUNT, ROW_COUNT, p_names)

    # Create the game window
    window_ = sg.Window('Connect 4 - PvP', layout_, size=(1100, 700), resizable=True, element_justification='center')

    # Game variables
    current_player_ = 0
    round_number_ = 1

    return grid_, layout_, window_, current_player_, round_number_


# main function
def main(p_names: list):

    game_name = "c4"

    # Set the font size of the window
    sg.SetOptions(font=('Helvetica', 18))

    # Set the player colors
    p_background_colors = ['#6F3AFC', '#FCF060']
    p_text_colors = ['#FFF7E2', '#2C2825']

    ## Setting up start variables
    grid, layout, window, current_player, round_number = create_game(p_names)

    ## Game loop
    while True:
        # Get the button click event
        event, values = window.read()

        if event is None:
            break

        if event == 'Back':
            window.close()
            main_menu.main()
            break

        if event == 'New Game':
            # create a new clean game board
            window.close()
            grid, layout, window, current_player, round_number = create_game(p_names)
            continue

        # Get the row and column of the button clicked
        row, col = event

        # Update the grid and window if the column is not full
        if grid[0][col] == ' ':
            for r in range(ROW_COUNT - 1, -1, -1):
                if grid[r][col] == ' ':
                    grid[r][col] = current_player
                    if current_player == 0:
                        window[(r, col)].update(button_color=('white', p_background_colors[0]))
                    else:
                        round_number += 1
                        window['round_number'].update(f'Round: {round_number}')
                        window[(r, col)].update(button_color=('white', p_background_colors[1]))
                    break

            # Check if the current player has won
            if check_win(grid, current_player):
                save_score(p_names, "Win", current_player, game_name)
                losing_player = 1 if current_player == 0 else 0
                save_score(p_names, "Lose", losing_player, game_name)
                # win pup up
                choice, _ = sg.Window('Game End', [[sg.T(p_names[current_player] + ' wins!', font=('Helvetica', 30, 'bold'), pad=(0, 5), justification='center', text_color=p_background_colors[current_player])], [sg.T('Do you want to play again?', font=('Helvetica', 15), pad=(0, 30), justification='center', text_color="#FFF7E2")], [sg.No(s=10, button_color=('black', '#B8F1FF')), sg.Yes(s=10, button_color=('black', '#FC9E47'))]], disable_close=True).read(close=True)
                # Pop-Up choice 'No'
                if choice == 'No':
                    # go back to the main menu
                    window.close()
                    main_menu.main()
                    break
                else:
                    # create a new clean game board
                    window.close()
                    grid, layout, window, current_player, round_number = create_game(p_names)
                    continue

            # Check if the board is full
            if check_full(grid):
                save_score(p_names, "Draw", 0, game_name)
                save_score(p_names, "Draw", 1, game_name)
                choice, _ = sg.Window('Game End', [[sg.T('Draw!', font=('Helvetica', 30, 'bold'), pad=(0, 5),
                                                         justification='center', text_color='#FC9E47')], [
                                                       sg.T('The board is full.', font=('Helvetica', 15),
                                                            pad=(0, 30), justification='center', text_color="#FFF7E2")],[
                                                       sg.T('Do you want to play again?', font=('Helvetica', 15), justification='center', text_color="#FFF7E2")],
                                                   [sg.No(s=10, button_color=('black', '#B8F1FF')),
                                                    sg.Yes(s=10, button_color=('black', '#FC9E47'))]],
                                      disable_close=True).read(close=True)
                # Pop-Up choice 'No'
                if choice == 'No':
                    # go back to the main menu
                    window.close()
                    main_menu.main()
                    break
                else:
                    # create a new clean game board
                    window.close()
                    grid, layout, window, current_player, round_number = create_game(p_names)
                    continue

            # Toggle the current player
            if current_player == 0:
                current_player = 1
            else:
                current_player = 0

            # update the current player text
            window['active_player'].update(f'Current Player: {p_names[current_player]}', background_color=p_background_colors[current_player], text_color=p_text_colors[current_player])

    ## Close the window
    window.close()

