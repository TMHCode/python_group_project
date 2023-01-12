import random

import PySimpleGUI as sg

sg.theme('DarkAmber')


# Define the possible choices the player can make
player_choices = ["rock", "paper", "scissors"]

# Define the possible choices the computer can make
computer_choices = ["rock", "paper", "scissors"]

# Define a dictionary that maps each choice to the choices it beats
winners = dict(rock=["scissors"], paper=["rock"], scissors=["paper"])

# Define a list that will keep track of the player's and computer's scores
scores = [0, 0]


# Define a function that will handle button clicks
def button_click(choice):
    # Set the player's choice
    player_choice = choice

    # Choose a random choice for the computer
    computer_choice = random.choice(computer_choices)

    # Update the player choice label
    player_choice_label.update(player_choice.capitalize())

    # Update the computer choice label
    computer_choice_label.update(computer_choice.capitalize())

    # Determine the outcome of the game
    if player_choice == computer_choice:
        result_label.update("It's a tie!")
    elif player_choice in winners[computer_choice]:
        result_label.update("You lose!")
        scores[1] += 1
    else:
        result_label.update("You win!")
        scores[0] += 1

    # Update the scores label
    scores_label.update("Player: %d, Computer: %d" % (scores[0], scores[1]))


# Create the main window
window = sg.Window("Rock-Paper-Scissors", layout=[
    [sg.Text("Make your choice:", font=("Helvetica", 16), text_color="yellow")],
    [sg.Button("Rock", button_color=("white", "black"), key="rock"),
     sg.Button("Paper", button_color=("white", "black"), key="paper"),
     sg.Button("Scissors", button_color=("white", "black"), key="scissors")],
    [sg.Text("Player's choice:", font=("Helvetica", 14), text_color="yellow"),
     sg.Text("", size=(20, 1), key="player_choice", font=("Helvetica", 14), text_color="red")],
    [sg.Text("Computer's choice:", font=("Helvetica", 14), text_color="yellow"),
     sg.Text("", size=(20, 1), key="computer_choice", font=("Helvetica", 14), text_color="red")],
    [sg.Text("Result:", size=(15, 1), font=("Helvetica", 14), text_color="yellow"),
     sg.Text("", size=(20, 1), key="result", font=("Helvetica", 14), text_color="red")],
    [sg.Text("Scores:", size=(15, 1), font=("Helvetica", 14), text_color="yellow"),
     sg.Text("", size=(20, 1), key="scores", font=("Helvetica", 14), text_color="red")],

    [sg.Button('Quit', key='quit')]
])

# Get the player choice label and computer choice label from the window
player_choice_label = window["player_choice"]
computer_choice_label = window["computer_choice"]

# Get the result label and scores label from the window
result_label = window["result"]
scores_label = window["scores"]

# Start the event loop
while True:
    # Wait for an event
    event, values = window.read()

    # if the player closes the window or clicks the Quit button
    if event in (None, 'quit'):
        break

    # If the window was closed, break out of the loop
    if event == sg.WIN_CLOSED:
        break

    # If a button was clicked, handle the button click
    if event in player_choices:
        button_click(event)

# Close the window
window.close()
