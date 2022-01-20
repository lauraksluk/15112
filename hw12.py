#################################################################
# 15-112-m19 hw12
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################################

import random, math

#################################################################

# A base class, Asteroid, is defined with properties and methods
# Properties: center coordinates, radius, speed, direction
# Methods: changing direction, moving asteroid, updating asteroid when it
# collides with wall, updating asteroid when it hits a bullet
class Asteroid (object):

    # Initialize attributes
    def __init__(self,cx,cy,radius,speed,direction = (0,1)):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.speed = speed
        self.direction = direction
        #specifies type is normal asteroid and purple
        self.kind = "Asteroid"
        self.color = 'purple'

    # Updates direction based on new direction
    def setDirection(self,dir):
        self.direction = dir

    # Returns direction
    def getDirection(self):
        return self.direction

    # Returns Boolean value depending on if asteroid hit a wall
    def isCollisionWithWall(self,canvasWidth,canvasHeight):
        x0 = self.cx - self.radius
        y0 = self.cy - self.radius
        x1 = self.cx + self.radius
        y1 = self.cy + self.radius
        if x0 < 0 or y0 < 0 or x1 > canvasWidth or y1 > canvasHeight:
            return True
        else:
            return False

    # Moves asteroid based on its speed and direction
    def moveAsteroid(self):
        self.cx += self.speed*self.direction[0]
        self.cy += self.speed*self.direction[1]

    # Returns center coordinates and radius of asteroid
    def getPositionAndRadius(self):
        return (self.cx, self.cy, self.radius)

    # Normal asteroids freeze when hit by bullet
    def reactToBulletHit(self):
        self.direction = (0,0)
        
    # Helper function for timerFired()
    # Normal asteroids wrap around at edge of canvas
    def onTimerFired(self, data):
        if self.isCollisionWithWall(data.width,data.height):
            #going out of bounds on top/left of canvas
            if self.cx - self.radius < 0:
                self.cx = data.width - self.radius
            if self.cy - self.radius < 0:
                self.cy = data.height - self.radius
            #going out of bounds on bottom/right of canvas
            if self.cx + self.radius > data.width:
                self.cx = self.radius
            if self.cy + self.radius > data.height:
                self.cy = self.radius
        #asteroid moves with speed per timerFired() call
        self.moveAsteroid()
    
    # Helper function to draw asteroids
    def draw(self,canvas):
        x0 = self.cx - self.radius
        y0 = self.cy - self.radius 
        x1 = self.cx + self.radius 
        y1 = self.cy + self.radius
        #color depends on kind of asteroid
        canvas.create_oval(x0,y0,x1,y1,fill=self.color)

# A class, ShrinkingAsteroid, is defined as a subclass of Asteroid
# Has most of same properties, and a shrink factor
# Has most of same methods
class ShrinkingAsteroid (Asteroid):

    # Initialize attributes
    def __init__(self,cx,cy,radius,speed,direction = (0,1),shrinkAmount = 5):
        #has most of the same attributes as Asteroid
        super().__init__(cx,cy,radius,speed,direction)
        self.shrinkAmount = shrinkAmount
        #specifies type is a shrinking asteroid and pink
        self.kind = "ShrinkingAsteroid"
        self.color = 'pink'

    # Updates radius by shrink factor when hit by bullet
    def reactToBulletHit(self):
        self.radius -= self.shrinkAmount

    # Shrinking asteroids bounce off walls
    def bounce(self):
        dx = self.direction[0]*-1
        dy = self.direction[1]*-1
        self.direction = (dx,dy)
    
    # Helper function for timerFired()
    # Shrinking asteroids bounce off edge of canvas
    def onTimerFired(self, data):
        if super().isCollisionWithWall(data.width,data.height):
            self.bounce()
        super().moveAsteroid()
    

# A class, SplittingAsteroid, is defined as a subclass of Asteroid
# Has most of same properties
# Has most of same methods
class SplittingAsteroid(Asteroid):

    # Initialize attributes
    def __init__(self,cx,cy,radius,speed,direction = (0,1)):
        #has same attributes as Asteroid
        super().__init__(cx,cy,radius,speed,direction)
        #specifies type is a splitting asteroid and blue
        self.kind = "SplittingAsteroid"
        self.color = 'blue'

    # Splits into two new asteroids when hit by bullet
    # Returns the two new instances of Splitting Asteroid class
    def reactToBulletHit(self):
        #new center is at top-left corner of original
        cx1 = self.cx - self.radius
        cy1 = self.cy - self.radius
        #new radius is half of original
        r1 = self.radius//2
        #new center is at bottom-right corner of original
        cx2 = self.cx + self.radius
        cy2 = self.cy + self.radius
        #new asteroids have same type, speed, direction as original
        newAsteroid1 = SplittingAsteroid(cx1,cy1,r1,self.speed,self.direction)
        newAsteroid2 = SplittingAsteroid(cx2,cy2,r1,self.speed,self.direction)
        return newAsteroid1, newAsteroid2
    
#################################################################

# Starter Code begins here. 

#################################################################

# Helper function for drawing the Rocket
def drawTriangle(canvas, cx, cy, angle, size, fill="black"):
    angleChange = 2*math.pi/3
    p1x, p1y = (cx + size*math.cos(angle), 
                    cy - size*math.sin(angle))
    p2x, p2y = (cx + size*math.cos(angle + angleChange), 
                    cy - size*math.sin(angle + angleChange))
    p3x, p3y = (cx, cy)
    p4x, p4y = (cx + size*math.cos(angle + 2*angleChange),
                    cy - size*math.sin(angle + 2*angleChange))
    
    canvas.create_polygon((p1x, p1y), (p2x, p2y), (p3x, p3y), (p4x, p4y),
                                                                 fill=fill)

