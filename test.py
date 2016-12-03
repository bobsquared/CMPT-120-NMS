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
    while (max_turns.isdigit() == False or int(max_turns) < 0 or int(max_turns) > 1000000):
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

def movement(planet_number, position):
        #This part asks rhe user if he would like to roll the die or choose the noext position
    selection = input("\nWould you like to roll the die, or select your next position? (d/u): ")
    while (selection.lower() != "d" and selection.lower() != "u"):
        selection = input("What you typed is not d or u. Please try again: ")
        #This part is the dice roll

    rand = r.randint(1,6)
    res = rand + position
    if selection.lower() == "d":
        while res >= len(planet_number):
            res -= len(planet_number)
        print("the die was... " + str(rand))
        print("the previous position was... " + str(position))
        print("and the next position is... " + str(res))
        #This part is asking the user where he wants to go with verification of inputs
    else:
        res = input("\nWhich planet would you like to go to next? (0 - " + str(len(planet_number)-1) + "): ")
        while (res.isdigit() == False or int(res) < 0 or int(res) > len(planet_number)-1):
            if res.isdigit() == False:
                res = input("That is not a positive integer. Please try again: ")
            else:
                res = input("That value is not within the valid range. Please try again: ")
        print("\nOkay! Travelling to planet " + str(res))
    res = int(res)
    return res


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
            print("Planet " + str(position) + " now has " + str(listOfString[position][1]) + " litres.")
            fuel_amount += loss_gain
            print("\n\nThe astronaut now has " + str(fuel_amount) + " fuel litres.")
            listOfString[position][1] -= loss_gain
        #This case is where the astronaut has a draw
        elif int(civ_lvl) == alien_lvl:
            print("\nOh well... the astronaut is equally as civilized as the aliens")
            if int((round(fuel_amount/2)))== 0:
                loss_gain = 0
            else:
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
        print("Planet " + str(position) + " now has " + str(listOfString[position][1]) + " litres.")
        fuel_amount += loss_gain
        print("\n\nThe astronaut now has " + str(fuel_amount) + " fuel litres.")
        listOfString[position][1] -= loss_gain
    return fuel_amount

def rock_collection(position, rock_counter, rock_list):
    if round(rock_list[position]/3) == 0:
        print ("Unfortunately, there were no rocks to collect!")
    else:
        rock_counter.append(round(rock_list[position]/3))
        print("\nYay! The astronaut collected " + str(round(rock_list[position]/3)) + " rocks!")
        print("His rock collection is now " + str(rock_counter))
        print("The planet " + str(position) + " now has " + str(listOfString[position][2] - round(rock_list[position]/3)) + " rocks.")
    listOfString[position][2] -= round(rock_list[position]/3)
    return rock_counter, rock_list
    
def turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, listOfString, rock_counter): 
    print("Now showing the astronaut. Commencing turn number " + str(turn_counter))
    print("\nThe astronaut " + name + "'s civilation level is " + str(civ_lvl))
    print("Right now, he is in position " + str(position))
    print("and has " + str(fuel_amount) + " fuel litres")
    print("and collected until and including this turn " + str(rock_counter) + " rock specimens")
    print("He is alive and ready to move!")
    return

def end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet):
    show_board(" end of game")
    print("Showing astronaut ... end of game")
    print("\nThe astronaut " + name + " has civilization level " + str(civ_lvl))
    print("He is in position: " + str(position))
    print("and currently has: " + str(fuel_amount) + " fuel litres")
    print("and collected during the whole game" + str(rock_counter) + " rock specimens.")
    if turn_counter == int(max_turns):
        print("So... he is very alive!")
        print("but he cannot move anymore since the game ended!")
    elif int(fuel_amount) == 0:
        print("He is stranded since he has no fuel!")
    elif position == python_planet:
        print("So... he is very alive!")
        print("And he also reached Python Planet,so he won!!!")
    yes_no = input("\nDo you want to play again? (y/n): ")
    while (yes_no.lower() != "y" and yes_no.lower() != "n"):
        yes_no = input("\nWhat you typed was not y or n. Please try again: ")
    if yes_no.lower() == "y":
        print("Let's get started again then.")
        turn_counter = 0
        fuel_amount = 1
        position = 0
        rock_counter = []
    return yes_no, turn_counter, fuel_amount, position, rock_counter

def end_of_all_games(game_count, win_count):
    print("\nThe user played " + str(game_count) + " games in total")
    print("of those, the astonaut won " + str(win_count))
    print("To conclude, the program will do a conversion from binary to decimal!")
    print("taking as source the  list of rock specimens in the last game board")
    return

def binaryList(lis):
    print("\nList with rock specimens: " + str(lis))
    newList = []
    for i in range(len(lis)):
        newList.append(lis[i]%2)
    print("Corresponding binary: " + str(newList))
    return newList

def toBase10(lis):
    num = 0
    negative = False
    if(lis[0] == 1):
        negative = True
        for i in range(len(lis)):
            if(lis[i] == 1):
                lis[i] = 0
            else:
                lis[i] = 1
        addOne(lis)
    for i in range(len(lis)):
        digit = lis[len(lis)-1-i]
        newDigit = digit * m.pow(2,i)
        num += newDigit
    if(negative):
        num = 0 - num
    return int(num)

