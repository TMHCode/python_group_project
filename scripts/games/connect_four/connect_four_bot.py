import PySimpleGUI as sg
from random import choice

from scripts.menus import main_menu
from scripts.statistics.stats import save_score
from scripts.games.connect_four.connect_four import check_win, check_full, create_game, switch_player, create_pop_up,\
                                                    ROW_COUNT, COL_COUNT
"""
This is the file for the connect four game against a simple bot.
It imports or contains the functions that are necessary to play the game and the main game loop.
"""


# FUNCTIONS
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
    bot_col = -1                                    # set the bot_column choice to -1 because -1 is no existing column
    # preventing player from winning (one step ahead)
    for col in range(COL_COUNT):                    # for every column
        if grid[0][col] == ' ':                     # if the top row of the clicked column is empty
            for r in range(ROW_COUNT - 1, -1, -1):  # check for every cell in the row (from bottom to top)
                if grid[r][col] == ' ':             # if the specific cell is empty
                    grid[r][col] = 0                # give that cell to the player
                    if check_win(grid, 0):          # check if the player would win now
                        grid[r][col] = ' '          # set the cell to empty again
                        bot_col = col               # determine this column as the bot choice
                        break
                    grid[r][col] = ' '              # set the cell to empty again (outside of the check-win-if)
                    break
            if bot_col != -1:                       # if no possible player victory for this column was found
                break                               # break and check the next column

    if bot_col == -1:                               # if bot_col is not already determined (-1)
        available_cols = list(range(0, COL_COUNT))  # create an available_cols list
        for col in available_cols:                  # and for every column
            if grid[0][col] != ' ':                 # where the top cell is occupied
                available_cols.remove(col)          # remove the column from the available_cols list
        bot_col = choice(available_cols)            # set the bot_col to a random choice from the list

    for r in range(ROW_COUNT - 1, -1, -1):          # for every cell in the rows (from bottom to top)
        if grid[r][bot_col] == ' ':                 # if the cell in the bot column is empty
            grid[r][bot_col] = cur_player           # fill the cell with the bots index
            valid_turn = True                       # set the fail-save valid_turn to True
            window[(r, bot_col)].update(button_color=('white', '#FCF060'))  # change the cell color
            break

    return grid, window, valid_turn


# MAIN FUNCTION
def main(p_names: list):
    """
    This is the main function of the connect four game against a simple bot.
    It sets up important game variables and settings and contains the main game loop.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'Bot']
    :return: NO return value.
    """
    game_name = "c4"                                # needed in the save_score() function

    sg.SetOptions(font=('Helvetica', 18))           # set the font size of the window

    # Setting up start variables
    grid, layout, window, current_player, round_number = create_game(p_names)   # setting up start variables

    # Game loop
    while True:
        valid_turn = False  # fail-save to check if a turn was actually made (used for the switch player check)

        if current_player == 1:                 # check if the current player is the bot
            grid, window, valid_turn = bot_turn(grid, window, current_player, valid_turn)
        else:
            event, values = window.read()       # get the button click event
            if event is None:                   # fail-save
                break

            if event == 'Back':                 # when Back button is pressed, go back to the main menu
                window.close()
                main_menu.main()
                break

            if event == 'New Game':             # when New Game button is pressed, create a new game
                window.close()
                grid, layout, window, current_player, round_number = create_game(p_names)
                continue

            row, col = event                    # get the row and column of the button clicked

            # Update the grid and window if the column is not full
            if grid[0][col] == ' ':                         # if the top row of the clicked column is empty
                for r in range(ROW_COUNT - 1, -1, -1):      # check for every cell in the row (from bottom to top)
                    if grid[r][col] == ' ':                 # if the specific cell is empty
                        grid[r][col] = current_player       # set this cell to the current_player
                        round_number += 1                   # add 1 to the round number
                        window['round_number'].update(f'Round: {round_number}')
                        window[(r, col)].update(button_color=('white', '#6F3AFC'))
                        valid_turn = True
                        break

        if check_win(grid, current_player):                 # check if the current player has won
            if current_player == 0:                         # if current_player is the player
                save_score(p_names, "Win", 0, game_name)    # save the score as a win
                choice = create_pop_up(p_names, 0)          # create the win pop-up for the player
            else:                                           # if the bot has won
                save_score(p_names, "Lose", 0, game_name)   # save the score as a lose
                choice = create_pop_up(p_names, 1)          # create the win pop-up for the bot

            if choice == 'No':                  # check the players pop-up choice
                window.close()                  # if player clicked 'No' go back to the main menu
                main_menu.main()
                break
            else:
                window.close()                  # if the player clicked 'Yes' create a new clean game grid
                grid, layout, window, current_player, round_number = create_game(p_names)
                continue

        if check_full(grid):                            # check if the board is full
            save_score(p_names, "Draw", 0, game_name)   # save the scores for the player
            choice = create_pop_up(p_names, 2)          # create the pop-up with winner_id = 2, because it is a draw

            if choice == 'No':              # check the players pop-up choice
                window.close()              # if player clicked 'No' go back to the main menu
                main_menu.main()
                break
            else:
                window.close()              # if the player clicked 'Yes' create a new clean game grid
                grid, layout, window, current_player, round_number = create_game(p_names)
                continue

        if valid_turn:                                      # if a valid turn was made
            current_player = switch_player(current_player)  # switch the player

    window.close()      # close the window
