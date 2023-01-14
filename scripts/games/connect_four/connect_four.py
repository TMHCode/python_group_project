import PySimpleGUI as sg

from scripts.menus import main_menu
from scripts.layouts import create_connect_four_layout
from scripts.statistics.stats import save_score
"""
This is the file for the connect four game player against player.
It contains the functions that are necessary to play the game and the main game loop.
"""


# GAME CONSTANTS
ROW_COUNT = 6
COL_COUNT = 7


# FUNCTIONS
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
    for r in range(ROW_COUNT):                          # for every row
        for c in range(COL_COUNT - 3):                  # for every column except the last 3
            if grid[r][c] == player \
                    and grid[r][c + 1] == player \
                    and grid[r][c + 2] == player \
                    and grid[r][c + 3] == player:       # if 4 adjacent cells are occupied by the same player
                return True                             # return True

    # Check vertical win
    for r in range(ROW_COUNT - 3):                      # for every row except the last 3
        for c in range(COL_COUNT):                      # for every column
            if grid[r][c] == player \
                    and grid[r + 1][c] == player \
                    and grid[r + 2][c] == player \
                    and grid[r + 3][c] == player:       # if 4 adjacent cells are occupied by the same player
                return True                             # return True

    # Check diagonal win (top-left to bottom-right)
    for r in range(ROW_COUNT - 3):                      # for every row except the last 3
        for c in range(COL_COUNT - 3):                  # for every column except the last 3
            if grid[r][c] == player \
                    and grid[r + 1][c + 1] == player \
                    and grid[r + 2][c + 2] == player \
                    and grid[r + 3][c + 3] == player:   # if 4 adjacent cells are occupied by the same player
                return True                             # return True

    # Check diagonal win (bottom-left to top-right)
    for r in range(3, ROW_COUNT):                      # for every row except the first 3
        for c in range(COL_COUNT - 3):                 # for every column except the last 3
            if grid[r][c] == player \
                    and grid[r - 1][c + 1] == player \
                    and grid[r - 2][c + 2] == player \
                    and grid[r - 3][c + 3] == player:   # if 4 adjacent cells are occupied by the same player
                return True                             # return True
    return False                                # otherwise, if no win condition is met, return False


def check_full(grid: list):
    """
    This function checks if the grid is full (if the game ends in a draw).
    This needs to be checked after every move.

    :param grid: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
    :return: (bool) returns True if the grid is full and False if there is still an empty cell.
    """
    for r in range(ROW_COUNT):                          # for every row
        for c in range(COL_COUNT):                      # for every column
            if grid[r][c] == ' ':                       # if any cell is still empty
                return False                            # return False
    return True                                 # otherwise return True


