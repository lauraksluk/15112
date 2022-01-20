#################################################################
# 15-112-m19 hw12
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C

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
        #specifies type is normal asteroid
        self.kind = "Asteroid"

    # Updates direction based on new direction
    def setDirection(self,dir):
        self.direction = dir

    # Returns direction
    def getDirection(self):
        return self.direction

    # Returns string of the type of asteroid, center coordinates, radius, and
    # direction
    def __repr__(self):
        return "%s at (%d, %d) with radius=%d and direction (%d, %d)" % \
        (self.kind,self.cx, self.cy, self.radius, self.direction[0], \
        self.direction[1])

    # Returns Boolean value depending on if asteroid hit a wall
    def isCollisionWithWall(self,canvasWidth,canvasHeight):
        x0 = self.cx - self.radius
        y0 = self.cy - self.radius
        x1 = self.cx + self.radius
        y1 = self.cy + self.radius
        if x0 <= 0 or y0 <= 0 or x1 >= canvasWidth or y1 >= canvasHeight:
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

# A class, ShrinkingAsteroid, is defined as a subclass of Asteroid
# Has most of same properties, and a shrink factor
# Has most of same methods
class ShrinkingAsteroid (Asteroid):

    # Initialize attributes
    def __init__(self,cx,cy,radius,speed,direction = (0,1),shrinkAmount = 5):
        #has same attributes as Asteroid
        super().__init__(cx,cy,radius,speed,direction)
        #specifies type is a shrinking asteroid
        self.kind = "ShrinkingAsteroid"
        self.shrinkAmount = shrinkAmount

    # Updates radius by shrink factor when hit by bullet
    def reactToBulletHit(self):
        self.radius -= self.shrinkAmount

    # Shrinking asteroids bounce off walls
    def bounce(self):
        dx = self.direction[0]*-1
        dy = self.direction[1]*-1
        self.direction = (dx,dy)

# A class, SplittingAsteroid, is defined as a subclass of Asteroid
# Has most of same properties
# Has most of same methods
class SplittingAsteroid(Asteroid):

    # Initialize attributes
    def __init__(self,cx,cy,radius,speed,direction = (0,1)):
        #has same attributes as Asteroid
        super().__init__(cx,cy,radius,speed,direction)
        #specifies type is a splitting asteroid
        self.kind = "SplittingAsteroid"

    # Splits into two new asteroids when hit by bullet
    # Returns the two new instances of Splitting Asteroid class
    def reactToBulletHit(self):
        #new center is at top-left corner of original
        cx1 = self.cx - self.radius
        cy1 = self.cy - self.radius
        #new radius is half of original
        r1 = self.radius//2
        #new asteroid has same speed and direction as original
        newAsteroid1 = SplittingAsteroid(cx1,cy1,r1,self.speed,self.direction)
        #new center is at bottom-right corner of original
        cx2 = self.cx + self.radius
        cy2 = self.cy + self.radius
        newAsteroid2 = SplittingAsteroid(cx2,cy2,r1,self.speed,self.direction)
        return newAsteroid1, newAsteroid2

#################################################################

# Starter Code begins here. Read and understand it!

import random, math

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

# Read this class carefully! You'll need to call the methods!
class Rocket(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.angle = 90

    def rotate(self, numDegrees):
        self.angle += numDegrees

    def bulletInfo(self):
        offset = 10
        dx, dy = (offset*math.cos(math.radians(self.angle)),
                            offset*math.sin(math.radians(self.angle)))
        speedLow, speedHigh = 20, 40

        return (self.cx+dx, self.cy-dy, self.angle,random.randint(speedLow, speedHigh))

    def makeBullet(self):
        offset = 10
        dx, dy = (offset*math.cos(math.radians(self.angle)),
                            offset*math.sin(math.radians(self.angle)))
        speedLow, speedHigh = 20, 40

        return Bullet (self.cx+dx, self.cy-dy, self.angle,random.randint(speedLow, speedHigh))

    def draw(self, canvas):
        size = 30
        drawTriangle(canvas, self.cx, self.cy,
            math.radians(self.angle), size, fill="green2")

# Read this class carefully! You'll need to call the methods!
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
                                        < self.r + other.r)

    def draw(self, canvas):
        cx, cy, r = self.cx, self.cy, self.r
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
            fill="white", outline=None)

    def onTimerFired(self, data):
        self.moveBullet()

#################################################################

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.rocket = Rocket(data.width//2, data.height//2)
    data.singleBullet = data.rocket.makeBullet()
    data.bullets = []
    data.singleBullet.angle = data.rocket.angle
    data.shoot = False


def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == 'Right':
        data.rocket.rotate(-15)
    if event.keysym == 'Left':
        data.rocket.rotate(15)
    if event.keysym == 'space':
        data.shoot = True
        data.singleBullet
        data.bullets.append(data.rocket.bulletInfo())




def timerFired(data):
    # it might be a good idea to define onTimerFired methods in your classes...
    if data.shoot == True:
        data.singleBbullet.onTimerFired(data)

def redrawAll(canvas, data):
    # draws the rocket and background
    canvas.create_rectangle(0, 0, data.width, data.height, fill="gray3")
    data.rocket.draw(canvas)
    if data.shoot == True:
        data.singleBullet.draw(canvas)
    # don't forget to draw asteroids and bullets!

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