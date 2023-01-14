import PySimpleGUI as sg

from scripts.games.connect_four import connect_four
from scripts.games.tic_tac_toe import tic_tac_toe_1vs1
from scripts.games.rock_paper_scissors import PVP
from scripts.menus import main_menu
from scripts.layouts import create_pvp_name_menu_layout
"""
This is the PVP name menu file.
"""


def main(game: str):
    """
    This is the main function of the PVP (Player vs. Player) name menu.
    It shows the PVP Name Menu, where the users must enter their names in order to play the game.
    It loads the pvp-name-menu-layout and window and determines the button events for this menu.

    :param game: (str)  name of the game. Can be 'ttt', 'c4' or 'rps'
    :return:  NO return parameter.
    """

    # Create the layout
    layout = create_pvp_name_menu_layout(game)

    # Create the window
    window = sg.Window('Name Menu', layout, size=(1200, 800), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            main_menu.main()
            break
        elif event == 'Continue':
            if values['input_p1_name'] == '' or values['input_p2_name'] == '':
                sg.popup('Player name(s) can\'t be empty!')
                continue
            window.close()
            if game == 'Connect Four':
                connect_four.main([values['input_p1_name'], values['input_p2_name']])
            elif game == 'Rock-Paper-Scissors':
                PVP.main()
            elif game == 'Tic-Tac-Toe':
                tic_tac_toe_1vs1.main([values['input_p1_name'], values['input_p2_name']])
            break

    window.close()
