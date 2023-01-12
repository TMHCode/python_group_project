import PySimpleGUI as sg

from scripts.layouts import create_RPS_pvpp_layout

import PySimpleGUI as sg


def main(p_names: list):
    layout = create_RPS_pvpp_layout(p_names)
    window = sg.Window("Rock-Paper-Scissors", layout)
    player1_choice = None
    player2_choice = None
    player1_score = 0
    player2_score = 0
    while True:
        event, values = window.read()
        if event in (None, 'Quit'):
            break
        if player1_choice is None:
            player1_choice = event.lower()
            layout[0] = [sg.Text('Player 2 Select your move')]
        elif player2_choice is None:
            player2_choice = event.lower()
            layout[0] = [sg.Text('Player 1 Select your move')]
            result = determine_winner(player1_choice, player2_choice)
            if 'Player 1' in result:
                player1_score += 1
            elif 'Player 2' in result:
                player2_score += 1
            print(result, end='\n\n')
            print(f'Player 1 Score: {player1_score}',
                  f'Player 2 Score: {player2_score}')
            player1_choice = None
            player2_choice = None
    window.close()


def determine_winner(player1, player2):
    if player1 == player2:
        return "Tie"
    elif player1 == "rock":
        if player2 == "scissors":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1 == "paper":
        if player2 == "rock":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1 == "scissors":
        if player2 == "paper":
            return "Player 1 wins!"

if __name__ == '__main__':
    p_names = ['john', 'bot']
    main(p_names)
