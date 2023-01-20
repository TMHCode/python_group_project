import PySimpleGUI as sg

from menus import pvp_name_menu, pvb_name_menu
from layouts import create_mode_menu_layout
from menus import main_menu
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
    layout = create_mode_menu_layout(game)                                          # create the layout

    window = sg.Window('Game Mode Menu', layout, size=(1200, 800), resizable=True)  # create the window

    # Main Loop
    while True:
        event, values = window.read()                           # get the button click event
        if event in (sg.WIN_CLOSED, 'Back'):                    # when Back button is pressed, go back to the main menu
            window.close()
            main_menu.main()
            break
        elif event == 'Player vs. Player':                      # whatever button is pressed,
            window.close()
            pvp_name_menu.main(game)                            # open the respective menu
            break
        elif event == 'Player vs. Bot':
            window.close()
            pvb_name_menu.main(game)
            break

    window.close()                                              # close the window
