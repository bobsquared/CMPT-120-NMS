import random as r

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

#This determines whether or not mild explosions happen or not if amazing explosions dont happen
    if amaz_expl.lower() == "n":
        mild_expl = input("\nSince you don't want amazing explosions to happen, do you want mild explosions to happen? (y/n): ")
        while (mild_expl.lower() != "y" and mild_expl.lower() != "n"):
            mild_expl = input("What you typed was not y or n. Please try again: ")
    else:
        mild_expl = "y"

    position = 0

    return name, civ_lvl, fuel_amount, max_turns, amaz_expl, mild_expl, position



def movement(planet_list, position):
    selection = input("Would you like to roll the die, or select your next position? (d/u): ")
    while (selection.lower() != "d" and selection.lower() != "u"):
        selection = input("What you typed is not d or u. Please try again: ")
    if selection.lower() == d:
        dice_roll = r.randint(1, 6)
        print("\nThe die was... " + str(dice_roll))
        print("The previous position was... " + str(position))
        position = (position + r.randint(1, 6)) % len(planet_list)
        print("and the next position is... " + str(position))
    else:
        position = input("\nWhich planet would you like to go to next? (0 - " + str(len(planet_list)) + "): ")
        while (position.isdigit() == False or int(position) < 0 or int(position) > len(planet_list)):
            if position.isdigit() == False:
                position = input("That is not a positive integer. Please try again: ")
            else:
                position = input("That value is not within the valid range. Please try again: ")
        print("\nOkay! Travelling to planet " + str(position))
    return position


def encounter(fuel_amount, civ_lvl, position, localList):
    alien_lvl = str(localList[position][0])
    if alien_lvl > 0:
        print("There are aliens on this planet! Their civilization level is " + alien_lvl)
        if civ_lvl > alien_lvl:
            print("\nGreat! The astronaut is more civilized than the aliens!")
            loss_gain = r.randint(1, localList[position][1])
            localList[position][1] += loss_again
        elif civ_lvl = alien_lvl:
            print("\nOh well... the astronaut is equally as civilized as the aliens")
            loss_gain = 0 - r.randint(1, (fuel_amount/2))
        else:
            print("\nOh no! The astronaut is less civilized than the aliens.")
            loss_gain = 0 - r.randint(1, fuel_amount)
    fuel_amount += loss_gain
    return fuel_amount
'''
def rock_collection(position,):
'''



def turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, local_list):
    rock_counter = []
    turn_counter = 1
    while turn_counter <= max_turns:
        #display_board()
        print("Now showing the astronaut. Commencing turn number " + str(turn_counter))
        print("\nThe astronaut " + name + "'s civilation level is " + str(civ_lvl))
        print("Right now, he is in position " + str(position))
        print("and has " + str(fuel_amount) + " fuel litres")
        print("and collected until and including this turn" + rock_counter + "rock specimens") #ADD THE FUNCTION FOR ROCKS
        print("He is alive and ready to move")






#-----------------------------------------------------------------Top Level--------------------------------------------------------------------------------------#




