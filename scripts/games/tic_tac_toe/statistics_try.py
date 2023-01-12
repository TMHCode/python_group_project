import PySimpleGUI as sg

# Initialize an empty dictionary to store the win, lose, and draw counts for each player
player_records = {}

# Open the text file and read the lines
with open('scores.txt') as f:
    lines = f.readlines()

# Iterate through each line of the file
for line in lines:
    # Split the line into words
    words = line.split()
    player = words[0]
    outcome = words[1]
    # check if player already exists in the dictionary
    if player in player_records:
        if outcome == 'Win':
            player_records[player]['Wins'] += 1
        elif outcome == 'Lose':
            player_records[player]['Loses'] += 1
        elif outcome == 'Draw':
            player_records[player]['Draws'] += 1
    # if player not exists in the dictionary
    else:
        if outcome == 'Win':
            player_records[player] = {'Wins': 1, 'Loses': 0, 'Draws': 0}
        elif outcome == 'Lose':
            player_records[player] = {'Wins': 0, 'Loses': 1, 'Draws': 0}
        elif outcome == 'Draw':
            player_records[player] = {'Wins': 0, 'Loses': 0, 'Draws': 1}

# Create a list of elements for the PySimpleGui layout
layout_elements = []

# Sort the players by win rate in descending order
sorted_players = sorted(player_records.items(), key=lambda x: x[1]['Wins']/(x[1]['Wins']+x[1]['Loses']), reverse=True)

#Append the headers
layout_elements.append([sg.Text('Player'), sg.Text('Wins'), sg.Text('Draws'), sg.Text('Loses'),sg.Text('Win Rate')])

# Append the top 10 players to the layout
for i in range(min(10, len(sorted_players))):
    player, records = sorted_players[i]
    layout_elements.append([sg.Text(player), sg.Text(records["Wins"]), sg.Text(records["Draws"]), sg.Text(records["Loses"]),sg.Text(f'{records["Wins"]/(records["Wins"]+records["Loses"]):.2%}')])

# Add an 'OK' button to the layout
layout_elements.append([sg.Button('OK')])

# Create a PySimpleGui window and display the results
window = sg.Window('Top 10 players by win rate', layout_elements)
while True:
    event, values = window.read()
    if event in (None, 'OK'):
        break

window.close()
