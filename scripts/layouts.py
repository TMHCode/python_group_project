import PySimpleGUI as sg

# Set color scheme of the window
sg.ChangeLookAndFeel('DarkAmber')  # Add a touch of color


# --- Create all the different Layouts for the window here ---

# ----- LAYOUT for main_menu.py -----
def create_main_menu_layout():
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text('Main Menu', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                [sg.Push(), sg.Button('Tic-Tac-Toe', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Connect Four', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Rock-Paper-Scissors', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Statistics', size=(16, 2), border_width=10, font=('Helvetica', 18), button_color=('black', '#FC9E47'), pad=(10, 20)), sg.Push()],
                [sg.VPush()],
                [sg.Button('Quit',  size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'), pad=(0, 0))]
    ]
# ----------


# ----- LAYOUT for mode_menu.py -----
def create_mode_menu_layout(game):
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text(f'Mode Menu - {game}', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                [sg.Push(), sg.Text('Chose your game-mode!', size=(17, 2), font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Player vs. Player', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Button('Player vs. Bot', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.VPush()],
                [sg.Button('Back',  size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'), pad=(0, 0))]
    ]
# ----------


# ----- LAYOUT for pvp_name_menu.py -----
def create_pvp_name_menu_layout(game):
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text(f'Name Menu - {game}', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                [sg.Push(), sg.Text('Enter your names!', size=(17, 2), font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Text('Player 1:', size=(17, 2), font=('Helvetica', 20), pad=(10, 10)), sg.InputText('Player 1', key='input_p1_name'), sg.Push()],
                [sg.Push(), sg.Text('Player 2:', size=(17, 2), font=('Helvetica', 20), pad=(10, 10)), sg.InputText('Player 2', key='input_p2_name'), sg.Push()],
                [sg.Push(), sg.Button('Continue', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.VPush()],
                [sg.Button('Back',  size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'), pad=(0, 0))]
    ]
# ----------


# ----- LAYOUT for pvb_name_menu.py -----
def create_pvb_name_menu_layout(game):
    return [
                [sg.VPush()],
                [sg.Push(), sg.Text(f'Name Menu - {game}', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
                [sg.Push(), sg.Text('Enter your name!', size=(17, 2), font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.Push(), sg.Text('Player:', size=(17, 2), font=('Helvetica', 20), pad=(10, 10)), sg.InputText('name player', key='input_player_name'), sg.Push()],
                [sg.Push(), sg.Button('Continue', size=(17, 2), border_width=10, font=('Helvetica', 20), pad=(10, 10)), sg.Push()],
                [sg.VPush()],
                [sg.Button('Back',  size=(7, 2), font=('Helvetica', 16), border_width=10, button_color=('black', '#B8F1FF'), pad=(0, 0))]
    ]
# ----------


# ----- LAYOUT for connect_four.py -----
def create_connect_four_layout(col_count: int, row_count: int, p_names: list):
    game_column = [
        *[[sg.Button(' ', button_color=('white', 'black'), size=(5, 2), pad=(0, 0), key=(r, c)) for c in range(col_count)] for r in range(row_count)],
        [sg.Button('Back', size=(8, 2), button_color=('black', '#B8F1FF'), pad=(50, 15), border_width=8), sg.Button('New Game', size=(14, 2), pad=(50, 15), border_width=10)]
    ]

    stats_column = [
        [sg.Push(background_color='#403731'), sg.Text('Game Info', font=('Helvetica', 20, 'bold'), background_color='#403731'), sg.Push(background_color='#403731')],
        [sg.HSeparator(color='#403731')],
        [sg.Text(f'Current Player: {p_names[0]}', background_color='#403731', text_color='#FFF7E2', key='active_player')],
        [sg.HSeparator(color='#403731')],
        [sg.Text(f'Player 1: {p_names[0]}', background_color='#403731', text_color='#FFF7E2', key='p1_name'), sg.Text('COL', background_color='#6F3AFC', text_color='#6F3AFC')],
        [sg.Text(f'Player 2: {p_names[1]}', background_color='#403731', text_color='#FFF7E2'), sg.Text('COL', background_color='#FCF060', text_color='#FCF060')],
        [sg.HSeparator(color='#403731')],
        [sg.Text('Round: 1', background_color='#403731', text_color='#FFF7E2', key='round_number')]
    ]

    return [
        [sg.VPush()],
        [sg.Push(), sg.Text('Connect Four', size=(30, 1), pad=(10, 20), font=('Helvetica', 50, 'bold'), text_color='#FFF7E2', justification='center'), sg.Push()],
        [sg.Push(), sg.Column(game_column),
            sg.VSeparator(color='#403731'),
            sg.Col(stats_column, background_color='#403731', pad=(30, 0)), sg.Push()],
        [sg.VPush()]
    ]
# ----------


# ----- LAYOUT for tic_tac_toe.py -----
def create_tic_tac_toe_layout():

    return[
        [[sg.Text("Tic-Tac-Toe", font=("Helvetica", 20))],
         [[sg.Button(" ", size=(5, 2), font=("Helvetica", 20), key=(i, j)) for i in range(3)]
          for j in range(3)],
         [sg.Button("Back", size=(8, 2), border_width=8, button_color=('black', '#B8F1FF')),
          sg.Button("New Game", size=(14, 2), border_width=10)]]

    ]
# ----------
