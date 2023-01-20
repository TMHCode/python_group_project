import PySimpleGUI as sg

from games.connect_four import connect_four_bot
from games.tic_tac_toe import tic_tac_toe_vs_bot
from games.rock_paper_scissors import rps_pvb
from menus import main_menu
from layouts import create_pvb_name_menu_layout
"""
This is the PVB name menu file.
"""


def main(game: str):
    """
    This is the main function of the PVB (Player vs. Bot) name menu.
    It shows the PVB Name Menu, where the user must enter their name in order to play the game.
    It loads the pvb-name-menu-layout and window and determines the button events for this menu.

    :param game: (str)  name of the game. Can be 'ttt', 'c4' or 'rps'
    :return:  NO return parameter.
    """
    layout = create_pvb_name_menu_layout(game)                                  # create the layout

    window = sg.Window('Name Menu', layout, size=(1200, 800), resizable=True)   # create the window

    # Main Loop
    while True:
        event, values = window.read()                           # get the button click event
        if event in (sg.WIN_CLOSED, 'Back'):                    # when Back button is pressed, go back to the main menu
            window.close()
            main_menu.main()
            break
        elif event == 'Continue':                                               # when Continue button is pressed
            if values['input_player_name'] == '':                               # check if name is not empty
                sg.popup('Player name can\'t be empty!')
                continue
            elif values['input_player_name'] == 'Bot':                          # check if the name is not 'Bot'
                sg.popup('Player can\'t be names \'Bot\'')
                continue
            elif len(values['input_player_name']) > 10:                         # check that the names are
                sg.popup('Player names can\'t be longer then 10 characters!')   # not too long
                continue
            window.close()
            if game == 'Connect Four':                          # depending on the game that was selected earlier
                connect_four_bot.main([values['input_player_name'], 'Bot'])     # go to that game
            elif game == 'Rock-Paper-Scissors':
                rps_pvb.main([values['input_player_name'], 'Bot'])
            elif game == 'Tic-Tac-Toe':
                tic_tac_toe_vs_bot.main(([values['input_player_name'], 'Bot']))
            break

    window.close()                                                              # close the window
