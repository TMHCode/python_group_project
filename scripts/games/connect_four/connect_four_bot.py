import PySimpleGUI as sg
from random import choice

from scripts.menus import main_menu
from scripts.statistics.stats import save_score
from scripts.games.connect_four.connect_four import check_win, check_full, create_game, switch_player
"""
This is the file for the connect four game against a simple bot.
It contains the functions that are necessary to play the game and the main game loop.
"""

# Game constants
ROW_COUNT = 6
COL_COUNT = 7


# Functions
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


def create_pop_up(p_names: list, winner_id: int):
    """
    This function creates a pop up when the end of the game is reached.
    Is can be a Draw or a Win Pop-Up. The player can chose to play another game or to return to the main menu
    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :param winner_id: (int) the id of the winner. Can be 0 or 1 (or 2 if it is a draw)
    :return: p_choice (str) the choice of the player when one of the pop up buttons was clicked. Can be 'Yes' or 'No'.
    """
    p_colors = ['#6F3AFC', '#FCF060']
    if winner_id == 2:      # winner_id is 2 when it is a draw
        pop_up_layout = [[sg.T('Draw!', font=('Helvetica', 30, 'bold'),
                               pad=(0, 5), justification='center', text_color='#FC9E47')],
                         [sg.T('The board is full.', font=('Helvetica', 15),
                               pad=(0, 30), justification='center', text_color="#FFF7E2")]]
    else:       # winner_id is 0 or 1
        pop_up_layout = [[sg.T(p_names[winner_id] + ' wins!', font=('Helvetica', 30, 'bold'),
                               pad=(0, 5), justification='center', text_color=p_colors[winner_id])]]

    pop_up_layout.append([[sg.T('Do you want to play again?', font=('Helvetica', 15),
                                pad=(0, 30), justification='center', text_color="#FFF7E2")],
                          [sg.No(s=10, button_color=('black', '#B8F1FF')),
                           sg.Yes(s=10, button_color=('black', '#FC9E47'))]])

    p_choice, _ = sg.Window('Game End', pop_up_layout, disable_close=True).read(close=True)
    return p_choice


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
                choice = create_pop_up(p_names, 0)
            else:
                save_score(p_names, "Lose", 0, game_name)
                choice = create_pop_up(p_names, 1)
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
            choice = create_pop_up(p_names, 2)
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
