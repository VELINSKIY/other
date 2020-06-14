#Python Random Module
import random

#Intro
print("Rock, Paper, Scissors...")

#Function
def try_again():
    #Random choise
    R_P_S = ["Rock", "Paper", "Scissors"]
    computer = random.choice(R_P_S)

    #Players choise
    player = input("Your choise: ")

    #If the pprogram chose rock
    if computer == "Rock":
        #if player chose rock
        if player == "Rock":
            print("I chose", computer, ", you chose", player, "- It is a tie!")
        #if player chose paper
        elif player == "Paper":
            print("I chose", computer, ", you chose", player, "- You win!")
        #if player chose scissors
        elif player == "Scissors":
            print("I chose", computer, ", you chose", player, "- I win!")

    #If the program chose paper
    elif computer == "Paper":
        #if player chose rock
        if player == "Rock":
            print("I chose", computer, ", you chose", player, "- I win!")
        #if player chose paper
        elif player == "Paper":
            print("I chose", computer, ", you chose", player, "- It is a tie!")
        #if player chose scissors
        elif player == "Schissors":
            print("I chose", computer, ", you chose", player, "- You win!")
    
    #If the program chose paper
    elif computer == "Schissors":
        #if player chose rock
        if player == "Rock":
            print("I chose", computer, ", you chose", player, "- You win!")
        #if player chose paper
        elif player == "Paper":
            print("I chose", computer, ", you chose", player, "- I win!")
        #if player chose scissors
        elif player == "Schissors":
            print("I chose", computer, ", you chose", player, "- It is a tie!")

    #If the player wants to play again
    play_again = input("Do you want to play again? Yes or No: ")
    #if the player says yes, go back to the function
    if play_again == "Yes":
        try_again()
    #if the player says no, say goodbye
    elif play_again == "No":
        print("Goodbye!")

#End of function
try_again()