## Explosions for Final assignment

def mild_explosions(planet_lst,planet_rocks):
    global mild_count
    planet_position = 0
    random = (r.randint(1,len(planet_lst)*5))
    for i in range(len(planet_lst)):
        if (random == (i+1)):
            print("Oooooh! A mild or amazing explosion is happening in planet # " + str(i+1) + " \n the board will have more rock specimens!")
            mild_count += 1
            planet_position = (i+1)
    for i in range(planet_position):
        for k in range(planet_position - 1,i,-1):
            planet_rocks[i] = planet_rocks[i] + planet_rocks[k]
    return planet_rocks
##Mild explosions inputs the planet number list and the planet rocks list. It returns a new list for the planet rocks after the mild explosion occurs.
##Input and output does not include planet 0 as the explosions don't affect it.
##Global variable for mild_count so that we can count how many times the mild_explosion occurs in the game.






def amazing_explosions(planet_lst,planet_rocks):
    global amazing_count
    planet_position = 0
    random = (r.randint(1,len(planet_lst)*5))
    for i in range(len(planet_lst)):
        if (random == (i+1)):
            print("Oooooh! A mild or amazing explosion is happening in planet # " + str(i+1) + " \n the board will have more rock specimens!")
            amazing_count += 1
            planet_position = (i+1)
            del planet_lst[-1]
    for i in range(planet_position):
        for k in range(planet_position - 1,i,-1):
            planet_rocks[i] = planet_rocks[i] + planet_rocks[k]
    if planet_position > 0:
        del planet_rocks[planet_position-1]
    return [planet_rocks,planet_lst]
##Amazing explosions inputs the planet number list and the planet rocks list. It returns a list of lists.
##A new list for the planet rocks after the explosion occurs, and a new list for the number of planets.
##Input and output does not include planet 0 as the explosions don't affect it.
##Global variable for amazing_count so that we can count how many times the amazing_explosion occurs in the game.
