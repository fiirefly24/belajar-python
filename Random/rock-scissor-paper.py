import random

options = ("rock", "scissor", "paper")
player = None
computer = random.choice(options)
running = True

while running:
    while player not in options:
        player = input("Enter a choice (rock, scissor, paper): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie")
    elif player == "rock" and computer == "scissor":
        print("Player win!")
    elif player == "paper" and computer == "rock":
        print("Player win!")
    elif player == "scissor" and computer == "paper":
        print("Player win!")
    else:
        print("Computer win!")
        

    if input("Do you want to play again? y/n: ").lower() == "y":
        running = True
        player = None
        computer = random.choice(options)
    else:
        running =  False
        print("Thanks for Playing!")