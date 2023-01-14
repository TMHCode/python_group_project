import PySimpleGUI as sg
from random import choice

from scripts.menus import main_menu
from scripts.layouts import create_connect_four_layout
from scripts.statistics.stats import save_score
"""
This is the file for the connect four game against a simple bot.
It contains the functions that are necessary to play the game and the main game loop.
"""

# Game constants
ROW_COUNT = 6
COL_COUNT = 7


# Functions
def check_win(grid: list, player: int):
    """
    This function checks the win conditions for the game connect four.
    There are three win conditions that need to be checked after every move:
        - are there 4 pieces next to each other in a row
        - are there 4 pieces next to each other in a column
        - are there 4 pieces next to each other diagonally

    :param grid: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
    :param player: (int) index of the current player. Can be 0 or 1
    :return: (bool) returns True if the player wins and False if the player does not win.
    """
    # Check horizontal win
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT - 3):
            if grid[r][c] == player \
                    and grid[r][c + 1] == player \
                    and grid[r][c + 2] == player \
                    and grid[r][c + 3] == player:
                return True

    # Check vertical win
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT):
            if grid[r][c] == player \
                    and grid[r + 1][c] == player \
                    and grid[r + 2][c] == player \
                    and grid[r + 3][c] == player:
                return True

    # Check diagonal win (top-left to bottom-right)
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT - 3):
            if grid[r][c] == player \
                    and grid[r + 1][c + 1] == player \
                    and grid[r + 2][c + 2] == player \
                    and grid[r + 3][c + 3] == player:
                return True

    # Check diagonal win (bottom-left to top-right)
    for r in range(3, ROW_COUNT):
        for c in range(COL_COUNT - 3):
            if grid[r][c] == player \
                    and grid[r - 1][c + 1] == player \
                    and grid[r - 2][c + 2] == player \
                    and grid[r - 3][c + 3] == player:
                return True
    return False


def check_full(grid: list):
    """
    This function checks if the grid is full (if the game ends in a draw).
    This needs to be checked after every move.

    :param grid: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
    :return: (bool) returns True if the grid is full and False if there is still an empty cell.
    """
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if grid[r][c] == ' ':
                return False
    return True


def create_game(p_names: list):
    """
    This function creates a clean new game grid.
    This needs to be called every time before a new game is starting.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'Bot']
    :return:
        grid_: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
        layout_: (list) a list that contains the layout for this window
        window_: (sg.Window) the PySimpleGUI Window element
        current_player_: (int) the index of the current player. Can be 0 or 1.
        round_number_: (int) the number of the current round
    """
    # Create the game grid
    grid_ = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

    # Create the layout for the game window
    layout_ = create_connect_four_layout(COL_COUNT, ROW_COUNT, p_names)

    # Create the game window
    window_ = sg.Window('Connect 4 - PvB', layout_, size=(1200, 800), resizable=True, element_justification='center')

    # Game variables
    current_player_ = 0
    round_number_ = 1

    return grid_, layout_, window_, current_player_, round_number_


def switch_player(cur_player: int):
    """
    This function switches the current player index.
    This needs to be called after every player move, if no game-ending condition (win, lose or draw) is met.

    :param cur_player: (int) index of the current player. Can be 0 or 1.
    :return: (int) returns the player index of the next player.
    """
    if cur_player == 0:
        return 1
    else:
        return 0


