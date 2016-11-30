def roll_die(pos,planet_number):
    rand = r.randint(1,6)
    print(rand)
    res = rand + pos
    while res >= len(planet_number):
        res -= len(planet_number)
    return res

#-------------------------------------------------------
##Returns the position of the player after you roll the die.

import random as r

pos = 5
planet_number = [0,1,2,3,4,5,6,7]
print(roll_die(pos,planet_number))

