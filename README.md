# Python Group Project - Minigame collection

#### [Link to the git-hub repo](https://github.com/TMHCode/python_group_project) 👈 
___
### How to run
- download the scripts-folder or clone the repo ```https://github.com/TMHCode/python_group_project.git```
- have python installed
- install the PySimpleGUI library
- run the __main__.py file
___
___
## Minigame-Collection
- **Tic-Tac-Toe** _(Viktor)_
- **Rock-Paper-Scissors** _(Trung)_
- **Connect 4** _(Tobias)_
___
### Task
We will create a collection of three minigames in python. Tic-Tac-Toe, Rock-Paper-Scissors
and Connect Four.

There will be a main menu where you are able to choose between these games and a
statistics menu.

After a game and gamemode (Player-vs-Player or Player-vs-Bot) is chosen, the user(s) can
enter their name(s).

The username and their number of wins and total games are stored in a
separate file to be able to show statistics and scoreboards.

In the “statistics menu” the user can check who is the best player in each game similar to a
Scoreboard (Wins/per game played).

>#### Viktor Wascher: “Tic-Tac-Toe”.
>Users will be able to play a classic game of tic-tac-toe, with a 3x3 field.
Player 1 fills the blank spaces with “X” and player 2 or the bot with “O”. First to connect 3 of
his symbols vertically, horizontal or diagonal wins the game.
If none manages to connect 3, it's a draw.

>#### Trung Nguyen: “Rock Paper Scissors”.
>It is a simple hand game played by two people.
The player/s choose one of three hand signs representing rock, paper, or scissors then a
counter starts counting down from three. After the timer reaches 0 both will show which hand
sign they have chosen.
The winner is determined by these rules.
Rock crushes scissors, scissors cut paper, paper covers rock.
If both players throw the same hand sign, the game is a tie.

>#### Tobias Herrmann: ”Connect Four”.
>The game consists of a 7x6 grid where two players can “drop” in their game-pieces. The
players take turns and the piece will always drop to the bottommost empty cell of the grid. A
player wins once he has successfully put four pieces in a row (either horizontal, vertical or
diagonal). Both players draw, when no one achieves four pieces in a row before the grid is
completely filled.

The games will have 2 modes: player versus player and player versus an easy bot.

If the game is finished the user will see his statistics, and can either play again, check the
scoreboard or return to the main menu.

An additional possible feature would be a good looking user interface with clickable cells and
different colors.
___
##### visual library: **PySimpleGUI**

##### Colors:
- Main Color Scheme: ```sg.ChangeLookAndFeel('DarkAmber')```
  - Main color: #FCCB53
  - Secondary color 2: #FC9E47
  - Third color: #FCF060
  - Complementary color 1: #703AFC
  - Complementary color 2: #B8F1FF
  - Background color: #2c2825
  - Font color: #fff7e2
  
