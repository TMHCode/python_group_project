import PySimpleGUI as sg

from scripts.layouts import create_scoreboard_menu_layout
from scripts.menus import main_menu
from scripts.statistics.stats import load_scores
"""
This is the scoreboard menu file.
"""


def main():
    """
    This is the main function of the scoreboard menu.
    It shows the Scoreboard.
    It loads the scoreboard-layout and window and determines the button events for this menu.

    :return: NO return parameter.
    """
    # get player records from file
    player_records = load_scores()
    # Create the layout
    layout = create_scoreboard_menu_layout(player_records)

    # Create the window
    window = sg.Window('Scoreboard', layout, size=(1200, 800), resizable=True)

    # Loop to handle events
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'C4':
            window['high_score_text'].update('High scores! - Connect 4')
            window['TTT_key'].update(visible=False)
            window['RPS_key'].update(visible=False)
            window['C4_key'].update(visible=True)
        elif event == 'RPS':
            window['high_score_text'].update('High scores! - Rock-Paper-Scissors')
            window['TTT_key'].update(visible=False)
            window['C4_key'].update(visible=False)
            window['RPS_key'].update(visible=True)
        elif event == 'TTT':
            window['high_score_text'].update('High scores! - Tic-Tac-Toe')
            window['C4_key'].update(visible=False)
            window['RPS_key'].update(visible=False)
            window['TTT_key'].update(visible=True)

        if event in (sg.WIN_CLOSED, 'Back'):
            window.close()
            main_menu.main()
            break

    window.close()
