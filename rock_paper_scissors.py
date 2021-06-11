'''
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
'''

import random

user_score = 0
comp_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score += 1

    else:
        print("You lost!")
        comp_score += 1

print("You won ", user_score, " times.")
print("The Computer won ", comp_score, " times.")
print("See You Again!")
