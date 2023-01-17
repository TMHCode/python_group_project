import PySimpleGUI as sg

from scripts.menus import main_menu
from scripts.layouts import create_tic_tac_toe_layout
from scripts.statistics.stats import save_score


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


def check_win_player1(board: list):

    """
       This function checks the win conditions for Tic-Tac-Toe for Player 1.
       There are three win conditions that need to be checked after every move:
           - are there 3 X in a row
           - are there 3 X in a column
           - are there 3 X diagonally

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


def check_win_player2(board: list):

    """
           This function checks the win conditions for Tic-Tac-Toe for Player 2.
           There are three win conditions that need to be checked after every move:
               - are there 3 O in a row
               - are there 3 O in a column
               - are there 3 X diagonally

           :param board: (list) a list of lists that is representing the playing field.
                           list-structure: [[row 1], [row 2], [row 3]]


           :return: (bool) returns True if player 2 wins and False if player 2 does not win.
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
    player = -player                # switches player
    for row in range(3):
        for col in range(3):
            board[row][col] = 0     # set all fields to 0
            window[(row, col)].update(" ", button_color=("#FCCB53", "#FCCB53")) # updates window


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

    #sets up variables to start the game
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
            row, col = event                              # gets row and column from the button click,used for the board
            if board[row][col] == 0:                      # checks if board field is empty
                board[row][col] = player                  # if so assigns field to current player
                player = -player                          # switches player
                window[event].update("O" if player == 1 else "X",
                                     button_color=("black", "#FC9E47" if player == 1 else "#B8F1FF"))   # updates board field with respective symbol

        # If the event is the "New Game" button, calls new_field function (resets field)
        if event == "New Game":
            new_field(player, board, window)

        # Check if player 1 has won the game
        if check_win_player1(board):
            sg.popup(f"Player 'X has won!")             # creates a pop that player 1 has won
            save_score(p_names, "Win", 0, game_name)    # saves a win for player 1 in ttt
            save_score(p_names, "Lose", 1, game_name)   # saves a lose for player 2 in ttt
            new_field(player, board, window)            # creates a new field

        if check_win_player2(board):
            sg.popup(f"Player 'O has won!")             # creates a pop that player 1 has won
            save_score(p_names, "Lose", 0, game_name)   # saves a win for player 2 in ttt
            save_score(p_names, "Win", 1, game_name)    # saves a lose for player 1 in ttt
            new_field(player, board, window)            # creates a new field

        if check_draw(board):
            sg.popup(f"Draw")                           # creates a pop that the game is a draw
            save_score(p_names, "Draw", 0, game_name)   # saves a draw for player 1 in ttt
            save_score(p_names, "Draw", 1, game_name)   # saves a draw for player 2 in ttt
            new_field(player, board, window)            # creates a new field

        # checks if current player is player 1 and changes respective line in game info to player 1 color
        if player == 1:
            window['active_player'].update(f'Current Player: {p_names[0]}', background_color="#B8F1FF", text_color="black")
        # checks if current player is player 2 and changes respective line in game info to player 2 color
        elif player == -1:
            window['active_player'].update(f'Current Player: {p_names[1]}', background_color="#FC9E47", text_color="black")
        # Close the window
    window.close()



