from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#ebf0f3")

# picture
rock_img = ImageTk.PhotoImage(Image.open("assets/stone.png"))
paper_img = ImageTk.PhotoImage(Image.open("assets/paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("assets/scissor.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("assets/stone.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("assets/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("assets/scissor.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#ebf0f3")
comp_label = Label(root, image=scissor_img_comp, bg="#ebf0f3")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# score
playerScore = Label(root, text=0, font=100, bg="#ebf0f3", fg="#020003")
computerScore = Label(root, text=0, font=100, bg="#ebf0f3", fg="#020003")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicator
user_indicator = Label(root, font=100, text="USER", bg="#ebf0f3", fg="#020003")
comp_indicator = Label(root, font=100, text="COMPUTER", bg="#ebf0f3", fg="#020003")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#ebf0f3", fg="#020003")
msg.grid(row=1, column=2)


# update msg
def updateMessage(x):
    msg['text'] = x


# update user score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)


# update computer score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)


def checkWin(player, computer):
    if player == "rock":
        if computer == "paper":
            updateMessage("You loose!")
            updateCompScore()
        elif computer == "rock":
            updateMessage("It's a tie!")
        elif computer == "scissor":
            updateMessage("You Win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose!")
            updateCompScore()
        elif computer == "paper":
            updateMessage("It's a tie!")
        elif computer == "rock":
            updateMessage("You Win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose!")
            updateCompScore()
        elif computer == "scissor":
            updateMessage("It's a tie!")
        elif computer == "paper":
            updateMessage("You Win!")
            updateUserScore()
    else:
        pass


# for user
choices = ["rock", "paper", "scissor"]


def updateChoice(x):


    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    elif x == "scissor":
        user_label.configure(image=scissor_img)

    # Choose a random choice for the computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    elif compChoice == "scissor":
        comp_label.configure(image=scissor_img_comp)

    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#212020", fg="#ebf0f3", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#d27b4b", fg="#ebf0f3",
               command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#b18cd9", fg="#020003",
                 command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

root.mainloop()
