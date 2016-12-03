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
    fuel_amount = int(input("\nHow much fuel do you start with? (10 - 50): "))
    while (str(fuel_amount).isdigit() == False or int(fuel_amount) < 10 or int(fuel_amount) > 50):
        if fuel_amount.isdigit() == False:
            fuel_amount = int(input("That is not a positive integer. Please try again: "))
        else:
            fuel_amount = int(input("That value is not within the valid range. Please try again: "))
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
        #This part is the dice roll
    
    if selection.lower() == "d":
        dice_roll = r.randint(1, 6)
        print("\nThe die was... " + str(dice_roll))
        print("The previous position was... " + str(position))
        position = (position + dice_roll) % len(planet_list)
        print("and the next position is... " + str(position))
        #This part is asking the user where he wants to go with verification of inputs
    else:
        position = input("\nWhich planet would you like to go to next? (0 - " + str(len(planet_list)-1) + "): ")
        while (position.isdigit() == False or int(position) < 0 or int(position) > len(planet_list)-1):
            if position.isdigit() == False:
                position = input("That is not a positive integer. Please try again: ")
            else:
                position = input("That value is not within the valid range. Please try again: ")
        print("\nOkay! Travelling to planet " + str(position))
    position = int(position)
    return position


def encounter(fuel_amount, civ_lvl, position, fuel_list, alienlvl_list):
    alien_lvl = alienlvl_list[position]
        #This section is executed if there are aliens on the planet
    if int(alien_lvl) > 0:
        print("\nThere are aliens on this planet! Their civilization level is " + str(alien_lvl))
        #This case is where the astronaut wins
        if int(civ_lvl) > alien_lvl:
            print("\nGreat! The astronaut is more civilized than the aliens!")
            if fuel_list[position] == 0:
                loss_gain = 0
            else:
                loss_gain = r.randint(1, fuel_list[position])
            fuel_list[position] -= loss_gain
            print("He won " + str(loss_gain) + " fuel litres.")
            print("Planet " + str(position) + " now has " + str(fuel_list[position]) + " litres.")
            fuel_amount += loss_gain
            print("\n\nThe astronaut now has " + str(fuel_amount) + " fuel litres.")
        #This case is where the astronaut has a draw
        elif int(civ_lvl) == alien_lvl:
            print("\nOh well... the astronaut is equally as civilized as the aliens")
            loss_gain = r.randint(1, int((round(fuel_amount/2))))
            print("He lost " + str(loss_gain) + " fuel litres.")
            fuel_amount -= loss_gain
            print("\n\nThe astronaut now has " + str(fuel_amount) + " fuel litres.")
        #This case is where the astronaut loses
        else:
            print("\nOh no! The astronaut is less civilized than the aliens.")
            loss_gain = r.randint(1, int(fuel_amount))
            print("He lost " + str(loss_gain) + " fuel litres.")
            fuel_amount -= loss_gain
            print("\n\nThe astronaut now has " + str(fuel_amount) + " fuel litres.")
    #This section of code executes if there are not aliens on the planet
    else:
        print("\nThere are no aliens on this planet.")
        if fuel_list[position] == 0:
            loss_gain = 0
        else:
            loss_gain = r.randint(1, fuel_list[position])
        fuel_list[position] += loss_gain
        print("He won " + str(loss_gain) + " fuel litres.")
        print("Planet " + str(position) + " now has" + str(fuel_list[position]) + " litres.")
        fuel_amount += loss_gain
        print("\n\nThe astronaut now has " + str(fuel_amount) + " fuel litres.")
    return fuel_amount

def rock_collection(position, rock_counter, rock_list):
    rock_counter.append(round(rock_list[position]/3))
    print("\nYay! The astronaut collected " + str(round(rock_list[position]/3)) + " rocks!")
    print("His rock collection is now " + str(rock_counter))
    print("The planet " + str(position) + " now has " + str(rock_list[position] - round(rock_list[position]/3)) + " rocks.")
    return rock_counter
    
def turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, listOfString, rock_counter): 
    print("Now showing the astronaut. Commencing turn number " + str(turn_counter))
    print("\nThe astronaut " + name + "'s civilation level is " + str(civ_lvl))
    print("Right now, he is in position " + str(position))
    print("and has " + str(fuel_amount) + " fuel litres")
    print("and collected until and including this turn " + str(rock_counter) + " rock specimens")
    print("He is alive and ready to move!")
    return