class Rocket(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.angle = 90

    def rotate(self, numDegrees):
        self.angle += numDegrees

    def makeBullet(self):
        offset = 10
        dx, dy = (offset*math.cos(math.radians(self.angle)), 
                            offset*math.sin(math.radians(self.angle)))
        speedLow, speedHigh = 20, 40

        return Bullet(self.cx+dx, self.cy-dy,
                self.angle,random.randint(speedLow, speedHigh))

    def draw(self, canvas):
        size = 30
        drawTriangle(canvas, self.cx, self.cy, 
            math.radians(self.angle), size, fill="green2")


class Bullet(object):
    def __init__(self, cx, cy, angle, speed=20):
        self.cx = cx
        self.cy = cy
        self.r = 5
        self.angle = angle
        self.speed = speed

    def moveBullet(self):
        dx = math.cos(math.radians(self.angle))*self.speed
        dy = math.sin(math.radians(self.angle))*self.speed
        self.cx, self.cy = self.cx + dx, self.cy - dy

    def isCollisionWithAsteroid(self, other):
        # in this case, other must be an asteroid
        if(not isinstance(other, Asteroid)):
            return False
        else:
            return (math.sqrt((other.cx - self.cx)**2 + 
                                (other.cy - self.cy)**2)
                                        < self.r + other.radius) 

    def draw(self, canvas):
        cx, cy, r = self.cx, self.cy, self.r
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, 
            fill="white", outline=None)

    def onTimerFired(self, data):
        self.moveBullet()

#################################################################

from tkinter import *

#################################################################

# Initialize variables for game
def init(data):
    #rocket stays in center of screen
    data.rocket = Rocket(data.width//2, data.height//2)
    #list of all bullets and asteroids on screen
    data.bullets = []
    data.asteroids = []
    #time counter for timerFired() events (in multiples of 100 ms)
    data.time = 0
    
# Designates player keys
def keyPressed(event, data):
    #right arrow key rotates rocket clockwise
    if event.keysym == 'Right':
        data.rocket.rotate(-15)
    #left arrow key rotates rocket counterclockwise
    if event.keysym == 'Left':
        data.rocket.rotate(15)
    #space bar shoots bullets from rocket
    if event.keysym == 'space':
        data.bullets.append(data.rocket.makeBullet())

# Creates a new asteroid with all attributes randomly chosen
def getAsteroid(data):
    #random type of asteroid
    newType = random.choice([SplittingAsteroid])
    #random radius, direction, speed
    radius = random.randint(20,40)
    direction = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
    speed = random.randint(5,20)
    #random center coordinates (full asteroids on screen)
    cx = random.randint(radius,data.width-radius)
    cy = random.randint(radius,data.height-radius)
    #create asteroid depending on type
    if newType == Asteroid:
        return Asteroid(cx,cy,radius,speed,direction)
    elif newType == ShrinkingAsteroid:
        return ShrinkingAsteroid(cx,cy,radius,speed,direction)
    else:
        return SplittingAsteroid(cx,cy,radius,speed,direction)

# Removes all frozen asteroids from list of asteroids
def removeFrozenAst(data):
    frozenAst = []
    #create new list of frozen asteroids
    for ast in data.asteroids: 
        if ast.getDirection() == (0,0):
            frozenAst.append(ast)
    #add all asteroids that are not frozen to temporary list
    tempAst = []
    for ast in data.asteroids:
        if ast not in frozenAst:
            tempAst.append(ast)
    #reset list of asteroids to temporary list
    data.asteroids = tempAst

# Designates time based components of game
def timerFired(data):
    #increment time counter for each timerFired() call
    data.time += 1
    #new asteroid is created every 2 seconds
    if data.time % 20 == 0:
        data.asteroids.append(getAsteroid(data))
    #moves each asteroid on screen based on its type
    for ast in data.asteroids:
        ast.onTimerFired(data)
    for bullet in data.bullets:
        #move bullets on screen
        bullet.onTimerFired(data)
        for ast in data.asteroids:    
            if bullet.isCollisionWithAsteroid(ast):
                ast.reactToBulletHit()
                #splitting asteroids split into two when hit by bullet
                if type(ast) == SplittingAsteroid:
                    data.asteroids.append(ast.reactToBulletHit()[0])
                    data.asteroids.append(ast.reactToBulletHit()[1])   
                    #remove original splitting asteroid that was hit
                    data.asteroids.remove(ast) 
                #shrinking asteroids with radius of 15 or less are removed
                if type(ast) == ShrinkingAsteroid and ast.radius <= 15:
                    data.asteroids.remove(ast)
    #every 10 seconds, all frozen normal asteroids are removed
    if data.time % 100 == 0:
        removeFrozenAst(data)
        
 
# Draws game components on canvas
def redrawAll(canvas, data):
    #draws the background and rocket
    canvas.create_rectangle(0, 0, data.width, data.height, fill="gray3")
    data.rocket.draw(canvas)
    #draws all bullets
    for bullet in data.bullets:
        bullet.draw(canvas)
    #draws all asteroids
    for aster in data.asteroids:
        aster.draw(canvas)

#################################################################
# use the run function as-is
#################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)