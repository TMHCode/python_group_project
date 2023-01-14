import PySimpleGUI as sg
import os
"""
This is the layouts file.
All the Layouts that are needed for the PySimpleGUI functionality are created and stored here.
"""

# Setting the color scheme for all layouts
sg.ChangeLookAndFeel('DarkAmber')


# --- Create all the different Layouts for the windows here ---
########################################
# MENU LAYOUTS
# ----- LAYOUT for main_menu.py -----
def create_main_menu_layout():
    """
    This function creates the layout for the main menu.

    :return: (list) layout-structure
    """
    return [
        [sg.VPush()],
        [sg.Push(),
         sg.Text('Main Menu', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2',
                 justification='center'), sg.Push()],
        [sg.Push(), sg.Button('Tic-Tac-Toe', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.Push(), sg.Button('Connect Four', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.Push(),
         sg.Button('Rock-Paper-Scissors', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.Push(), sg.Button('Statistics', size=(16, 2), border_width=10, font=('Helvetica', 18),
                              button_color=('black', '#FC9E47'), pad=(10, 20)), sg.Push()],
        [sg.VPush()],
        [sg.Button('Quit', size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'),
                   pad=(0, 0))]
    ]


# ----------


# ----- LAYOUT for mode_menu.py -----
def create_mode_menu_layout(game: str):
    """
    This function creates the layout for the game mode menu.

    :param game: (str) name of the game
    :return: (list) layout-structure
    """
    header_font_size = 50 if game != 'Rock-Paper-Scissors' else 45
    return [
        [sg.VPush()],
        [sg.Push(), sg.Text(f'{game}', size=(30, 1), pad=(10, 10), font=('Helvetica', header_font_size, 'bold'),
                            text_color='#FFF7E2', justification='center'), sg.Push()],
        [sg.HSeparator()],
        [sg.Push(), sg.Text('Chose your game-mode!', size=(30, 2), font=('Helvetica', 20), pad=(0, 20),
                            justification='center', text_color='#FC9E47'), sg.Push()],
        [sg.Push(), sg.Button('Player vs. Player', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.Push(), sg.Button('Player vs. Bot', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.VPush()],
        [sg.Button('Back', size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'),
                   pad=(0, 0))]
    ]


# ----------


# ----- LAYOUT for pvp_name_menu.py -----
def create_pvp_name_menu_layout(game: str):
    """
    This function creates the layout for the pvp (player vs. player) name menu.

    :param game: (str) name of the game
    :return: (list) layout-structure
    """
    header_font_size = 50 if game != 'Rock-Paper-Scissors' else 45
    return [
        [sg.VPush()],
        [sg.Push(), sg.Text(f'{game}', size=(30, 1), pad=(10, 10), font=('Helvetica', header_font_size, 'bold'),
                            text_color='#FFF7E2', justification='center'), sg.Push()],
        [sg.HSeparator()],
        [sg.Push(), sg.Text('Enter your names!', size=(30, 2), font=('Helvetica', 20), pad=(0, 20),
                            justification='center', text_color='#FC9E47'), sg.Push()],
        [sg.Push(), sg.Text('Player 1:', size=(10, 1), font=('Helvetica', 20), pad=(0, 10)),
         sg.Input(key='input_p1_name', size=(15, 1), pad=(0, 10)), sg.Push()],
        [sg.Push(), sg.Text('Player 2:', size=(10, 1), font=('Helvetica', 20), pad=(0, 10)),
         sg.Input(key='input_p2_name', size=(15, 1), pad=(0, 10)), sg.Push()],
        [sg.Push(), sg.Button('Continue', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.VPush()],
        [sg.Button('Back', size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'),
                   pad=(0, 0))]
    ]


# ----------


# ----- LAYOUT for pvb_name_menu.py -----
def create_pvb_name_menu_layout(game: str):
    """
    This function creates the layout for the pvb (player vs. bot) name menu.

    :param game: (str) name of the game
    :return: (list) layout-structure
    """
    # Change the font-size depending on the game (text doesn't fit otherwise)
    header_font_size = 50 if game != 'Rock-Paper-Scissors' else 45
    return [
        [sg.VPush()],
        [sg.Push(), sg.Text(f'{game}', size=(30, 1), pad=(10, 10), font=('Helvetica', header_font_size, 'bold'),
                            text_color='#FFF7E2', justification='center'), sg.Push()],
        [sg.HSeparator()],
        [sg.Push(), sg.Text('Enter your name!', size=(30, 2), font=('Helvetica', 20), pad=(0, 20),
                            justification='center', text_color='#FC9E47'), sg.Push()],
        [sg.Push(), sg.Text('Player:', size=(8, 1), font=('Helvetica', 20), pad=(0, 10)),
         sg.Input(key='input_player_name', size=(15, 1), pad=(0, 10)), sg.Push()],
        [sg.Push(), sg.Button('Continue', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Push()],
        [sg.VPush()],
        [sg.Button('Back', size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'),
                   pad=(0, 0))]
    ]


# ----------


# ----- LAYOUT for scoreboard_menu.py -----
def create_scoreboard_menu_layout(player_records: dict):
    """
    This function creates the layout for the scoreboard menu.

    :param player_records: (dict) dictionary of dictionaries that contains all the player scores for every game.
                            dict-structure: {'game': {'name': {'Wins': 0, 'Loses': 1, 'Draws': 2, 'Winrate': 0.0}}}
    :return: (list) layout-structure
    """
    # Creating columns for every game that can be used by the sg.Column() element in the main layout
    # --- TTT-Stats-Table ---
    ttt_column = []
    sorted_players = sorted(player_records['ttt'].items(), key=lambda x: x[1]['Winrate'], reverse=True)
    # Append the headers
    ttt_column.append([sg.HSeparator()])
    # Append the top 10 players to the layout
    for i in range(min(10, len(sorted_players))):
        player, records = sorted_players[i]
        ttt_column.append(
            [sg.Push(), sg.Text(player, size=(10, 0), justification='center'),
             sg.Text(records["Wins"], size=(10, 0), justification='center'),
             sg.Text(records["Draws"], size=(10, 0), justification='center'),
             sg.Text(records["Loses"], size=(10, 0), justification='center'),
             sg.Text(f'{records["Winrate"]} %', size=(10, 0), justification='center'), sg.Push()])

    # --- C4-Stats-Table ---
    c4_column = []
    sorted_players = sorted(player_records['c4'].items(), key=lambda x: x[1]['Winrate'], reverse=True)
    # Append the headers
    c4_column.append([sg.HSeparator()])
    # Append the top 10 players to the layout
    for i in range(min(10, len(sorted_players))):
        player, records = sorted_players[i]
        c4_column.append(
            [sg.Push(), sg.Text(player, size=(10, 0), justification='center'),
             sg.Text(records["Wins"], size=(10, 0), justification='center'),
             sg.Text(records["Draws"], size=(10, 0), justification='center'),
             sg.Text(records["Loses"], size=(10, 0), justification='center'),
             sg.Text(f'{records["Winrate"]} %', size=(10, 0), justification='center'), sg.Push()])

    # --- RPS-Stats-Table ---
    rps_column = []
    sorted_players = sorted(player_records['rps'].items(), key=lambda x: x[1]['Winrate'], reverse=True)
    # Append the headers
    rps_column.append([sg.HSeparator()])
    # Append the top 10 players to the layout
    for i in range(min(10, len(sorted_players))):
        player, records = sorted_players[i]
        rps_column.append(
            [sg.Push(), sg.Text(player, size=(10, 0), justification='center'),
             sg.Text(records["Wins"], size=(10, 0), justification='center'),
             sg.Text(records["Draws"], size=(10, 0), justification='center'),
             sg.Text(records["Loses"], size=(10, 0), justification='center'),
             sg.Text(f'{records["Winrate"]} %', size=(10, 0), justification='center'), sg.Push()])

    return [
        [sg.VPush()],
        [sg.Push(),
         sg.Text('Scoreboard', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2',
                 justification='center'), sg.Push()],
        [sg.HSeparator()],
        [sg.Push(), sg.Text('High scores! - Tic-Tac-Toe', key='high_score_text', size=(30, 2),
                            font=('Helvetica', 20), justification='center', text_color="#FC9E47"), sg.Push()],
        [sg.Push(), sg.Text('Player', size=(10, 0), justification='center', text_color='#FFF7E2'),
         sg.Text('Wins', size=(10, 1), justification='center', text_color='#FFF7E2'),
         sg.Text('Draws', size=(10, 1), justification='center', text_color='#FFF7E2'),
         sg.Text('Loses', size=(10, 1), justification='center', text_color='#FFF7E2'),
         sg.Text('Win Rate', size=(10, 1), justification='center', text_color='#FFF7E2'), sg.Push()],
        [sg.Column(ttt_column, key='TTT_key', justification='center'),
         (sg.Column(c4_column, visible=False, key='C4_key', justification='center')),
         (sg.Column(rps_column, visible=False, key='RPS_key', justification='center'))],
        [sg.Button('Back', size=(5, 2), font=('Helvetica', 16), border_width=10,
                   button_color=('black', '#B8F1FF'), pad=(0, 0)),
         sg.Push(), sg.Button('TTT', size=(7, 2), font=('Helvetica', 16), border_width=10,
                              button_color=('black', "#FCCB53"), pad=(0, 20)),
         sg.Button('C4', size=(7, 2), font=('Helvetica', 16), border_width=10,
                   button_color=('black', "#FCCB53"), pad=(0, 20)),
         sg.Button('RPS', size=(7, 2), font=('Helvetica', 16), border_width=10,
                   button_color=('black', "#FCCB53"), pad=(0, 20)), sg.Push()],
        [sg.VPush()]

    ]


# ----------
########################################


########################################
# GAME LAYOUTS
# ----- LAYOUT for connect_four -----
def create_connect_four_layout(col_count: int, row_count: int, p_names: list):
    """
    This function creates the layout for the connect four game.

    :param col_count: (int) number of columns
    :param row_count: (int) number of row
    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :return: (list) layout-structure
    """
    game_column = [
        *[[sg.Button(' ', button_color=('white', 'black'), size=(5, 2), pad=(0, 0), key=(r, c)) for c in
           range(col_count)] for r in range(row_count)],
        [sg.Button('Back', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(50, 15), border_width=8),
         sg.Button('New Game', size=(14, 2), pad=(50, 15), border_width=10)]
    ]

    stats_column = [
        [sg.Push(background_color='#403731'),
         sg.Text('Game Info', font=('Helvetica', 20, 'bold'), background_color='#403731'),
         sg.Push(background_color='#403731')],
        [sg.HSeparator(color='#403731')],
        [sg.Text(f'Current Player: {p_names[0]}', background_color='#6F3AFC', text_color='#FFF7E2',
                 key='active_player')],
        [sg.HSeparator(color='#403731')],
        [sg.Text(f'Player 1: {p_names[0]}', background_color='#403731', text_color='#FFF7E2', key='p1_name'),
         sg.Text('COL', background_color='#6F3AFC', text_color='#6F3AFC')],
        [sg.Text(f'Player 2: {p_names[1]}', background_color='#403731', text_color='#FFF7E2'),
         sg.Text('COL', background_color='#FCF060', text_color='#FCF060')],
        [sg.HSeparator(color='#403731')],
        [sg.Text('Round: 1', background_color='#403731', text_color='#FFF7E2', key='round_number')]
    ]

    return [
        [sg.VPush()],
        [sg.Push(),
         sg.Text('Connect Four', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2',
                 justification='center'), sg.Push()],
        [sg.Push(), sg.Column(game_column),
         sg.VSeparator(color='#403731'),
         sg.Col(stats_column, background_color='#403731', pad=(30, 0)), sg.Push()],
        [sg.VPush()]
    ]


# ----------


# ----- LAYOUT for tic_tac_toe -----
def create_tic_tac_toe_layout(p_names: list):
    """
    This function creates the layout for the tic tac toe game.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :return: (list) layout-structure
    """
    grid_layout = [[sg.Button(" ", size=(5, 2), pad=(0, 0), font=("Helvetica", 20),
                              key=(i, j)) for i in range(3)] for j in range(3)]

    game_column = [
        [sg.Push(), sg.Column(grid_layout), sg.Push()],
        [sg.Button('Back', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(50, 15), border_width=8),
         sg.Button('New Game', size=(14, 2), pad=(50, 15), border_width=10)]
    ]

    stats_column = [
        [sg.Push(background_color='#403731'),
         sg.Text('Game Info', font=('Helvetica', 20, 'bold'), background_color='#403731'),
         sg.Push(background_color='#403731')],
        [sg.HSeparator(color='#403731')],
        [sg.Text(f'Current Player: {p_names[0]}', background_color="#B8F1FF", text_color='black',
                 key='active_player')],
        [sg.HSeparator(color='#403731')],
        [sg.Text(f'Player 1: {p_names[0]} ', background_color='#403731', text_color='#FFF7E2', key='p1_name'),
         sg.Text(' X ', size=(2, 0), background_color="#B8F1FF", text_color="black")],
        [sg.Text(f'Player 2: {p_names[1]}', background_color='#403731', text_color='#FFF7E2'),
         sg.Text(' O ', size=(2, 0), background_color="#FC9E47", text_color="black")],

    ]

    return [
        [sg.VPush()],
        [sg.Push(),
         sg.Text('Tic-Tac-Toe', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2',
                 justification='center'), sg.Push()],
        [sg.Push(), sg.Column(game_column),
         sg.VSeparator(color='#403731'),
         sg.Col(stats_column, background_color='#403731', pad=(30, 0)), sg.Push()],
        [sg.VPush()]
    ]


# ----------


# ----- LAYOUT for rock paper scissors -----
def create_rps_layout(p_names: list):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    rock_img = os.path.join(current_directory, 'assets', 'stone.png')
    paper_img = os.path.join(current_directory, 'assets', 'paper.png')
    scissors_img = os.path.join(current_directory, 'assets', 'scissor.png')

    return [
        [sg.VPush()],
        [sg.Push()],
        [sg.Text("Rock-Paper-Scissor", size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2',
                 justification='center')],
        [sg.Text(f"Make your choice {p_names[0]}", font=("Helvetica", 24), pad=(5, 10))],
        [sg.Button('', image_filename=rock_img, button_color="white", key="Rock", image_subsample=2,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(10, 20)),
         sg.Button('', image_filename=paper_img, button_color='#ea8953', key="Paper", image_subsample=2,
                   size=(7, 2), font=('Helvetica', 16), border_width=10,
                   pad=(10, 20)),
         sg.Button('', image_filename=scissors_img, button_color='#c7aee4', key="Scissors",
                   image_subsample=2, size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(10, 20))],
        [sg.Text('', key='-OUTCOME-')],
        [sg.Text('', key='-SCORE-', font=("Helvetica", 26))],
        [sg.Button('Back', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(30, 15), border_width=8),
         sg.Button('New', size=(14, 2), pad=(30, 15), border_width=10)],
        [sg.VPush()],
        [sg.Push()]
    ]


def create_RPS_pvp_layout(p_names: list):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    rock_img = os.path.join(current_directory, 'assets', 'stone.png')
    paper_img = os.path.join(current_directory, 'assets', 'paper.png')
    scissors_img = os.path.join(current_directory, 'assets', 'scissor.png')

    return [
        [sg.VPush()],
        [sg.Push()],
        [sg.Text("Rock-Paper-Scissor", size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2',
                 justification='center')],
        [sg.Text(f"Make your choice", font=("Helvetica", 26)),
         sg.Text(f"{p_names[0]}:", background_color='#6F3AFC', font=("Helvetica", 26))],
        [sg.Button('', image_filename=rock_img, button_color="white", key="p1-rock", image_subsample=4,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(50, 30)),
         sg.Button('', image_filename=paper_img, button_color='#ea8953', key="p1-paper", image_subsample=4,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(50, 30)),
         sg.Button('', image_filename=scissors_img, button_color='#c7aee4', key="p1-scissors", image_subsample=4,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(50, 30))],
        [sg.Text(f"Make your choice", font=("Helvetica", 26)),
            sg.Text(f"{p_names[0]}:", background_color='#B8F1FF', text_color='black', font=("Helvetica", 26))],
        [sg.Button('', image_filename=rock_img, button_color="white", key="p2-rock", image_subsample=4,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(50, 30)),
         sg.Button('', image_filename=paper_img, button_color='#ea8953', key="p2-paper", image_subsample=4,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(50, 30)),
         sg.Button('', image_filename=scissors_img, button_color='#c7aee4', key="p2-scissors", image_subsample=4,
                   size=(7, 2), font=('Helvetica', 16), border_width=10, pad=(50, 30))],
        [sg.Button('Show', size=(8, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)),
         sg.Button('Back', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(50, 15), border_width=8)],
        [sg.VPush()],
        [sg.Push()]
    ]
