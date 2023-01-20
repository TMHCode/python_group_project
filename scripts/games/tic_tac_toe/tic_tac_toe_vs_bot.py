import PySimpleGUI as sg
from random import randrange

import pickle

from menus import main_menu
from layouts import create_tic_tac_toe_layout
from statistics.stats import save_score


def create_game(p_names: list):

    """
        This function creates the first game board


        :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
        :return:
            board: (list) a list of lists that is representing the playing field.
                        list-structure: [[row 1], [row 2], [row 3]]

            layout: (list) a list that contains the layout for this window

            window: (sg.Window) the PySimpleGUI Window element
    """

    # Create the layout of the game
    layout = create_tic_tac_toe_layout(p_names)

    # Create the window
    window = sg.Window('Tic-Tac-Toe', layout, size=(1100, 700), resizable=True, element_justification="center")

    # Create a list to store the state of the game
    board = [[0 for _ in range(3)] for _ in range(3)]

    return board, layout, window


def check_win_player(board):

    """
          This function checks the win conditions for Tic-Tac-Toe for Player 1.
          There are three win conditions that need to be checked after every move:
              - are there 3 X's in a row
              - are there 3 X's in a column
              - are there 3 X's diagonally

          :param board: (list) a list of lists that is representing the playing field.
                          list-structure: [[row 1], [row 2], [row 3]]

          :return: (bool) returns True if player 1 wins and False if player 1 does not win.
    """

    if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or \
            (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or \
            (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or \
            (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or \
            (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or \
            (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or \
            (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or \
            (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        return True
    return False


def check_win_bot(board):

    """
              This function checks the win conditions for Tic-Tac-Toe for the Bot.
              There are three win conditions that need to be checked after every move:
                  - are there 3 O's in a row
                  - are there 3 O's in a column
                  - are there 3 O's diagonally

              :param board: (list) a list of lists that is representing the playing field.
                              list-structure: [[row 1], [row 2], [row 3]]


              :return: (bool) returns True if the Bot wins and False if the Bot does not win.
    """

    if (board[0][0] == -1 and board[0][1] == -1 and board[0][2] == -1) or \
            (board[1][0] == -1 and board[1][1] == -1 and board[1][2] == -1) or \
            (board[2][0] == -1 and board[2][1] == -1 and board[2][2] == -1) or \
            (board[0][0] == -1 and board[1][0] == -1 and board[2][0] == -1) or \
            (board[0][1] == -1 and board[1][1] == -1 and board[2][1] == -1) or \
            (board[0][2] == -1 and board[1][2] == -1 and board[2][2] == -1) or \
            (board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1) or \
            (board[0][2] == -1 and board[1][1] == -1 and board[2][0] == -1):
        return True
    return False

def check_draw(board):

    """
            This function checks if the board is full which results in a draw.
            This needs to be checked after every move.

            :param board: (list) a list of lists that is representing the playing field.
                            list-structure: [[row 1], [row 2], [row 3]]

            :return: (bool) returns True if the grid is full and False if there is still an empty cell.
    """

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def new_field(player, board, window):

    """
            This function creates a clean new game board.
            This needs to be called every time before a new game is starting.

            :param player: (int) a variable which assigns 1 for player 1 and -1 for player 2
                            used to switch players
            :param board: (list) a list of lists that is representing the playing field.
                            list-structure: [[row 1], [row 2], [row 3]]

            :param window:  window: (sg.Window) the PySimpleGUI Window element
                            used to update the current window

            :return: NO return value.

    """

    player = -player
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
            window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))


def bot_move(player, board, window):

    """
        This function simulates the bots turn.
        The Bot tries to prevent the player from winning
        The Bot makes his moves randomly unless the next move could win the game for the bot

       :param board: (list) a list of lists that is representing the playing field.
                            list-structure: [[row 1], [row 2], [row 3]]

        :param window: (sg.Window) the PySimpleGUI Window element


    """

    # Check for potential winning moves for the bot
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:            # checks if board field is empty
                board[row][col] = -player       # fills board field with a -1 for the bot
                if check_win_bot(board):        # checks if the bot can win
                    # Makes the winning move
                    window[(row, col)].update("O", button_color=("black", "#FC9E47")) # updates window, fills chosen field with O
                    return
                else:
                    board[row][col] = 0         # if bot would not win makes field empty again

    # check for potential winning moves for the player and block it
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:          # checks if board field is empty
                board[row][col] = player      # fills board field with a -1 for the bot
                if check_win_player(board):   # checks if the player can win
                    # Block the potential winning move for the player by making the same move for the bot
                    board[row][col] = -player # fills board field with a -1 for the bot
                    window[(row, col)].update("O", button_color=("black", "#FC9E47"))   # updates window, fills chosen field with O
                    return
                else:
                    board[row][col] = 0       # if bot would not win makes field empty again
    # If there is no potential winning move for the bot, make a random move
    while True:
        row = randrange(3)
        col = randrange(3)
        if board[row][col] == 0:              # checks if any board field is empty
            board[row][col] = -player         # fills board field with a -1 for the bot
            window[(row, col)].update("O", button_color=("black", "#FC9E47"))   # updates window, fills chosen field with O
            break


def main(p_names: list):

    """
            This is the main function of Tic-Tac-Toe game player vs. player.
            It sets up important game variables and settings and contains the main game loop.

            :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']

            :return: NO return value.
    """

    # Create a player and assigns 1
    player = 1

    # Variable used in save_score(), shows which game was played
    game_name = "ttt"

    # sets up variables to start the game
    board, layout, window = create_game(p_names)

    # Main game loop
    while True:
        # Read the window, used to get the button clicks
        event, values = window.read()

        # If the window was closed, breaks out of the loop and ends program
        if event is None:
            break

        # If the back button is pressed, returns to the main menu
        if event == 'Back':
            window.close()
            main_menu.main()
            break

        # If the event is a button press, update the board and switch players
        if isinstance(event, tuple):
            row, col = event                                                    # gets row and column from the button click,used for the board
            if board[row][col] == 0:                                            # checks if board field is empty
                board[row][col] = player                                        # if so assigns field to current player
                window[event].update("X", button_color=("black", "#B8F1FF"))    # updates board field with respective symbol
                if check_win_player(board):                                     # Check if player 1 has won the game
                    sg.popup(f"Player 'X' has won!")                            # creates a pop that player 1 has won
                    save_score(p_names, "Win", 0, game_name)                    # saves a win for player 1 in ttt
                    new_field(player, board, window)                            # creates a new field
                    continue
                if not check_draw(board):                                        # Check if the game is a draw
                    bot_move(player, board, window)                              # make the bot_move
                    if check_win_bot(board):                                     # Check if the bot has won the game
                        sg.popup(f"Player 'O' has won!")                         # creates a pop that the bot has won
                        save_score(p_names, "Lose", 0, game_name)                # saves a lose for player 1 in ttt
                        new_field(player, board, window)

        # If the event is the "New Game" button, reset the board
        if event == "New Game":
            new_field(player, board, window)

        # Check if the game is a draw
        if check_draw(board):
            sg.popup(f"Draw")
            new_field(player, board, window)            # creates a new field
            save_score(p_names, "Draw", 0, game_name)   # saves a draw for player 1 in ttt

        # Close the window
    window.close()




