import PySimpleGUI as sg

from scripts.menus import main_menu
from scripts.layouts import create_tic_tac_toe_layout
from scripts.statistics.stats import save_score


def create_game(p_names: list):
    # Create the layout of the game
    layout = create_tic_tac_toe_layout(p_names)

    # Create the window
    window = sg.Window('Tic-Tac-Toe', layout, size=(1100, 700), resizable=True, element_justification="center")

    # Create a list to store the state of the game
    board = [[0 for _ in range(3)] for _ in range(3)]

    return board, layout, window


def check_win_player1(board):
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


def check_win_player2(board):
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


def new_field(player, board, window):
    player = -player
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
            window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53"))


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
                player = -player
                window[event].update("O" if player == 1 else "X", button_color=("black", "#FC9E47" if player == 1 else "#B8F1FF"))


        # If the event is the "New Game" button, reset the board and switch players
        if event == "New Game":
            new_field(player, board, window)


        #Check if someone has won the game
        if check_win_player1(board):
            sg.popup(f"Player 'X has won!")
            save_score(p_names, "Win", 0, game_name)
            save_score(p_names, "Lose", 1, game_name)
            new_field(player, board, window)

        if check_win_player2(board):
            sg.popup(f"Player 'O has won!")
            save_score(p_names, "Lose", 0, game_name)
            save_score(p_names, "Win", 1, game_name)
            new_field(player, board, window)

        if check_draw(board):
            sg.popup(f"Draw")
            save_score(p_names, "Draw", 0, game_name)
            save_score(p_names, "Draw", 1, game_name)
            new_field(player, board, window)

        if player == 1:
            window['active_player'].update(f'Current Player: {p_names[0]}', background_color="#B8F1FF", text_color="black")
        elif player == -1:
            window['active_player'].update(f'Current Player: {p_names[1]}', background_color="#FC9E47", text_color="black")
        # Close the window
    window.close()



