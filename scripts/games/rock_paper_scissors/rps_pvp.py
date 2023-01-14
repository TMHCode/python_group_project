import PySimpleGUI as sg

from scripts.layouts import create_RPS_pvp_layout
from scripts.menus import main_menu
from scripts.statistics.stats import save_score

"""
This is the file for the rock paper scissor game player versus player.
It contains the functions that are necessary to play the game and the main game loop.
"""


def disable_p1(window):
    """
    This function disable the three buttons of Player 1 and
    activate the three buttons of Player 2.
    This needs to be called every time after Player 1 choose a Button.

    :param window:  parameter for (sg.Window) the PySimpleGUI Window element
    :return: (bool) returns True or False if button need to be disabled

    """
    window['p1-rock'].update(disabled=True)  # block button Rock from Player 1
    window['p1-paper'].update(disabled=True)  # block button Paper from Player 1
    window['p1-scissors'].update(disabled=True)  # block button Scissors from Player 1

    window['p2-rock'].update(disabled=False)  # activate button Rock from Player 2
    window['p2-paper'].update(disabled=False)  # activate button Paper from Player 2
    window['p2-scissors'].update(disabled=False)  # activate button Scissors from Player 2
    return window  # return parameter true or false


def block_p(window):
    """
        Exact same function as disable_p1, just disabled all the buttons.
        This function disable the all buttons of Player 2 and 1.
        Show Button need to be active so the players need to choose the other buttons first.
        This needs to be called every time after Player 2 choses a button.

        :param window:  parameter for (sg.Window) the PySimpleGUI Window element
        :return: (bool) returns True or False if button need to be disabled

        """
    window['p1-rock'].update(disabled=True)
    window['p1-paper'].update(disabled=True)
    window['p1-scissors'].update(disabled=True)

    window['p2-rock'].update(disabled=True)
    window['p2-paper'].update(disabled=True)
    window['p2-scissors'].update(disabled=True)

    window['Show'].update(disabled=False) #active the show button
    return window


def disable_p2(window):
    """
    Exact same function as disable_p1, just reversed.
    This function disable the three buttons of Player 2 and
    activate the three buttons of Player 1.
    Show Button need to be redisabled so the players need to choose the other buttons first.
    This needs to be called every time after Show is clicked to begin new.

    :param window:  parameter for (sg.Window) the PySimpleGUI Window element
    :return: (bool) returns True or False if button need to be disabled

    """
    window['p1-rock'].update(disabled=False)
    window['p1-paper'].update(disabled=False)
    window['p1-scissors'].update(disabled=False)

    window['p2-rock'].update(disabled=True)
    window['p2-paper'].update(disabled=True)
    window['p2-scissors'].update(disabled=True)

    window['Show'].update(disabled=True)  # button show will be disabled
    return window


def main(p_names: list):
    """
     This is the main function of the Rock paper scissor game player versus player.
    It sets up important game variables and settings and contains the main game loop.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :return: NO return value.
    """

    game_name = 'rps'                   # name of game, need in the save_score() function

    layout = create_RPS_pvp_layout(p_names)  # setting up start variables
    window = sg.Window('Rock-Paper-Scissors', layout, size=(1200, 800), resizable=True, element_justification='center') #create window

    p1 = 'p1'
    p2 = 'p2'

    while True:

        event, values = window.Read()
        if event in (None, 'Back'):
            window.close()
            main_menu.main()
            break

        elif event == 'p1-rock':
            p1 = 'rock'
            window = disable_p1(window)

        elif event == 'p1-paper':
            p1 = 'paper'
            window = disable_p1(window)

        elif event == 'p1-scissors':
            p1 = 'scissors'
            window = disable_p1(window)

        elif event == 'p2-rock':
            p2 = 'rock'
            window = block_p(window)

        elif event == 'p2-paper':
            p2 = 'paper'
            window = block_p(window)

        elif event == 'p2-scissors':
            p2 = 'scissors'
            window = block_p(window)

        elif event == 'Show':
            if p1 == p2:
                save_score(p_names, "Draw", 0, game_name)
                save_score(p_names, "Draw", 1, game_name)
                sg.Popup('Draw')
                p1 = 'p1'
                p2 = 'p2'
                window = disable_p2(window)

            elif (p1 == 'rock' and p2 == 'scissors') or \
                    (p1 == 'scissors' and p2 == 'paper') or (
                    p1 == 'paper' and p2 == 'rock'):
                save_score(p_names, "Win", 0, game_name)
                save_score(p_names, "Lose", 1, game_name)
                sg.Popup(f'{p_names[0]} wins!', text_color='#6F3AFC')
                p1 = 'p1'
                p2 = 'p2'
                window = disable_p2(window)
            else:
                save_score(p_names, "Win", 1, game_name)
                save_score(p_names, "Lose", 0, game_name)
                sg.Popup(f'{p_names[1]} wins!', text_color='#B8F1FF')
                p1 = 'p1'
                p2 = 'p2'
                window = disable_p2(window)

    window.Close()
