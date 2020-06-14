import random

print("Welcome to Hangman! I will choose a word and you have to guess its letters. You only have 6 attempts.")
#function
def try_again():
    #random chooser
    words = ["ignore"]
    word_choise = random.choice(words)

    #variables
    attempts = 0
    a = False
    b = False
    c = False
    d = False
    e = False
    f = False
    g = False
    h = False
    i = False
    j = False
    k = False
    l = False
    m = False
    n = False
    o = False
    p = False
    q = False
    r = False
    s = False
    t = False
    u = False
    v = False
    w = False
    x = False
    y = False
    z = False

    #if program chose a word, print it out with missing letters.
    # If the user gets the letters correct, change its variable to True and print it out. 
    # Once all the letters are found, the player won
    if word_choise == "ignore":
        print(" ____ n o __ e")
        guess = input("type the missing letters: ")
        while attempts < 6:
            if guess == "i":
                i = True
                if g == True and r == True:
                    print(" i g n o r e")
                    win = input("You won, you took {attempts} attempts. Do you want to play again? Yes or No: ")
                    if win == "Yes":
                        try_again()
                        break
                    elif win == "No":
                        print("Goodbye")
                        break
                elif r == True:
                    print("i __ n o r e")
                    guess = input("Type the missing letter: ")
                elif g == True:
                    print("i g n o __ e")
                    guess = input("Type the missing letter: ")
                else:
                    print("i __ n o __ e")
                    guess = input("Type the missing letter: ")
            elif guess == "g":
                g = True
                if i == True and r == True:
                    print("i g n o r e")
                    win = input("You won, you took {attempts} attempts. Do you want to play again? Yes or No: ")
                    if win == "Yes":
                        try_again()
                        break
                    elif win == "No":
                        print("Goodbye")
                        break
                elif r == True:
                    print("__ g n o r e")
                    guess = input("Type the missing letter: ")
                elif i == True:
                    print("i g n o __ e")
                    guess = input("Type the missing letter: ")
                else:
                    print("__ g n o __ e")
                    guess = input("Type the missing letter: ")
            elif guess == "r":
                r = True
                if i == True and g == True:
                    print("i g n o r e")
                    win = input("You won, you took {attempts} attempts. Do you want to play again? Yes or No: ")
                    if win == "Yes":
                        try_again()
                        break
                    elif win == "No":
                        print("Goodbye")
                        break
                elif g == True:
                    print("__ g n o r e")
                    guess = input("type the missing letter: ")
                elif i == True:
                    print("i __ n o r e")
                    guess = input("type the missing letter: ")
                else:
                    print(" ____ n o r e")
                    guess = input("type the missing letter: ")
            else:
                print("Try Again")
                attempts += 1
                guess = input("type the missing letter: ")
            
            #if all player's attemts lost, game over
            if not attempts < 6:
                game_over = input("Game Over. Do you want to play again? Yes or No: ")
                if game_over == "Yes":
                    try_again()
                elif game_over == "No":
                    print("Goodbye")

try_again()