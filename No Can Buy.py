##No Man's Sky? More like, No Can Buy! Yukyukyuk!##
import turtle as t

def drawPlanet(lis):
    t.pencolor(determinePlanetOutlineColour(lis))
    t.fillcolor(determinePlanetFillColour(lis))
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

def drawSpace():
    t.penup()
    t.forward(70)
    t.pendown()

def drawAllPlanets(lis):
    t.speed(0)
    startPos(len(lis))
    for i in range(len(lis)):
        drawPlanet(lis[i])
        drawSpace()

def drawAstro(planets, pos, fuel):
    t.penup()
    t.fillcolor(determineShipColour(fuel))
    t.backward(70*(planets-pos))
    t.right(90)
    t.forward(150)
    t.left(90)
    t.forward(25)
    t.pencolor("black")
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

def startPos(n):
    t.penup()
    space = 0
    if((n%2)==0):
        space = n/2
        t.backward((space*50)+((space-1)*20)+10)
    else:
        space = n//2
        t.backward((space*50)+(space*20)+25)
    t.pendown()
    '''space = (n-1)*50 + 25
    t.backward(space)
    t.pendown()'''

def determinePlanetFillColour(lis):
    colour = (0, 0, 0)
    value = lis[2] * 17
    if(value < 1):
        colour = (0, 0, 0)
    elif(value < 255):
        colour = (0, value, 0)
    elif(value < 455):
        colour = ((value - 255), 255, (value - 255))
    else:
        colour = (200, 255, 200)
    return colour

def determinePlanetOutlineColour(lis):
    colour = ""
    if(lis[1] > 0):
        colour = "orange"
    else:
        colour = "black"
    return colour

def determineShipColour(fuel):
    colour = ""
    if(fuel < 1):
        colour = "red"
    elif(fuel < 10):
        colour = "yellow"
    else:
        colour = "green"
    return colour

#Planets is the matrix of planets, pos is the position of the player,
#fuel is the amount of fuel the player has
def drawBoard(planets, pos, fuel):
    t.colormode(255)
    t.pensize(5)
    drawAllPlanets(planets)
    drawAstro(len(planets), pos, fuel)


#Test case for drawBoard()
#drawBoard([[0, 0, 0],[1, 10, 20],[3, 10, 15],[2, 30, 20],[1, 0, 5],
#           [1, 10, 6],[3, 10, 30],[3, 10, 4]], 0, 10)
