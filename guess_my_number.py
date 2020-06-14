#Python Random Module
import random

#Number of Attempts
attempts = 0

#Choose a random number
number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10')

#While the player's guess is less than 6
while attempts < 6:
    guess = input('Take a guess: ')
    guess = int(guess)

    attempts += 1

    #if player's guess is too low
    if guess < number:
        print('Higher')

    #if player's guess is too high
    if guess > number:
        print('Lower')

    #if the player won, stop the loop
    if guess == number:
        break

#If the player won
if guess == number:
    attempts = str(attempts)
    print("Good Job! You guessed my number in", attempts, "guesses!")

#If the player lost
if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was", number)