import PySimpleGUI as sg
import random
import pickle
import os


# Save the player's name and score to a file
def save_data(name, score):
    data = {'name': name, 'score': score}
    with open("../../../data.pkl", "wb") as file:
        pickle.dump(data, file)


# Load the player's name and score from a file
def load_data():
    with open("../../../data.pkl", "rb") as file:
        return pickle.load(file)


def main():
    sg.theme('DarkAmber')

    player_name = ''
    layout = [[sg.Text('Enter your name:')],
              [sg.InputText(key='-NAME-')],
              [sg.Button('Start'), sg.Button('Quit')]]

    window = sg.Window('Rock-Paper-Scissors', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Quit'):
            break
        elif event == 'Start':
            player_name = values['-NAME-']
            window.close()
            break

    rock_img = "stone.png"
    paper_img = "paper.png"
    scissors_img = "scissor.png"

    layout = [[sg.Text("Make your choice:", font=("Helvetica", 26), text_color="yellow")],
              [sg.Button('', image_filename=rock_img, button_color="white", key="Rock", image_subsample=2),
               sg.Button('', image_filename=paper_img, button_color='#ea8953', key="Paper", image_subsample=2),
               sg.Button('', image_filename=scissors_img, button_color='#c7aee4', key="Scissors",
                         image_subsample=2)],
              [sg.Text('', key='-OUTCOME-')],
              [sg.Text('Score: 0 wins, 0 losses, 0 ties', key='-SCORE-', font=("Arial", 20))],
              [sg.Button('New', size=(10, 10), font=("Arial", 20)),
               sg.Button('Safe', size=(10, 10), font=("Arial", 20)),
               sg.Button('Quit', size=(10, 10), font=("Arial", 20))]]

    window = sg.Window('Rock-Paper-Scissors', layout, size=(1100, 500), resizable=True, element_justification='center')
    score = {'wins': 0, 'losses': 0, 'ties': 0}
    score_text = window['-SCORE-']

    while True:
        event, values = window.read()
        if event in (None, 'Quit'):
            break
        elif event in (None, 'Safe'):
            save_data(player_name, score)
            loaded_data = load_data()
            sg.popup(loaded_data)  # (0, 0, 0)
            break
        elif event in (None, 'New'):
            score = {'wins': 0, 'losses': 0, 'ties': 0}
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        outcome = compare(event, computer_choice)

        if outcome == 'win':
            score['wins'] += 1
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            sg.popup(f'You chose {event}. Computer chose {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="green")
        elif outcome == 'lose':
            score['losses'] += 1
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            sg.popup(f'You chose {event}. Computer chose {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="red")
        elif outcome == 'lose':
            score['ties'] += 1
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
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
    main()
