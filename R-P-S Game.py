from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os

def load_image(image_path):
    try:
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

# Initialize the main window
root = Tk()
root.title("Rock Paper Scissors")
#root.geometry("1000x5000")
root.configure(background="#9b59b6")

# Define image paths
image_paths = {
    "rock_user": "rock-user.png",
    "paper_user": "paper-user.png",
    "scissors_user": "scissors-user.png",
    "rock_comp": "rock_com.png",
    "paper_comp": "paper_com.png",
    "scissors_comp": "scissors_com.png"
}


images = {name: load_image(path) for name, path in image_paths.items()}


for name, img in images.items():
    if img is None:
        print(f"Image for '{name}' could not be loaded.")


user_label = Label(root, image=images["scissors_user"], bg="#9b59b6")
comp_label = Label(root, image=images["scissors_comp"], bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)

user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root, font=50, bg="#9b59b6", fg="white", text="You lose")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

def updateCompScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

def checkwin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserscore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserscore()
    elif player == "scissors":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserscore()

choices = ["rock", "paper", "scissors"]

def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=images["rock_comp"])
    elif compChoice == "paper":
        comp_label.configure(image=images["paper_comp"])
    else:
        comp_label.configure(image=images["scissors_comp"])
    
    if x == "rock":
        user_label.configure(image=images["rock_user"])
    elif x == "paper":
        user_label.configure(image=images["paper_user"])
    else:
        user_label.configure(image=images["scissors_user"])
    
    checkwin(x, compChoice)

rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: updateChoice("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor"))

rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

root.mainloop()
