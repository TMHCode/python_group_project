import PySimpleGUI as sg

# Constants for the game board
ROWS = 6
COLS = 7

# Create the game board as a 2D list
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]


# Function to draw the game board
def draw_board():
    # Create a graphical representation of the game board
    board_layout = [[sg.Button(board[r][c], size=(5, 2), pad=(0, 0), key=(r, c)) for c in range(COLS)] for r in range(ROWS)]
    return sg.Column(board_layout, key='_BOARD_')


# Function to check for a win
def check_win(piece):
    # Check for horizontal wins
    for row in range(ROWS):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    # Check for vertical wins
    for row in range(ROWS-3):
        for col in range(COLS):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    # Check for diagonal wins
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col+3] == piece and board[row+1][col+2] == piece and board[row+2][col+1] == piece and board[row+3][col] == piece:
                return True
    return False


# Function to check if the board is full
def check_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == ' ':
                return False
    return True

# Create the layout for the game
layout = [
    [sg.Text('Connect Four', size=(30, 1), font=('Helvetica', 20))],
    [draw_board()],
    [sg.Button('Quit', size=(10, 2))]
]

# Create the window and show the game
window = sg.Window('Connect Four', layout, size=(750, 750))

# Initialize the player to be "X"
player = "X"

while True:
    # Get the next event in the game
    event, values = window.read()

    # If the event is "Quit" then close the window and exit the game
    if event == 'Quit' or event is None:
        window.close()
        break

    # If the event is a button click, then place a piece on the board
    if event[0] is not None and event[1] is not None:
        r, c = event
        for row in range(ROWS-1, -1, -1):
            if board[row][c] == ' ':
                board[row][c] = player
                print(board)
                break

        # Update the bottommost button in the column to show that it has been clicked
        for row in range(ROWS-1, -1, -1):
            #print(board[row][c], row, c)
            print(window.find_element((row, c)).GetText())
            if board[row][c] == ' ':
                window.find_element((row+1, c)).Update(board[row+1][c])
                break

        # Check if the player has won the game
        if check_win(player):
            sg.popup(f"Player {player} has won!")
            window.close()
            break

        # Check if the board is full
        if check_full():
            sg.popup("The game is a draw!")
            window.close()
            break

        # Switch to the other player
        if player == "X":
            player = "O"
        else:
            player = "X"

    # Redraw the board
    window.Element('_BOARD_').update(draw_board())