def addOne(lis):
    i = len(lis) - 1
    done = False
    while(not done):
        if(lis[i] == 0):
            lis[i] = 1
        else:
            lis[i] = 0
        i -= 1
        if((i < 0) or (lis[i + 1] == 1)):
            done = True
    return lis


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

def file():
    file = input("\nType the name of the board file including '.txt' or type d for default :")
    while (file.lower() != "d" and file.find(".txt") == -1):
        file = input("You did not type the file name correctly. Try again: ")
    if file.lower() == "d":
        res = "planetsData1.txt"
    else:
        res = file
    return res

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


            
            
def display_board(planet_number,lst,pos,python_planet):
    result = "Planet#            CivLevel          Fuel               Rocks \n"
    for i in range(len(lst)):
        result += str(planet_number[i]) 
        for k in range(len(lst[i])):
            if len(str(lst[i][k])) == 1:
                result += "                  " + str(lst[i][k])
            else:
                result += "                 " + str(lst[i][k])
        if python_planet == i and python_planet > 0:
            result += "       <===== Python Planet     "
        if planet_number[i] == pos:
            result += "       <===== Astronaut Position\n"
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
    print ("\n The board at this point contains...\n")

    # your code...
    return display_board(planet_number,listOfString,position,python_planet)


    

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
        show_board("after mild explosion")
    return planet_rocks

def amazing_explosions(listOfString,planet_lst,planet_fuel,planet_rocks,pos,python_planet):
    global amazing_count
    planet_position = 0
    random = (r.randint(1,len(planet_lst)*5))
    for i in range(len(planet_lst)-1):
        if (random == (i+1)):
            print("\nOooooh! A mild or amazing explosion is happening in planet # " + str(i+1) + " \n the board will have more rock specimens!")
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
        pos -=1
        python_planet -=2
        print("\n\nOh oh! An amazing explosion occured in planet # " + str(planet_position) + "\nThis planet will dissapear!\nand the board shrunk\nbut the astronaut was not there and it did not affect his position...")
        show_board("after amazing explosion")
    
    return [planet_rocks,planet_lst,python_planet,pos]











#========================================================================#
import random as r
import turtle as t
import math as m

fuel_amount = 1
game_count = 0
win_count = 0
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
python_planet = 0
if yes_no == "y":   
    show_board("just created")

python_planet = int(input("Which position should python planet be? (0-" + str(len(planet_number)-1) + ") 0 no affect"))
while not(str(python_planet).isdigit()) or python_planet <0 or python_planet > (len(planet_number)-1):
    if not(python_planet.isdigit):
        python_planet = int(input("That is not a positive integer. Please try again: "))
    else:
        python_planet = int(input("That value is not within the valid range. Please try again: "))
if python_planet == 0:
    python_planet = int(-1)

while yes_no.lower() == "y":
    while turn_counter <= int(max_turns) and int(fuel_amount) > 0:

        if turn_counter == 1:
            data = file()
            listStrings = read_string_list_from_file(data)
            listOfString = convert_to_list(listStrings)
        
            planet_number = planet_num(listOfString)
            planet_civ_level = (create_lists_board(listOfString))[0]
            planet_fuel = (create_lists_board(listOfString))[1]
            planet_rocks = (create_lists_board(listOfString))[2]
            display_board(planet_number,listOfString,position, python_planet)
            name, civ_lvl, fuel_amount, max_turns, amaz_expl, mild_expl, position = game_info()
    
        display_board(planet_number,listOfString,position, python_planet)
    
        turn(name, civ_lvl, position, fuel_amount, max_turns, mild_expl, amaz_expl, listOfString, rock_counter)

        if amaz_expl.lower() == "y" and position > 0:
            result = amazing_explosions(listOfString,planet_number,planet_fuel,planet_rocks,position,python_planet)
            python_planet = result[2]
            position = result[3]
            print(position)
            planet_number = result[1]
            planet_rocks = result[0]
            mild_expl = "n"
        elif amaz_expl.lower() == "y" and position == 0:
            result = amazing_explosions(listOfString,planet_number,planet_fuel,planet_rocks,position,python_planet)
            planet_number = result[1]
            planet_rocks = result[0]
            mild_expl = "n"
        if mild_expl.lower() == "y":
            mild_explosions(listOfString,planet_number,planet_rocks)

        position = movement(planet_number, position)
        if position != python_planet:
            fuel_amount = encounter(fuel_amount, civ_lvl, position, planet_fuel, planet_civ_level)

            if int(fuel_amount) > 0:
                rock_counter, rock_list = rock_collection(position, rock_counter, planet_rocks)
            else:
                game_count += 1
                yes_no, turn_counter, fuel_amount, position, rock_counter = end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet) 

        else:
            print("WOW! The astronaut reached Python Planet and the game is now over!")
            game_count += 1
            win_count += 1
            yes_no, turn_counter, fuel_amount, position, rock_counter = end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet)

        if turn_counter == int(max_turns):
            game_count += 1    
            yes_no, turn_counter, fuel_amount, position, rock_counter = end_of_game(name, civ_lvl, position, fuel_amount, rock_counter, max_turns, turn_counter, python_planet)

        turn_counter += 1

end_of_all_games(game_count, win_count)
newList = binaryList(planet_rocks)
num = toBase10(newList)

print("Which converted to decimal is "+ str(num) + ".")
print("Goodbye!")
