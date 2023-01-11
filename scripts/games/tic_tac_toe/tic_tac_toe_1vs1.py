import PySimpleGUI as sg

from scripts.menus import main_menu
from scripts.layouts import create_tic_tac_toe_layout


def check_win(player, board, window):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            sg.popup(f"Player {'X' if board[row][0] == 1 else 'O'} has won!")
            new_field(player, board, window)

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            sg.popup(f"Player {'X' if board[0][col] == 1 else 'O'} has won!")
            new_field(player, board, window)

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        sg.popup(f"Player {'X' if board[0][0] == 1 else 'O'} has won!")
        new_field(player, board, window)

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        sg.popup(f"Player {'X' if board[0][2] == 1 else 'O'} has won!")
        new_field(player, board, window)


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


def main():

    sg.ChangeLookAndFeel("DarkAmber")
    # Create the layout of the game
    layout = create_tic_tac_toe_layout()

    # Create the window
    window = sg.Window('Tic-Tac-Toe', layout, size=(1100, 700), resizable=True, element_justification="center")

    # Create a list to store the state of the game
    board = [[0 for _ in range(3)] for _ in range(3)]

    # Create a player
    player = 1

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
        check_win(player, board, window)
        if check_draw(board):
            sg.popup(f"Draw")
            new_field(player, board, window)

        # Close the window
    window.close()


if __name__ == '__main__':
    main()
