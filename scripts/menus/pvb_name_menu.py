import PySimpleGUI as sg

from scripts.games.connect_four import connect_four_bot
#from scripts.games.tic_tac_toe import tic_tac_toe_vs_bot
from scripts.menus import main_menu
from scripts.layouts import create_pvb_name_menu_layout


def main(game):

    # Create the layout
    layout = create_pvb_name_menu_layout(game)

    # Create the window
    window = sg.Window('Menu', layout, size=(1100, 700), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            main_menu.main()
            break
        elif event == 'Continue':
            window.close()
            if game == 'Connect Four':
                connect_four_bot.main()
            elif game == 'Rock Paper Scissors':
                pass
            else:  # game == 'Tic Tac Toe'
                #tic_tac_toe_vs_bot.main()
                pass
            break

    window.close()
