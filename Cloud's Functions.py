def start_game(): #Starts the game
    yes_no = input("Do you want play? (y/n): ")
    while (yes_no.lower() != "y" and yes_no.lower() != "n"):
        yes_no = input("\nWhat you typed was not y or n. Please try again: ")
    if yes_no.lower() == "n":
        print ("\nThat's okay. Maybe you'll play next time. Bye!")
    else:
        print ("\nGreat! Let's get started then.")
    return yes_no


def game_info():  #The initial 5 questions about the game collected all in one function with verification
    print ("Now we'll fill in the data for you.")
    name = input("\nWhat is your name? ")

#This determines your civilization level for the game
    civ_lvl = input("\nHow civilized are you? (0 - 3): ")
    while (civ_lvl.isdigit() == False or int(civ_lvl) < 0 or int(civ_lvl) > 3):
        if civ_lvl.isdigit() == False:
            civ_lvl = input("That is not a positive integer. Please try again: ")
        else:
            civ_lvl = input("That value is not within the valid range. Please try again: ")

#This determines your initial fuel amount
    fuel_amount = input("\nHow much fuel do you start with? (10 - 50): ")
    while (fuel_amount.isdigit() == False or int(fuel_amount) < 10 or int(fuel_amount) > 50):
        if fuel_amount.isdigit() == False:
            fuel_amount = input("That is not a positive integer. Please try again: ")
        else:
            fuel_amount = input("That value is not within the valid range. Please try again: ")

#This determines the maximum turns this game can have
    max_turns = input("\nWhat is the maximum amount of turns this game? (1 - 10): ")
    while (max_turns.isdigit() == False or int(max_turns) < 0 or int(max_turns) > 10):
        if max_turns.isdigit() == False:
            max_turns = input("That is not a positive integer. Please try again: ")
        else:
            max_turns = input("That value is not within the valid range. Please try again: ")

#This determines if amazing explosions happen or not. If they do happen, the mild explosions automatically happen as well.
    amaz_expl = input("\nDo you want amazing explosions to happen? (y/n): ")
    while (amaz_expl.lower() != "y" and amaz_expl.lower() != "n"):
        amaz_expl = input("What you typed was not y or n. Please try again: ")

#This determines whether or not mild explosions happen or not if amazing explosionsdont happen
    if amaz_expl.lower() == "n":
        mild_expl = input("\nSince you don't want amazing explosions to happen, do you want mild explosions to happen? (y/n): ")
        while (mild_expl.lower() != "y" and mild_expl.lower() != "n"):
            mild_expl = input("What you typed was not y or n. Please try again: ")
    else:
        mild_expl = "y"

    return name, civ_lvl, fuel_amount, max_turns, amaz_expl, mild_expl




#-------------------------------------------------------------------------------------------------------------------------------------------------------#
