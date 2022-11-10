import random

# tuples = lists that cant be changed - no function to add upon it - is good in a case such as rps
moves = ("rock", "paper", "scissors")
while True:
    computer = random.choice(moves)
    player = input(
        "Choose rock, paper or scissors... Or 'end' to end the game: ")
        
    if player not in moves:
        print("Invalid Option!")
    elif player == "end":
        print("Game over!")
        exit()
### could also do break instead of exit - exit, stops entire code break just takes you back to the start
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("You win", player, "beats", computer)
    elif player == computer:
        print("Tie!")
    else: 
        print("You lose!", computer, "beats", player)

### this will never print due to the exit() in line 12
print("Testing")

