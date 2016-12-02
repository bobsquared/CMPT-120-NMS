def roll_die(pos,planet_number):
    choose = input("(d/u) : ")
    rand = r.randint(1,6)
    res = rand + pos
    if choose == "d":
        while res >= len(planet_number):
            res -= len(planet_number)
        print("the die was... " + str(rand))
        print("the previous position was... " + str(pos))
        print("and the next position is... " + str(res))
    elif choose == "u":
        lol = input("planet")
        res = int(lol)
    else:
        roll_die(pos,planet_number)
    return res

#-------------------------------------------------------
##Returns the position of the player after you roll the die.
##Bottom is example
import random as r

pos = 0
planet_number = [0,1,2,3]
pos = roll_die(pos,planet_number)
pos = roll_die(pos,planet_number)
pos = roll_die(pos,planet_number)
pos = roll_die(pos,planet_number)