def create_game(p_names: list):
    """
    This function creates a clean new game grid.
    This needs to be called every time before a new game is starting.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :return:
        grid_: (list) a list of lists that is representing the playing field.
                    list-structure: [[row 1], [row 2], [row 3],...]
                           example: [[' ', 1, 1, ' ', 0,...], [' ', 0, 1, ' ', 0,...], [...], ...]
        layout_: (list) a list that contains the layout for this window
        window_: (sg.Window) the PySimpleGUI Window element
        current_player_: (int) the index of the current player. Can be 0 or 1.
        round_number_: (int) the number of the current round
    """
    grid_ = [[' ' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]     # create the game grid

    layout_ = create_connect_four_layout(COL_COUNT, ROW_COUNT, p_names)     # create the layout for the game window

    window_ = sg.Window('Connect 4 - PvB', layout_, size=(1200, 800),
                        resizable=True, element_justification='center')     # create the game window

    current_player_ = 0                 # create game variables
    round_number_ = 1

    return grid_, layout_, window_, current_player_, round_number_


def switch_player(cur_player: int):
    """
    This function switches the current player index.
    This needs to be called after every player move, if no game-ending condition (win, lose or draw) is met.

    :param cur_player: (int) index of the current player. Can be 0 or 1.
    :return: (int) returns the player index of the next player.
    """
    nxt_player = 1 if cur_player == 0 else 0    # switch the player id
    return nxt_player                           # return the id of the next player


def create_pop_up(p_names: list, winner_id: int):
    """
    This function creates a pop up when the end of the game is reached.
    Is can be a Draw or a Win Pop-Up. The player can chose to play another game or to return to the main menu.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :param winner_id: (int) the id of the winner. Can be 0 or 1 (or 2 if it is a draw)
    :return: p_choice (str) the choice of the player when one of the pop up buttons was clicked. Can be 'Yes' or 'No'.
    """
    p_colors = ['#6F3AFC', '#FCF060']       # set the color for both player
    if winner_id == 2:                      # winner_id is 2 when it is a draw
        pop_up_layout = [[sg.T('Draw!', font=('Helvetica', 30, 'bold'),
                               pad=(0, 5), justification='center', text_color='#FC9E47')],
                         [sg.T('The board is full.', font=('Helvetica', 15),
                               pad=(0, 30), justification='center', text_color="#FFF7E2")]]
    else:                                   # winner_id is 0 or 1
        pop_up_layout = [[sg.T(p_names[winner_id] + ' wins!', font=('Helvetica', 30, 'bold'),
                               pad=(0, 5), justification='center', text_color=p_colors[winner_id])]]

    pop_up_layout.append([[sg.T('Do you want to play again?', font=('Helvetica', 15),
                                pad=(0, 30), justification='center', text_color="#FFF7E2")],
                          [sg.No(s=10, button_color=('black', '#B8F1FF')),
                           sg.Yes(s=10, button_color=('black', '#FC9E47'))]])

    p_choice, _ = sg.Window('Game End', pop_up_layout,
                            disable_close=True).read(close=True)    # create a Window with 'Yes' and 'No' button and
                                                                    # save the players choice in the p_choice variable
    return p_choice                                                 # return that choice


# MAIN FUNCTION
def main(p_names: list):
    """
    This is the main function of the connect four game player against player.
    It sets up important game variables and settings and contains the main game loop.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :return: NO return value.
    """
    game_name = "c4"                                # needed in the save_score() function

    sg.SetOptions(font=('Helvetica', 18))           # set the font size of the window

    p_background_colors = ['#6F3AFC', '#FCF060']    # set the player colors
    p_text_colors = ['#FFF7E2', '#2C2825']

    grid, layout, window, current_player, round_number = create_game(p_names)   # setting up start variables

    # Game loop
    while True:
        event, values = window.read()               # get the button click event

        if event is None:                           # fail save
            break

        if event == 'Back':                         # when Back button is pressed, go back to the main menu
            window.close()
            main_menu.main()
            break

        if event == 'New Game':                      # when New Game button is pressed, create a new game
            window.close()
            grid, layout, window, current_player, round_number = create_game(p_names)   # create a new clean game board
            continue

        row, col = event                            # get the row and column of the clicked grid button

        # Update the grid and window if the column is not full
        if grid[0][col] == ' ':                         # if the top row of the clicked column is empty
            for r in range(ROW_COUNT - 1, -1, -1):      # check for every cell in the row (from bottom to top)
                if grid[r][col] == ' ':                 # if the specific cell is empty
                    grid[r][col] = current_player       # set this cell to the current_player
                    if current_player == 0:             # change the cell/button color according to the player
                        window[(r, col)].update(button_color=('white', p_background_colors[0]))
                    else:
                        round_number += 1               # after player 2 turn, add 1 to the round number
                        window['round_number'].update(f'Round: {round_number}')
                        window[(r, col)].update(button_color=('white', p_background_colors[1]))
                    break

            if check_win(grid, current_player):                         # check if the current player has won
                save_score(p_names, "Win", current_player, game_name)   # save the score of the winning player
                losing_player = 1 if current_player == 0 else 0
                save_score(p_names, "Lose", losing_player, game_name)   # save the score of the losing player
                choice = create_pop_up(p_names, current_player)         # create the win pop-up

                if choice == 'No':                  # check the players pop-up choice
                    window.close()                  # if player clicked 'No' go back to the main menu
                    main_menu.main()
                    break
                else:
                    window.close()                  # if the player clicked 'Yes' create a new clean game grid
                    grid, layout, window, current_player, round_number = create_game(p_names)
                    continue

            if check_full(grid):                            # check if the board is full
                save_score(p_names, "Draw", 0, game_name)   # save the scores for both players
                save_score(p_names, "Draw", 1, game_name)
                choice = create_pop_up(p_names, 2)          # create the pop-up with winner_id = 2, because it is a draw

                if choice == 'No':                  # check the players pop-up choice
                    window.close()                  # if player clicked 'No' go back to the main menu
                    main_menu.main()
                    break
                else:
                    window.close()                  # if the player clicked 'Yes' create a new clean game grid
                    grid, layout, window, current_player, round_number = create_game(p_names)
                    continue

            current_player = switch_player(current_player)  # switch the current player

            # update the current player text
            window['active_player'].update(f'Current Player: {p_names[current_player]}',
                                           background_color=p_background_colors[current_player],
                                           text_color=p_text_colors[current_player])
    window.close()      # close the window
