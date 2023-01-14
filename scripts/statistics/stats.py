"""
This is the stats file.
It contains the functions for saving and loading the player statistics.
"""


def save_score(p_names: list, result: str, index: int, game_name: str):
    """
    This function saves game results in a 'scores.txt' file by appending the new result to the file.

    :param p_names: (list) list of players. list-structure: ['name player 1', 'name player 2']
    :param result: (str) game result for this player. can be 'Win', 'Lose', or 'Draw'
    :param index: (int) player index in p_names
    :param game_name: (str) name of the played game. can be 'ttt', 'c4' or 'rps'
    :return: NO return value
    """
    # Get the desired player name from the list
    p_name = p_names[index]

    # Open the file in append mode
    with open("statistics/scores.txt", "a") as file:
        file.write(p_name + " " + result + " " + game_name + "\n")


def load_scores():
    """
    This function reads the scores from the 'scores.txt' file and fills a python dictionary with its data.
    It calls another function as its return parameter.

    :return: (function) calls the calculate_winrate function and returns the return parameter
                        of the calculate_winrate function afterwards.
    """
    # Initialize an empty dictionary to store the win, lose, and draw counts for each player in each game
    player_records = {'ttt': {}, 'c4': {}, 'rps': {}}
    # Open the text file and read the lines
    with open('statistics/scores.txt') as f:
        lines = f.readlines()
    # Iterate through each line of the file
    for line in lines:
        # Split the line into words
        player, outcome, game = line.split()
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


def calculate_winrate(player_records: dict):
    """
    This function calculates the winrate for every player in the player_records dictionary and adds it to the dict.

    :param player_records: (dict) dictionary of dictionaries that contains all the player scores for every game.
                            dict-structure: {'game': {'name': {'Wins': 0, 'Loses': 1, 'Draws': 2}}}
    :return: (dict) dictionary of dictionaries that contains all the player scores for every game including win rate.
                            dict-structure: {'game': {'name': {'Wins': 0, 'Loses': 1, 'Draws': 2, 'Winrate': 0.0}}}
    """
    for game in player_records:
        for player in player_records[game]:
            winrate = int(round(player_records[game][player]['Wins'] /
                                (player_records[game][player]['Wins'] +
                                 player_records[game][player]['Loses'] +
                                 player_records[game][player]['Draws']), 2) * 100)

            player_records[game][player]['Winrate'] = winrate
    return player_records
