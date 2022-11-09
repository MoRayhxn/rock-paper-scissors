from random import randint
### possible options to play 
moves = ["rock", "paper", "scissors"]
### start a loop so player can keep going till they lose
while True:
### allows computer to choose randomly and player to choose
    computer = moves[randint(0,2)]
    player = input("Choose rock, paper or scissors, or 'end' to finish the game: ").lower()
### allows player to end game if they wish
    if player == "end":
        print("Game over!")
### ends the loop if player does end
        break
### listing all win conditions in one if statement. rest will result in a loss or a tie so no need to make a code for other variations aside from else or lose and == for tie
    if player == 'rock' and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper":
        print("You win!", player, "beats", computer)
    elif player == computer:
        print('Tie')
    else:
        print("You lose!", computer, "beats", player) 