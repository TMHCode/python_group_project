import tkinter as tk
import random

# create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")
button = Button(window)

# create a function to determine the winner
def play(player, computer, result_text=None, ranking_list=None, ranking_list_text=None):
    if player == computer:
        result_text.set("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            result_text.set("Computer wins!")
        else:
            result_text.set("You win!")
            global win_streak
            win_streak += 1
            ranking_list.insert(0, win_streak)
            ranking_list.sort(reverse=True)
            ranking_list_text.set(ranking_list)
    elif player == "paper":
        if computer == "scissors":
            result_text.set("Computer wins!")
        else:
            result_text.set("You win!")
            win_streak += 1
            ranking_list.insert(0, win_streak)
            ranking_list.sort(reverse=True)
            ranking_list_text.set(ranking_list)
    elif player == "scissors":
        if computer == "rock":
            result_text.set("Computer wins!")
        else:
            result_text.set("You win!")
            win_streak += 1
            ranking_list.insert(0, win_streak)
            ranking_list.sort(reverse=True)
            ranking_list_text.set(ranking_list)


# create a function to handle the rock button click
def rock():
    global win_streak
    win_streak = 0
    computer = random.choice(["rock", "paper", "scissors"])
    play("rock", computer)
    animate()


# create a function to handle the paper button click
def paper():
    global win_streak
    win_streak = 0
    computer = random.choice(["rock", "paper", "scissors"])
    play("paper", computer)
    animate()


# create a function to handle the scissors button click
def scissors():
    global win_streak
    win_streak = 0
    computer = random.choice(["rock", "paper", "scissors"])
    play("scissors", computer)
    animate()


# create a function to animate the buttons
def animate():
    # disable the buttons
    rock_button.configure(state="disabled")
    paper_button.configure(state="disabled")
    scissors_button.configure(state="disabled")

    # animate the buttons
    for i in range(10):
        window.update()
        rock_button.pack_forget()
        paper_button.pack_forget()
        scissors_button.pack_forget()
        window.update()
        rock_button.pack()
        paper_button.pack()
        scissors_button.pack()

    # enable the buttons
    rock_button.configure(state="normal")
    paper_button.configure(state="normal")
    scissors_button.configure
