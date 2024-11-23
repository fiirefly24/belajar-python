import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "A"]
# number = random.randint(low, high) #Return random integer in range [a, b], including both end points.
# number = random.random()
# option = random.choice(options) # Choose a random element from a non-empty sequence
# random.shuffle(cards) # Shuffle list x in place, and return None.
# print(cards)

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try again!")
        elif guess > answer:
            print("Too High! Try again!")
        else:
                print(f"Correct~! The answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False
    else:
        print("Invalid Guess")
        print(f"Please Select a number between {lowest_num} and {highest_num}")