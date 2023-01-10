import PySimpleGUI as sg
import random

# Set the theme for the GUI
sg.theme('DarkAmber')

# Set the layout for the main window
layout = [[sg.Text('Tic-Tac-Toe')],
          [sg.Button('', size=(4, 2), key=1), sg.Button('', size=(4, 2), key=2), sg.Button('', size=(4, 2), key=3)],
          [sg.Button('', size=(4, 2), key=4), sg.Button('', size=(4, 2), key=5), sg.Button('', size=(4, 2), key=6)],
          [sg.Button('', size=(4, 2), key=7), sg.Button('', size=(4, 2), key=8), sg.Button('', size=(4, 2), key=9)],
          [sg.Text('Your turn')],
          [sg.Button('New Game')]]

# Create the main window
window = sg.Window('Tic-Tac-Toe', layout)

# Set the initial board to be empty
board = [' ' for _ in range(9)]

# Set the player's letter to be X and the bot's letter to be O
player_letter = 'X'
bot_letter = 'O'

# Set the initial turn to be the player's turn
turn = 'player'

# Set the game to be ongoing
game_over = False

while True:
    # Get the next event
    event, values = window.read()

    # If the event is to close the window, exit the game
    if event == sg.WIN_CLOSED:
        break

    # If the event is to start a new game, reset the board and the turn
    if event == 'New Game':
        board = [' ' for _ in range(9)]
        window.find_all()[0].update(value='Your turn')
        window.find_all()[1].update(value='', disabled=False)
        window.find_all()[2].update(value='', disabled=False)
        window.find_all()[3].update(value='', disabled=False)
        window.find_all()[4].update(value='', disabled=False)
        window.find_all()[5].update(value='', disabled=False)
        window.find_all()[6].update(value='', disabled=False)
        window.find_all()[7].update(value='', disabled=False)
        window.find_all()[8].update(value='', disabled=False)
        turn = 'player'
        game_over = False

    # If the event is a button click, make a move
    if event in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        # If the game is over, do nothing
        if game_over:
            continue

        # If the space is not empty, do nothing
        if board[event - 1] != ' ':
            continue

    # Update the board with the player's move
    board[event - 1] = player_letter
    window.find_element(event).update(value=player_letter, disabled=True)

    # Check if the player has won
    if (board[0] == player_letter and board[1] == player_letter and board[2] == player_letter) or \
       (board[3] == player_letter and board[4] == player_letter and board[5] == player_letter) or \
       (board[6] == player_letter and board[7] == player_letter and board[8] == player_letter) or \
       (board[0] == player_letter and board[3] == player_letter and board[6] == player_letter) or \
       (board[1] == player_letter and board[4] == player_letter and board[7] == player_letter) or \
       (board[2] == player_letter and board[5] == player_letter and board[8] == player_letter) or \
       (board[0] == player_letter and board[4] == player_letter and board[8] == player_letter) or \
       (board[2] == player_letter and board[4] == player_letter and board[6] == player_letter):
        window.find_element(0).update(value='You won!')
        game_over = True
        continue

    # Check if the board is full
    if ' ' not in board:
        window.find_element(0).update(value='The game is a tie!')
        game_over = True
        continue

    # Change the turn to the bot's turn
    turn = 'bot'
    window.find_element(0).update(value='Bot\'s turn')

    # Have the bot make a move
    move = random.choice([i for i in range(9) if board[i] == ' '])
    board[move] = bot_letter
    window.find_element(move + 1).update(value=bot_letter, disabled=True)

    # Check if the bot has won
    if (board[0] == bot_letter and board[1] == bot_letter and board[2] == bot_letter) or \
            (board[3] == bot_letter and board[4] == bot_letter and board[5] == bot_letter) or \
            (board[6] == bot_letter and board[7] == bot_letter and board[8] == bot_letter) or \
            (board[0] == bot_letter and board[3] == bot_letter and board[6] == bot_letter) or \
            (board[1] == bot_letter and board[4] == bot_letter and board[7] == bot_letter) or \
            (board[2] == bot_letter and board[5] == bot_letter and board[8] == bot_letter) or \
            (board[0] == bot_letter and board[4] == bot_letter and board[8] == bot_letter) or \
            (board[2] == bot_letter and board[4] == bot_letter and board[6] == bot_letter):
        window.find_element(0).update(value='The bot won!')
        game_over = True
        continue

    # Change the turn back to the player's turn
    turn = 'player'
    window.find_element(0).update(value='Your turn')

# Close the window
window.close()

