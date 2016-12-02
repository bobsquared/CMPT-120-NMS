

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
        #This part asks rhe user if he would like to roll the die or choose the noext position
    selection = input("\nWould you like to roll the die, or select your next position? (d/u): ")
    while (selection.lower() != "d" and selection.lower() != "u"):
        selection = input("What you typed is not d or u. Please try again: ")
        #This part is the dice rol
    if selection.lower() == d:
        dice_roll = r.randint(1, 6)
        print("\nThe die was... " + str(dice_roll))
        print("The previous position was... " + str(position))
        position = (position + r.randint(1, 6)) % len(planet_list)
        print("and the next position is... " + str(position))
        #This part is asking the user where he wants to go with verification of inputs
    else:
        position = input("\nWhich planet would you like to go to next? (0 - " + str(len(planet_list)) + "): ")
        while (position.isdigit() == False or int(position) < 0 or int(position) > len(planet_list)):
            if position.isdigit() == False:
                position = input("That is not a positive integer. Please try again: ")
            else:
                position = input("That value is not within the valid range. Please try again: ")
        print("\nOkay! Travelling to planet " + str(position))
    return position


def encounter(fuel_amount, civ_lvl, position, fuel_list, alienlvl_list):
    alien_lvl = str(alienlvl_list[position])
        #This section is executed if there are aliens on the planet
    if alien_lvl > 0:
        print("There are aliens on this planet! Their civilization level is " + alien_lvl)

        #This case is where the astronaut wins
        if civ_lvl > alien_lvl:
            print("\nGreat! The astronaut is more civilized than the aliens!")
            loss_gain = r.randint(1, fuel_list[position])
            fuel_list[position] += loss_again
            print("He won " + str(loss_gain) + " fuel litres.")
            print("Planet " + str(position) + " now has " + str(fuel_list[position]) + " litres.")
            fuel_amount += loss_gain
            print("\n\nThe astronaut now has " + fuel_amount + " fuel litres.")

        #This case is where the astronaut has a draw
        elif civ_lvl = alien_lvl:
            print("\nOh well... the astronaut is equally as civilized as the aliens")
            loss_gain = r.randint(1, (fuel_amount/2))
            print("He lost " + str(loss_gain) + " fuel litres.")
            fuel_amount -= loss_gain
            print("\n\nThe astronaut now has " + fuel_amount + " fuel litres.")

        #This case is where the astronaut loses
        else:
            print("\nOh no! The astronaut is less civilized than the aliens.")
            loss_gain = r.randint(1, fuel_amount)
            print("He lost " + str(loss_gain) + " fuel litres.")
            fuel_amount -= loss_gain
            print("\n\nThe astronaut now has " + fuel_amount + " fuel litres.")
    #This section of code executes if there are not aliens on the planet
    else:
        print("\nThere are no aliens on this planet.")
        loss_gain = r.randint(1, fuel_list[position])
        fuel_list[position] += loss_again
        print("He won " + str(loss_gain) + " fuel litres.")
        print("Planet " + str(position) + " now has" + str(fuel_list[position]) + " litres.")
        fuel_amount += loss_gain
        print("\n\nThe astronaut now has " + fuel_amount + " fuel litres.")

    return fuel_amount

def rock_collection(position, rock_counter, rock_list):
    rock_counter.append(round(rock_list[position]/3))
    print("\nYay! The astronaut collected " + str(round(rock_list[position]/3)) + " rocks!")
    print("His rock collection is now " + rock_counter)
    print("The planet " + str(position) + " now has " + str(rock_list[position] - round(rock_list[position]/3)) + " rocks.")

    return rock_counter
    



def turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, local_list):
    rock_counter = []
    turn_counter = 1
    while turn_counter <= max_turns:
        #display_board()
        print("Now showing the astronaut. Commencing turn number " + str(turn_counter))
        print("\nThe astronaut " + name + "'s civilation level is " + str(civ_lvl))
        print("Right now, he is in position " + str(position))
        print("and has " + str(fuel_amount) + " fuel litres")
        print("and collected until and including this turn" + rock_counter + "rock specimens")
        print("He is alive and ready to move!")

        movement(planet_list, position)

        rock_collection(position, rock_counter, rock_list)
        
        turn_counter += 1

    return






#-----------------------------------------------------------------Top Level--------------------------------------------------------------------------------------#

import random as r


