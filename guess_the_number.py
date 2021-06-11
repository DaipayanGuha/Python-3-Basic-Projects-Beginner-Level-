import random

max_value = input("Enter a number : ")

if max_value.isdigit():
    max_value = int(max_value)

    if max_value <= 0:
        print('Please enter an Integer larger than 0 next time.')
        quit()
else:
    print('Please type an Integer next time.')
    quit()

random_num = random.randint(0, max_value)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess an integer : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_num:
        print("BINGO!")
        break
    elif user_guess > random_num:
        print("You guessed higher.")
    else:
        print("You guessed lower.")

print("You guessed it in ", guesses, " guesses.")