def bot_turn(grid: list, window: sg.Window, cur_player: int, valid_turn: bool):
    """
    This function simulates the bots turn.
    It is a very simple bot that tries to prevent the player from winning if the player would win with their next move.
    Otherwise it currently just places pieces randomly in the free cells on the grid.

    :param grid: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
    :param window: (sg.Window) the PySimpleGUI Window element
    :param cur_player: (int) index of the current player. Can be 0 or 1.
    :param valid_turn: (bool) a control boolean to check if a valid move was made, so the bot doesn't skip its turn.
    :return:
        grid: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
        window: (sg.Window) the PySimpleGUI Window element
        valid_turn: (bool) a control boolean to check if a valid move was made, so the bot doesn't skip its turn
    """
    bot_col = -1
    # preventing player from winning (one step ahead)
    for col in range(COL_COUNT):
        if grid[0][col] == ' ':
            for r in range(ROW_COUNT - 1, -1, -1):
                if grid[r][col] == ' ':
                    grid[r][col] = 0
                    if check_win(grid, 0):
                        grid[r][col] = ' '
                        bot_col = col
                        break
                    grid[r][col] = ' '
                    break
            if bot_col != -1:
                break

    # random cell placement if bot_col is not already determined
    if bot_col == -1:
        # check what columns still have an empty space
        available_cols = list(range(0, COL_COUNT))
        for col in available_cols:
            if grid[0][col] != ' ':
                available_cols.remove(col)
        # determine a random column from the free columns
        bot_col = choice(available_cols)

    for r in range(ROW_COUNT - 1, -1, -1):
        if grid[r][bot_col] == ' ':
            grid[r][bot_col] = cur_player
            valid_turn = True
            window[(r, bot_col)].update(button_color=('white', '#FCF060'))
            break

    return grid, window, valid_turn


def main(p_names: list):
    """
    This is the main function of the connect four game against a simple bot.
    It sets up important game variables and settings and contains the main game loop.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'Bot']
    :return: NO return value.
    """
    game_name = "c4"

    # Set the font size of the window
    sg.SetOptions(font=('Helvetica', 18))

    # Setting up start variables
    grid, layout, window, current_player, round_number = create_game(p_names)

    # Game loop
    while True:
        valid_turn = False  # bool to check if a turn was actually made (used for the switch player check)
        # Check if BOT turn
        if current_player == 1:
            grid, window, valid_turn = bot_turn(grid, window, current_player, valid_turn)
        else:
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
                        round_number += 1
                        window['round_number'].update(f'Round: {round_number}')
                        window[(r, col)].update(button_color=('white', '#6F3AFC'))
                        valid_turn = True
                        break

        # Check if the current player has won
        if check_win(grid, current_player):
            if current_player == 0:
                save_score(p_names, "Win", 0, game_name)
                choice, _ = sg.Window('Game End',
                                      [[sg.T(p_names[0] + ' wins!', font=('Helvetica', 30, 'bold'),
                                             pad=(0, 5), justification='center', text_color='#6F3AFC')],
                                       [sg.T('Do you want to play again?', font=('Helvetica', 15),
                                             pad=(0, 30), justification='center', text_color="#FFF7E2")],
                                       [sg.No(s=10, button_color=('black', '#B8F1FF')),
                                        sg.Yes(s=10, button_color=('black', '#FC9E47'))]],
                                      disable_close=True).read(close=True)
            else:
                save_score(p_names, "Lose", 0, game_name)
                choice, _ = sg.Window('Game End',
                                      [[sg.T('Bot wins!', font=('Helvetica', 30, 'bold'),
                                             pad=(0, 5), justification='center', text_color='#FCF060')],
                                       [sg.T('Do you want to play again?', font=('Helvetica', 15),
                                             pad=(0, 30), justification='center', text_color="#FFF7E2")],
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

        # Check if the board is full
        if check_full(grid):
            save_score(p_names, "Draw", 0, game_name)
            choice, _ = sg.Window('Game End',
                                  [[sg.T('Draw!', font=('Helvetica', 30, 'bold'),
                                         pad=(0, 5), justification='center', text_color='#FC9E47')],
                                   [sg.T('The board is full.', font=('Helvetica', 15),
                                         pad=(0, 30), justification='center', text_color="#FFF7E2")],
                                   [sg.T('Do you want to play again?', font=('Helvetica', 15),
                                         justification='center', text_color="#FFF7E2")],
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

        if valid_turn:
            current_player = switch_player(current_player)

    # Close the window
    window.close()
