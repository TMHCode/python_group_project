import PySimpleGUI as sg

from scripts.games.connect_four import connect_four_bot
from scripts.games.tic_tac_toe import tic_tac_toe_vs_bot
from scripts.games.rock_paper_scissors import PVBnew
from scripts.menus import main_menu
from scripts.layouts import create_pvb_name_menu_layout


def main(game):
    # Create the layout
    layout = create_pvb_name_menu_layout(game)

    # Create the window
    window = sg.Window('Name Menu', layout, size=(1100, 700), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            main_menu.main()
            break
        elif event == 'Continue':
            if values['input_player_name'] == '':
                sg.popup('Player name can\'t be empty!')
                continue
            window.close()
            if game == 'Connect Four':
                connect_four_bot.main([values['input_player_name'], 'Bot'])
            elif game == 'Rock-Paper-Scissors':
                PVBnew.main([values['input_player_name'], 'Bot'])
            elif game == 'Tic-Tac-Toe':
                tic_tac_toe_vs_bot.main(([values['input_player_name'], 'Bot']))
            break

    window.close()
