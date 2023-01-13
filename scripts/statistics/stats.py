

def save_score(p_names, result, index, game_name):
    # Get the desired player name from the list
    p_name = p_names[index]

    # Open the file in append mode
    with open("statistics/scores.txt", "a") as file:
        file.write(p_name + " " + result + " " + game_name + "\n")


def load_scores():
    # Initialize an empty dictionary to store the win, lose, and draw counts for each player
    player_records = {'ttt': {}, 'c4': {}, 'rps': {}}
    # Open the text file and read the lines
    with open('statistics/scores.txt') as f:
        lines = f.readlines()
    # Iterate through each line of the file
    for line in lines:
        # Split the line into words
        words = line.split()

        player = words[0]
        outcome = words[1]
        game = words[2]
        # check if player already exists in the dictionary
        if player in player_records[game]:
            if outcome == 'Win':
                player_records[game][player]['Wins'] += 1
            elif outcome == 'Lose':
                player_records[game][player]['Loses'] += 1
            elif outcome == 'Draw':
                player_records[game][player]['Draws'] += 1
        # if player not exists in the dictionary
        else:
            if outcome == 'Win':
                player_records[game][player] = {'Wins': 1, 'Loses': 0, 'Draws': 0}
            elif outcome == 'Lose':
                player_records[game][player] = {'Wins': 0, 'Loses': 1, 'Draws': 0}
            elif outcome == 'Draw':
                player_records[game][player] = {'Wins': 0, 'Loses': 0, 'Draws': 1}
    return calculate_winrate(player_records)


def calculate_winrate(player_records):
    for game in player_records:
        for player in player_records[game]:
            winrate = round(player_records[game][player]['Wins'] / (player_records[game][player]['Wins'] + player_records[game][player]['Loses'] + player_records[game][player]['Draws']), 2)
            player_records[game][player]['Winrate'] = winrate
    return player_records

