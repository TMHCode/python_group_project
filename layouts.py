import PySimpleGUI as sg

# Set color scheme of the window
sg.ChangeLookAndFeel('DarkAmber')  # Add a touch of color


# --- Create all the different Layouts for the window here ---

# ----- LAYOUT for menu.py -----
def create_menu_layout():
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


# ----- LAYOUT for connect_four.py -----
def create_connect_four_layout(col_count, row_count):
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
        [sg.Text('Current Player: <P1 name>', background_color='#403731', text_color='#FFF7E2')],
        [sg.HSeparator(color='#403731')],
        [sg.Text('Player 1: <name>', background_color='#403731', text_color='#FFF7E2'),
         sg.Text('COL', background_color='#6F3AFC', text_color='#6F3AFC')],
        [sg.Text('Player 2: <name>', background_color='#403731', text_color='#FFF7E2'),
         sg.Text('COL', background_color='#FCF060', text_color='#FCF060')],
        [sg.HSeparator(color='#403731')],
        [sg.Text('Rounds played: <number>', background_color='#403731', text_color='#FFF7E2')]
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

def create_RPS_layout():
    # Create the main window
    window = sg.Window("Rock-Paper-Scissors", layout=[
        [sg.Text("Make your choice:", font=("Helvetica", 16), text_color="yellow")],
        [sg.Button("Rock [r]", button_color=("white", "black"), key="rock"),
         sg.Button("Paper [p]", button_color=("white", "black"), key="paper"),
         sg.Button("Scissors [s]", button_color=("white", "black"), key="scissors")],
        [sg.Text("Player's choice:", font=("Helvetica", 14), text_color="yellow"),
         sg.Text("", size=(20, 1), key="player_choice", font=("Helvetica", 14), text_color="red")],
        [sg.Text("Computer's choice:", font=("Helvetica", 14), text_color="yellow"),
         sg.Text("", size=(20, 1), key="computer_choice", font=("Helvetica", 14), text_color="red")],
        [sg.Text("Result:", size=(15, 1), font=("Helvetica", 14), text_color="yellow"),
         sg.Text("", size=(20, 1), key="result", font=("Helvetica", 14), text_color="red")],
        [sg.Text("Scores:", size=(15, 1), font=("Helvetica", 14), text_color="yellow"),
         sg.Text("", size=(20, 1), key="scores", font=("Helvetica", 14), text_color="red")],

        [sg.Button('Quit', key='quit')]
    ])
