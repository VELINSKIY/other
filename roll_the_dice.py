#Python random
import random

#Function
def again():
    #Variablees
    dices = 0
    roll_again = print()
    while dices == 0:
        #user's choice of how many dices they want to roll
        chosen_dices = int(input("How many dices do you want to roll? (from 1 to 5): "))
        #if thhe user choose a number between 1 and 5, break out of the loop
        if chosen_dices > 0 and chosen_dices < 6:
            break

    #if the user choose (any number) dice(s), generate a random number from 1 to 6 and continue until we meet the user's needs
    if chosen_dices == 1:
        while dices < 1:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 2:
        while dices < 2:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1
    
    elif chosen_dices == 3:
        while dices < 3:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 4:
        while dices < 4:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 5:
        while dices < 5:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    #askin the user if he wants to roll again
    print("Do you want to roll again? ")
    while roll_again != "Yes" or roll_again != "No":
        roll_again = input("Yes | No: ")
        if roll_again == "Yes":
            again()
            break
        if roll_again == "No":
            print("Goodbye!")
            break

again()