import PySimpleGUI as sg
import random

from scripts.layouts import create_rps_layout
from scripts.menus import main_menu
from scripts.statistics.stats import save_score


def main(p_names: list):
    sg.theme('DarkAmber')
    game_name = "rps"

    layout = create_rps_layout(p_names)
    window = sg.Window('Rock-Paper-Scissors', layout, size=(1200, 800), resizable=True, element_justification='center')
    score = {'wins': 0, 'losses': 0, 'ties': 0}
    score_text = window['-SCORE-']

    while True:
        event, values = window.read()
        if event in (None, 'Quit'):
            window.close()
            main_menu.main()
            break
        elif event in (None, 'New'):
            score = {'wins': 0, 'losses': 0, 'ties': 0}
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        outcome = compare(event, computer_choice)

        if outcome == 'win':
            score['wins'] += 1
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            save_score(p_names, "Win", 0, game_name)
            sg.popup(f'You chose {event}. Bot choses {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="green")
        elif outcome == 'lose':
            score['losses'] += 1
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            save_score(p_names, "Lose", 0, game_name)
            sg.popup(f'You chose {event}. Computer chose {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="red")
        elif outcome == 'tie':
            score['ties'] += 1
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            save_score(p_names, "Draw", 0, game_name)
            sg.popup(f'You chose {event}. Computer chose {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="yellow")

    window.close()


def compare(player, computer):
    if player == "Rock":
        if computer == "Paper":
            return 'lose'
        elif computer == "Rock":
            return 'tie'
        elif computer == "Scissors":
            return 'win'
    elif player == "Paper":
        if computer == "Scissors":
            return 'lose'
        elif computer == "Paper":
            return 'tie'
        elif computer == "Rock":
            return 'win'
    elif player == "Scissors":
        if computer == "Rock":
            return 'lose'
        elif computer == "Scissors":
            return 'tie'
        elif computer == "Paper":
            return 'win'
    else:
        pass


if __name__ == '__main__':
    p_names = ['john', 'bot']
    main(p_names)
