import PySimpleGUI as sg
from random import randrange

import pickle

from scripts.menus import main_menu
from scripts.layouts import create_tic_tac_toe_layout


def create_game(p_names: list):
    # Create the layout of the game
    layout = create_tic_tac_toe_layout(p_names)

    # Create the window
    window = sg.Window('Tic-Tac-Toe', layout, size=(1100, 700), resizable=True, element_justification="center")

    # Create a list to store the state of the game
    board = [[0 for _ in range(3)] for _ in range(3)]

    return board, layout, window


def check_win_player(board):
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
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def new_field(player,board,window):
    player = -player
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
            window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))


def bot_move(player, board, window):
    # Check for potential winning moves for the bot
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = -player
                if check_win_bot(board):
                    # Make the winning move
                    window[(row, col)].update("O", button_color=("black", "#FC9E47"))
                    return
                else:
                    board[row][col] = 0

    # check for potential winning moves for the player and block it
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = player
                if check_win_player(board):
                    # Block the potential winning move for the player by making the same move for the bot
                    board[row][col] = -player
                    window[(row, col)].update("O", button_color=("black", "#FC9E47"))
                    return
                else:
                    board[row][col] = 0
    # If there is no potential winning move for the bot, make a random move
    while True:
        row = randrange(3)
        col = randrange(3)
        if board[row][col] == 0:
            board[row][col] = -player
            window[(row, col)].update("O", button_color=("black", "#FC9E47"))
            break


def save_score(p_names, result, index, game_name):
    # Get the desired player name from the list
    p_name = p_names[index]

    # Open the file in append mode
    with open("scores.txt", "a") as file:
        file.write(p_name + " " + result + " " + game_name + "\n")
def main(p_names: list):

    # Create a player
    player = 1

    game_name = "ttt"

    board, layout, window = create_game(p_names)
    # Main game loop
    while True:
        # Read the window
        event, values = window.read()

        # If the window was closed, break out of the loop
        if event is None:
            break

        if event == 'Back':
            window.close()
            main_menu.main()
            break

        # If the event is a button press, update the board and switch players
        if isinstance(event, tuple):
            row, col = event
            if board[row][col] == 0:
                board[row][col] = player
                #print(board[row][col])
                window[event].update("X", button_color=("black", "#B8F1FF"))
                if check_win_player(board):
                    sg.popup(f"Player 'X' has won!")
                    save_score(p_names, "Win", 0, game_name)
                    new_field(player, board, window)
                    continue
                if not check_draw(board):
                    bot_move(player, board, window)
                    if check_win_bot(board):
                        sg.popup(f"Player 'O' has won!")
                        save_score(p_names, "Lose", 0, game_name)
                        new_field(player, board, window)

        # If the event is the "New Game" button, reset the board and switch players
        if event == "New Game":
            new_field(player, board, window)

        if check_draw(board):
            sg.popup(f"Draw")
            new_field(player, board, window)
            save_score(p_names, "Draw", 0, game_name)

        # Close the window
    window.close()




