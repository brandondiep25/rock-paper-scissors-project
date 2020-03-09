import random

comp_wins = 0
player_wins = 0


# Defining Options
def Choose_Option():
    user_choice = input ("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print ("I didn't understand, please try again!")
        Choose_Option()
    return user_choice


# CPU Options
def Computer_Option():
    comp_choice = random.randint (1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else: comp_choice = "s"
    return comp_choice


#Defining Moves
while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock & the CPU chose rock. You tied!")
        elif comp_choice == "p":
            print("You chose rock & the CPU chose paper. You lost!")
            comp_wins += 1
        elif comp_choice == "s":
            print("You chose rock & the CPU chose scissors. You win!")
            player_wins += 1

    if user_choice == "p":
        if comp_choice == "p":
            print("You chose paper & the CPU chose paper. You tied!")
        elif comp_choice == "s":
            print("You chose paper & the CPU chose scissors . You lost!")
            comp_wins += 1
        elif comp_choice == "r":
            print("You chose paper & the CPU chose rock. You win!")
            player_wins += 1

    if user_choice == "s":
        if comp_choice == "s":
            print("You chose scissors & the CPU chose scissors. You tied!")
        elif comp_choice == "r":
            print("You chose scissors & the CPU chose rock. You lost!")
            comp_wins += 1
        elif comp_choice == "p":
            print("You chose scissors & the CPU chose paper. You win!")
            player_wins += 1


# Notating Winner
        print("")
        print("Player wins: " + str(player_wins))
        print("Computer wins: " + str(comp_wins))
        print("")


#Play Again?    
    user_choice = input("Would you like to play again? (Y/N)")

    if user_choice in ["Y", "y", "yes", "Yes"]:
            pass
    
    elif user_choice in ["N", "n", "no", "No"]:
            break
    else:
        print ("I didn't understand, please try again!")
        input("Would you like to play again? (Y/N)")



