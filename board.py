


#### CMPT 120
#### Planets, Aliens and Explosions Game
#### game copyright - Diana Cukierman
#### author: Diana Cukierman


#### CODE TO BE INCORPORATED IN YOUR OWN PROGRAM
#### Incorporate with the comments exactly as indicated here.
# yu may revise and in that case  include  additional comments as well

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
            print("Oooooh! A mild or amazing explosion is happening in planet # " + str(i+1) + " \n the board will have more rock specimens!")
            mild_count += 1
            planet_position = (i+1)
    for i in range(planet_position):
        for k in range(planet_position,i,-1):
            planet_rocks[i] = planet_rocks[i] + planet_rocks[k]
    replace_rocks(planet_rocks,listOfString)
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




#-----------------------------Top Level--------------------------#8========D
import random as r

amazing_count = 0
mild_count = 0

pos = 0
listStrings = read_string_list_from_file("planetsData1.txt")
listOfString = convert_to_list(listStrings)

planet_number = planet_num(listOfString)
planet_civ_level = (create_lists_board(listOfString))[0]
planet_fuel = (create_lists_board(listOfString))[1]
planet_rocks = (create_lists_board(listOfString))[2]
i = 0



##UNQUOTE THIS PART TO TEST AMAZING EXPLOSIONS
##CONTROL C TO STOP THE LOOP
'''
while i<1:
    show_board("lol")
    planet = (amazing_explosions(listOfString,planet_number,planet_fuel,planet_rocks))
    planet_rocks = planet[0]
    planet_number = planet[1]
    pos = roll_die(pos,planet_number)
    print(planet_number)
'''

##UNQUOTE THIS PART TO TEST MILD EXPLOSIONS
##CONTROL C TO STOP THE LOOP
'''
while i<1:
    show_board("lol")
    planet_rocks = (mild_explosions(listOfString,planet_number,planet_rocks))
    pos = roll_die(pos,planet_number)
    print(planet_number)
'''












