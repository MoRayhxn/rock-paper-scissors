### Import specification function required - for some reason if I do just "import random"
from random import randint

moves = ["rock", "paper", "scissors"]

### While pretty much is used so we can play over and over.
while True:
    computer = moves[randint(0,2)]
    player = input("Choose rock, paper or scissors, or 'end' to finish the game: ").lower()

### Break the loop if player wants to end
    if player == "end":
        print("The game is over")
        break

### All possible iterations.
    elif player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)

### This is to let the player know they typed in the wrong thing and re do it.
    else:
        print("Check your spelling and try again...")