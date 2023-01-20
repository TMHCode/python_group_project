import PySimpleGUI as sg
import random

from layouts import create_rps_layout
from menus import main_menu
from statistics.stats import save_score


def compare(player, computer):  # function check game rules
    """
    This is the Game Rule function of Rock paper scissor game player vs bot.
    It compares the choices with the choices from the bot and return the result.
    :param player: get button event (player choice)
    :param computer: get random choice of bot
    :return: result value of the game
    """
    if player == "Rock":
        if computer == "Paper":
            return 'lose'  # return result
        elif computer == "Rock":
            return 'tie'  # return result
        elif computer == "Scissors":
            return 'win'  # return result
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


def main(p_names: list):
    """
     This is the main function of the Rock paper scissor game player versus bot.
    It sets up important game variables and settings and contains the main game loop.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'bot']
    :return: NO return value.
    """
    sg.theme('DarkAmber')
    game_name = "rps"  # name of game, need in the save_score() function

    layout = create_rps_layout(p_names)  # get values for the layout from function in scripts 'layouts'
    window = sg.Window('Rock-Paper-Scissors', layout, size=(1200, 800), resizable=True, element_justification='center')
    # create window
    score = {'wins': 0, 'losses': 0, 'ties': 0}  # init scoreboard
    score_text = window['-SCORE-']  # get result-text

    # Game loop
    while True:
        event, values = window.read()  # get the button click event
        if event in (None, 'Back'):  # when Back button is pressed, go back to the main menu
            window.close()
            main_menu.main()
            break
        elif event in (None, 'New'):  # when New button is pressed, create a new game
            score = {'wins': 0, 'losses': 0, 'ties': 0}  # reset scoreboard
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            # show reseted scoreboard
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])  # generate random choice of bot
        outcome = compare(event, computer_choice)  # check event choice with generated choice of bot
        # check if the player has won
        # return of result as outcome

        if outcome == 'win':  # if clause if result is win
            score['wins'] += 1  # add 1 to wins in scoreboard
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            # show result
            save_score(p_names, "Win", 0, game_name)  # save the score of the winning player
            sg.popup(f'You chose {event}. Bot chooses {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="green")  # show popup what the bot choose and show what the player choose
        elif outcome == 'lose':  # if result is lose
            score['losses'] += 1  # add 1 to lose in scoreboard
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            # update score
            save_score(p_names, "Lose", 0, game_name)  # save the score of the winning player
            sg.popup(f'You chose {event}. Computer chose {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="red")  # show popup what the bot choose and show what the player choose
        elif outcome == 'tie':  # result is tie
            score['ties'] += 1  # add 1 to tie in scoreboard
            score_text.update(f'Score: {score["wins"]} wins, {score["losses"]} losses, {score["ties"]} ties')
            save_score(p_names, "Draw", 0, game_name)  # save the score of the winning player
            sg.popup(f'You chose {event}. Computer chose {computer_choice}. You \n{outcome}', font=("Helvetica", 20),
                     text_color="yellow")

    window.close()   # close the window