def read_string_list_from_file(the_file):
    '''
    CODE PROVIDED TO INCORPORATE
    
    <file-name including extension .txt>(String) --> List of strings
    
    Assumptions:
    1) the_file is in the same directory as this program 
    2) the_file contains one planet data per line 
    3) after the data of each planet in the file  there is a return (
       so that the next planet is in the next line), and also
      there is (one single) return after the last planet
      in the_file
    

    to call or invoke this function:
    listStrings = read_string_list_from_file(<file-name.txt in quotes>)
    using the data provided the call to this function would be:
    
    listStrings = read_string_list_from_file("planetsData1.txt")
    '''
    
    fileRef = open(the_file,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()  
        
    #........
    #print ("\n JUST TO TRACE, the local list of strings is:\n")
    #for element in localList:
    #    print (element)
    #print ()
    #........
        
    return localList



def create_lists_board(listStrings):
    
    '''
    Assumptions:
    
    1) The listStrings parameter will have a list with the strings,
    2) each string corresponds to the data for one planet
    3) de string for each planet is:  civlevel-fuel-rocks
    4) civleve, fuel and rocks are integer numbers each
    '''

    # RECOMMENDED THAT YOU IMPLEMENT THIS
    #
    # your code will process the  parameter list and return 3 lists:
    
    # one list for the civilization level in each planet,
    # one list for the fuel liters in each planet
    # one list for the rock specimens in each planet
    civlevel = []
    fuel = []
    rocks = []
    for i in range(len(listStrings)):
        civlevel += [listStrings[i][0]]
        fuel += [listStrings[i][1]]
        rocks += [listStrings[i][2]]
    return [civlevel,fuel,rocks]


            
            
def display_board(planet_number,lst,pos):
    result = "Planet#            CivLevel          Fuel               Rocks \n"
    for i in range(len(lst)):
        result += str(planet_number[i]) 
        for k in range(len(lst[i])):
            if len(str(lst[i][k])) == 1:
                result += "                  " + str(lst[i][k])
            else:
                result += "                 " + str(lst[i][k])
        if planet_number[i] == pos:
            result += "       <===== Astronaught Position\n"
        else:
            result += "\n"
    print (result)
    return 


def show_board(title):
    
    #RECOMMENDED
    #This will be useful to show the board each time that
    #the borad needs to be shown to the user.
    #the parameter title woudl allow that the function is called
    #at differnt times and the title so indicates: exmple: after creation",
    #before turn number xxx, etc
    
    print ("\nShowing board... " + title)
    print ("\n The board at this point contains...")

    # your code...
    return display_board(planet_number,listOfString,pos)


    

def convert_to_list(a):
    res = []
    for i in range(len(a)):
        lst = []
        st = ""
        for k in range(len(a[i])):
            if a[i][k].isdigit() and not(k == (len(a[i])-1)):
                st += a[i][k]
            elif k == (len(a[i])-1):
                st += a[i][k]
                lst.append(int(st))
            else:
                lst.append(int(st))
                st = ""
        res += [lst]
    return res


def planet_num(a):
    res = []
    for i in range(len(a)):
        res += [i]
    return res


def roll_die(pos,planet_number):
    rand = r.randint(1,6)
    res = rand + pos
    while res >= len(planet_number):
        res -= len(planet_number)
    print("the die was... " + str(rand))
    print("the previous position was... " + str(pos))
    print("and the next position is... " + str(res))
    return res



def replace_rocks(planet_rocks,listOfString):
    for i in range(len(planet_rocks)):
        listOfString[i][2] = planet_rocks[i]
    listOfString[0] = [0,0,0]
    return
            
def mild_explosions(listOfString,planet_lst,planet_rocks):
    global mild_count
    planet_position = 0
    random = (r.randint(1,len(planet_lst)*5))
    for i in range(len(planet_lst)-1):
        if (random == (i+1)):
            print("\nOooooh! A mild or amazing explosion is happening in planet # " + str(i+1) + " \n the board will have more rock specimens!")
            mild_count += 1
            planet_position = (i+1)
    for i in range(planet_position):
        for k in range(planet_position,i,-1):
            planet_rocks[i] = planet_rocks[i] + planet_rocks[k]
    replace_rocks(planet_rocks,listOfString)
    if (random == (i+1)):
        print("\nShowing the board after the mild explosion.")
        display_board(planet_number,listOfString,position)
    return planet_rocks

def amazing_explosions(listOfString,planet_lst,planet_fuel,planet_rocks):
    global amazing_count
    planet_position = 0
    random = (r.randint(1,len(planet_lst)*5))
    for i in range(len(planet_lst)-1):
        if (random == (i+1)):
            print("Oooooh! A mild or amazing explosion is happening in planet # " + str(i+1) + " \n the board will have more rock specimens!")
            amazing_count += 1
            planet_position = (i+1)
    for i in range(planet_position):
        for k in range(planet_position,i,-1):
            planet_rocks[i] = planet_rocks[i] + planet_rocks[k]
    replace_rocks(planet_rocks,listOfString)
    if planet_position > 0:
        del planet_rocks[planet_position]
        del listOfString[planet_position]
        planet_lst = planet_num(listOfString)
        
    return [planet_rocks,planet_lst]











#========================================================================#
import random as r

mild_count = 0
amazing_count = 0
max_turns = 1000000
turn_counter = 1
position = 0
rock_counter = []

listStrings = read_string_list_from_file("planetsData1.txt")
listOfString = convert_to_list(listStrings)

yes_no = start_game()


planet_number = planet_num(listOfString)
planet_civ_level = (create_lists_board(listOfString))[0]
planet_fuel = (create_lists_board(listOfString))[1]
planet_rocks = (create_lists_board(listOfString))[2]
display_board(planet_number,listOfString,position)


while yes_no == "y" and turn_counter <= int(max_turns):

    if turn_counter == 1:
        name, civ_lvl, fuel_amount, max_turns, amaz_expl, mild_expl, position = game_info()

    display_board(planet_number,listOfString,position)
    
    turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, listOfString, rock_counter)

    if amaz_expl.lower() == "y" and mild_expl == "y":
        amazing_explosions(listOfString,planet_number,planet_fuel,planet_rocks)
    
    if mild_expl.lower() == "y":
        mild_explosions(listOfString,planet_number,planet_rocks)

    position = movement(planet_number, position)
    
    fuel_amount = encounter(fuel_amount, civ_lvl, position, planet_fuel, planet_civ_level)

    rock_counter = rock_collection(position, rock_counter, planet_rocks)

    turn_counter += 1

print("Oh no, youve reached the max amount of turns.")
