import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Player 1'), sg.Button('Rock', key='p1rock'), sg.Button('Paper', key='p1paper'),
     sg.Button('Scissors', key='p1scissors')],
    [sg.Text('Player 2'), sg.Button('Rock', key='p2rock'), sg.Button('Paper', key='p2paper'),
     sg.Button('Scissors', key='p2scissors')],
    [sg.Text('', size=(40, 1), key='result')],
    [sg.Text("Result:", size=(15, 1), font=("Helvetica", 14), text_color="yellow"),
     sg.Text("", size=(20, 1), key="result", font=("Helvetica", 14), text_color="red")]
]

window = sg.Window('Rock-Paper-Scissors', layout)


# Function to determine the winner
def get_winner(p1_move, p2_move):
    if p1_move == p2_move:
        return "Tie"
    elif p1_move == 'rock' and p2_move == 'scissors':
        return "Player 1 wins!"
    elif p1_move == 'paper' and p2_move == 'rock':
        return "Player 1 wins!"
    elif p1_move == 'scissors' and p2_move == 'paper':
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


player1_move = None
player2_move = None

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event.startswith('p1'):
        player1_move = event[3:]
        if player2_move is not None:
            result = get_winner(player1_move, player2_move)
            window['result'].update(f"Player 1 played {player1_move} and Player 2 played {player2_move}.\n{result}")
            player1_move = None
            player2_move = None
    elif event.startswith('p2'):
        player2_move = event[3:]
        if player1_move is not None:
            result = get_winner(player1_move, player2_move)
            window['result'].update(f"Player 1 played {player1_move} and Player 2 played {player2_move}.\n{result}")
            player1_move = None
            player2_move = None

window.close()
