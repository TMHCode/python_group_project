import PySimpleGUI as sg

from scripts.menus import pvp_name_menu, pvb_name_menu
from scripts.layouts import create_mode_menu_layout
from scripts.menus import main_menu
"""
This is the mode menu file.
"""


def main(game):
    """
    This is the main function of the game-mode menu.
    It shows the game-mode Menu, where the user can chose to play against another user or against a (simple) bot.
    It loads the mode-menu-layout and window and determines the button events for this menu.

    :param game: (str)  name of the game. Can be 'ttt', 'c4' or 'rps'
    :return:  NO return parameter.
    """
    # Create the layout
    layout = create_mode_menu_layout(game)

    # Create the window
    window = sg.Window('Game Mode Menu', layout, size=(1200, 800), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Back'):

            window.close()
            main_menu.main()
            break
        elif event == 'Player vs. Player':
            window.close()
            pvp_name_menu.main(game)
            break
        elif event == 'Player vs. Bot':
            window.close()
            pvb_name_menu.main(game)
            break

    window.close()
