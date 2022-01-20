#################################################
# 15-112-m19 hw10
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################

import string

#################################################
# Helper functions
#################################################

#Returns Boolean value depending on if board is filled or not
def isComplete(board):
    for i in range(len(board)):
        for j in range(len(board)):
            #if any cells are 0, the board is not complete
            if board[i][j] == 0:
                return False
    return True

#Returns Boolean value depending on if letter at current position is valid
#Current position is in one of the 2 diagonals
def isDiagLegal(board,row,col,constraints):
    diagConstraints = constraints["diags"]
    #if position is in main diagonal
    if row == col:
        return board[row][col] in diagConstraints["left"]
    #if position is in minor diagonal
    elif row + col == len(board) - 1:
        return board[row][col] in diagConstraints["right"]

#Checks if letter at current position is valid
def isLegal(board,row,col,constraints):
    rowConstraints = constraints["rows"]
    #checks if letter meets row constraint
    if board[row][col] in rowConstraints[row]:
        return True
    colConstraints = constraints["cols"]
    #checks if letter meets column constraint
    if board[row][col] in colConstraints[col]:
        return True
    #if position is not in the diagonals, letter is not valid
    if row+col != len(board) - 1 and row != col:
        return False
    else:
    #if position is in one of the diagonals, call isDiagLegal to check
    #diagonal constraint
        if isDiagLegal(board,row,col,constraints) == False:
            return False
        else:
            return True

#Helper function for ABC Path game
#Extra parameters: current board, string of letter choices
def abcHelper(board,letters,constraints,aLocation):
    if isComplete(board):
        return board
    row, col = aLocation[0], aLocation[1]
    #list of possible moves for the next adjacent cell
    moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for tuple in moves:
        newRow,newCol = row + tuple[0], col + tuple[1]
        #check if new position is still on board
        if newRow in range(5) and newCol in range(5):
            #check if new position is empty
            if board[newRow][newCol] == 0:
                #fill empty cell with next letter of alphabet
                board[newRow][newCol] = letters[0]
                if isLegal(board,newRow,newCol,constraints):
                    newLoc = (newRow,newCol)
                    #recursive call with new letter choices and new position
                    tempSol = abcHelper(board,letters[1:],constraints,newLoc)
                    if tempSol != None:
                        return tempSol
                board[newRow][newCol] = 0 #undo move
    return None

#################################################
# Problems
#################################################

#Returns a dictionary mapping every person in dictionary, d, to a set of their
#friends of friends (mutual friends excluding direct friends)
def friendsOfFriends(d):
    result = dict()
    #iterate through each key in d
    for name in d:
        #initialize empty set for each name
        result[name] = set()
        #iterate through set of friends
        for friend in d[name]:
            for mutual in d[friend]:
                #excluding original person and direct friends
                if mutual == name or mutual in d[name]:
                    continue
                else:
                    result[name].add(mutual)
    return result

#Returns completed board for ABC Path game with given constraints
#and location for 'A'
def solveABC(constraints,aLocation):
    #initialize 2d list to represent board
    board = []
    for row in range(5):
        board += [[0]*5]
    row, col = aLocation[0], aLocation[1]
    #fill in 'A' with given position
    board[row][col] = 'A'
    #string of letter choices ('B' to 'Y', inclusive)
    letters = string.ascii_uppercase[1:-1]
    return abcHelper(board,letters,constraints,aLocation)

#################################################
#ignore_rest
#################################################

from tkinter import *
import math
import random

#Initialize variables for dotsGalore game
def init(data):
    #list of dots on canvas
    data.dots = []
    #time elapsed in multiples of 100 ms
    data.time = 0
    #list of dots that are removed
    data.dotsRemoved = []
    data.score = 0
    data.gameOver = False
    data.paused = False

#Returns the distance between (x0,y0) and (x1,y1)
def dist(x0,y0,x1,y1):
    result = math.sqrt((x0-x1)**2 + (y0-y1)**2)
    return result

#Designates player clicks
def mousePressed(event, data):
    if data.paused == False:
        for dot in data.dots:
            distance = dist(event.x, event.y, dot[0], dot[1])
            #if player clicks inside a dot
            if distance <= dot[2]:
                #remove dot from canvas
                data.dots.remove(dot)
                #keep track of removed dot
                data.dotsRemoved.append(dot)
                #increment score
                data.score += 1

#Designates player keys
def keyPressed(event, data):
    #restart game if player presses 'r'
    if event.keysym == 'r':
        init(data)
    if event.keysym == 'p':
        #pause game if player presses 'p'
        if data.paused == False:
            data.paused = True
        #unpauses game if game is already paused
        else:
            data.paused = False
    if data.paused == False:
        #if player presses spacebar, the last removed dot reappears
        if event.keysym == 'space' and data.dotsRemoved != []:
            data.dots.append(data.dotsRemoved.pop())

#When two dots collide, both dots will bounce off each other
def didCollide(data):
    for dot1 in data.dots:
        for dot2 in data.dots:
            #ensure the two dots are not the same dot
            if dot1 != dot2:
                #at collision, angle is updated to its negation
                if dist(dot1[0],dot1[1],dot2[0],dot2[1]) <= dot1[2]+dot2[2]:
                    dot1[3] += math.pi/2
                    dot2[3] += math.pi/2

#Designates time-based components in game
def timerFired(data):
    #increment time elapsed every 100 ms
    data.time += 1
    #game is over when all dots are gone and score is at least 5
    if data.dots == [] and data.score >= 5:
        data.gameOver = True
    if data.paused == False:
        #every 2 seconds, a new dot appears
        if data.time % 20 == 0:
            newDot(data)
        #every 10 seconds, every dot grows by 5 pixels
        if data.time % 100 == 0:
            for dot in data.dots:
                dot[2] += 5
        #calls helper function for collisions
        didCollide(data)
        #direction for each dot in list of dots on canvas
        for dot in data.dots:
            dot[0] += math.cos(dot[3])
            dot[1] -= math.sin(dot[3])
            #dots will wrap around when it reaches edge of canvas
            if dot[0] - dot[2] < 0:
                dot[0] = data.width - dot[2]
            if dot[0] + dot[2] > data.width:
                dot[0] = dot[2]
            if dot[1] - dot[2] < 0:
                dot[1] = data.height - dot[2]
            if dot[1] + dot[2] > data.height:
                dot[1] = dot[2]

#Draws canvas for game
def redrawAll(canvas, data):
    if data.gameOver == False:
        #draws each dot in list of dots
        for dot in data.dots:
            x0 = dot[0] - dot[2]
            y0 = dot[1] - dot[2]
            x1 = dot[0] + dot[2]
            y1 = dot[1] + dot[2]
            canvas.create_oval(x0,y0,x1,y1,fill=dot[4])
        #displays score at top of screen
        score = 'Score: ' + str(data.score)
        canvas.create_text(data.width//2,10,text=score)
    #displays game over message
    else:
        canvas.create_text(data.width//2,data.height//2,text='GAME OVER!')

#Creates new dot with random radius, position, direction, and color
def newDot(data):
    #random radius
    rad = random.randint(5,50)
    #random color
    color = random.choice(['red','blue','green','yellow'])
    #random position that is valid on board
    cx = random.randint(rad,data.width-rad)
    cy = random.randint(rad,data.height-rad)
    #random angle in radians
    angle = math.radians(random.randint(0,360))
    #add new dot to list of dots
    data.dots.append([cx,cy,rad,angle,color])

####################################
# use the run function as-is
####################################

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

run(300, 300)

#################################################
# Test functions
#################################################

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end='')
    d = {}
    d["spongebob"] = set(["sandy", "patrick", "mr.krabs", "squidward"])
    d["mr.krabs"] = set(["pearl", "spongebob", "squidward"])
    d["pearl"] = set(["mr.krabs"])
    d["sandy"] = set(["spongebob", "patrick"])
    d["patrick"] = set(["spongebob", "sandy"])
    d["squidward"] = set()
    solution = {
    'spongebob': {'pearl'},
    'mr.krabs': {'patrick', 'sandy'},
    'pearl': {'spongebob', 'squidward'},
    'sandy': {'mr.krabs', 'squidward'},
    'patrick': {'mr.krabs', 'squidward'},
    'squidward': set(),
    }
    assert(friendsOfFriends(d) == solution)

    d = {}
    d['winnie'] = set(['laura','jenny','rui'])
    d['steph'] = set(['rui','laura'])
    d['laura'] = set(['jenny','jon','winnie'])
    d['jenny'] = set(['jon','steph'])
    d['rui'] = set(['steph','winnie'])
    d['jon'] = set()
    solution = {
    'winnie': {'jon','steph'},
    'steph': {'winnie','jenny','jon'},
    'laura': {'steph','rui'},
    'jenny': {'rui','laura'},
    'rui': {'laura','jenny'},
    'jon': set()
    }
    assert(friendsOfFriends(d) == solution)

    d = {}
    d["mak"] = set(["gwen", "laura","allie"])
    d["gwen"] = set(["laura"])
    d["laura"] = set(["mak","allie"])
    d["allie"] = set(["mak"])
    solution = {
    'mak': set(),
    'gwen': {'mak', 'allie'},
    'laura': {'gwen'},
    'allie': {'gwen', 'laura'}
    }
    assert(friendsOfFriends(d) == solution)
    print('Passed!')

def testIsComplete():
    print('Testing isComplete()...', end='')
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    assert(isComplete(board) == False)

    board = [['I', 'J', 'K', 'L', 'A'],
            ['H', 'G', 'F', 'B', 'M'],
            ['T', 'Y', 'C', 'E', 'N'],
            ['U', 'S', 'X', 'D', 'O'],
            ['V', 'W', 'R', 'Q', 'P']]
    assert(isComplete(board) == True)

    board = [['I', 'J', 'K', 'L', 'A'],
            ['H', 'G', 'F', 'B', 'M'],
            ['T', 'Y', 0, 'E', 'N'],
            ['U', 'S', 'X', 0, 'O'],
            ['V', 'W', 'R', 'Q', 'P']]
    assert(isComplete(board) == False)
    print('Passed!')

def testIsDiagLegal():
    print('Testing isDiagLegal()...', end='')
    board = [['I', 'J', 'K', 'L', 'A'],
            ['H', 'A', 'F', 'B', 'M'],
            ['T', 'Y', 'C', 'E', 'N'],
            ['U', 'S', 'X', 'D', 'O'],
            ['V', 'W', 'R', 'Q', 'P']]
    constraints = {
            "rows" :    { 0 : ["I", "L"],
                          1 : ["M", "F"],
                          2 : ["Y", "N"],
                          3 : ["D", "U"],
                          4 : ["Q", "R"] },
            "cols" :    { 0 : ["H", "T"],
                          1 : ["J", "W"],
                          2 : ["X", "K"],
                          3 : ["B", "E"],
                          4 : ["O", "P"] },
            "diags" :   { "left"  : ["C", "G"],
                          "right" : ["V", "S"] } }
    assert(isDiagLegal(board,2,2,constraints) == True)
    assert(isDiagLegal(board,1,1,constraints) == False)
    assert(isDiagLegal(board,4,0,constraints) == True)
    print('Passed!')

def testIsLegal():
    print('Testing isLegal()...', end='')
    board = [['I', 'J', 'K', 'L', 'A'],
            ['H', 'G', 'F', 'B', 'M'],
            ['T', 'Y', 'P', 'E', 'N'],
            ['U', 'S', 'X', 'D', 'O'],
            ['V', 'W', 'R', 'Q', 'P']]
    constraints = {
            "rows" :    { 0 : ["I", "L"],
                          1 : ["M", "F"],
                          2 : ["Y", "N"],
                          3 : ["D", "U"],
                          4 : ["Q", "R"] },
            "cols" :    { 0 : ["H", "T"],
                          1 : ["J", "W"],
                          2 : ["X", "K"],
                          3 : ["B", "E"],
                          4 : ["O", "P"] },
            "diags" :   { "left"  : ["C", "G"],
                          "right" : ["V", "S"] } }
    assert(isLegal(board,2,1,constraints) == True)
    assert(isLegal(board,1,3,constraints) == True)
    assert(isLegal(board,2,2,constraints) == False)
    print('Passed!')

def testAbcHelper():
    print('Testing abcHelper()...', end='')
    board = [[0, 0, 0, 0, 'A'],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    letters = 'BCDEFGHIJKLMNOPQRSTUVWXY'
    constraints = {
            "rows" :    { 0 : ["I", "L"],
                          1 : ["M", "F"],
                          2 : ["Y", "N"],
                          3 : ["D", "U"],
                          4 : ["Q", "R"] },
            "cols" :    { 0 : ["H", "T"],
                          1 : ["J", "W"],
                          2 : ["X", "K"],
                          3 : ["B", "E"],
                          4 : ["O", "P"] },
            "diags" :   { "left"  : ["C", "G"],
                          "right" : ["V", "S"] } }
    aLocation = (0,4)
    solution = [ ['I', 'J', 'K', 'L', 'A'],
                 ['H', 'G', 'F', 'B', 'M'],
                 ['T', 'Y', 'C', 'E', 'N'],
                 ['U', 'S', 'X', 'D', 'O'],
                 ['V', 'W', 'R', 'Q', 'P'] ]
    assert(abcHelper(board,letters,constraints,aLocation) == solution)

    board = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 'A'],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    letters = 'BCDEFGHIJKLMNOPQRSTUVWXY'
    constraints = {
            "rows" :    { 0 : ["V", "O"],
                          1 : ["R", "Q"],
                          2 : ["L", "C"],
                          3 : ["K", "H"],
                          4 : ["G", "I"] },
            "cols" :    { 0 : ["X", "W"],
                          1 : ["Y", "U"],
                          2 : ["N", "S"],
                          3 : ["F", "D"],
                          4 : ["E", "B"] },
            "diags" :   { "left"  : ["T", "M"],
                          "right" : ["J", "P"] } }
    aLocation = (2,4)
    solution = [['V', 'U', 'S', 'O', 'P'],
                 ['W', 'T', 'N', 'R', 'Q'],
                 ['X', 'L', 'M', 'C', 'A'],
                 ['K', 'Y', 'H', 'D', 'B'],
                 ['J', 'I', 'G', 'F', 'E']]
    assert(abcHelper(board,letters,constraints,aLocation) == solution)

    board = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 'A'],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    letters = 'BCDEFGHIJKLMNOPQRSTUVWXY'
    constraints = {
            "rows" :    { 0 : ["I", "L"],
                          1 : ["M", "F"],
                          2 : ["Y", "N"],
                          3 : ["D", "U"],
                          4 : ["Q", "R"] },
            "cols" :    { 0 : ["H", "T"],
                          1 : ["J", "W"],
                          2 : ["B", "K"],
                          3 : ["X", "E"],
                          4 : ["O", "P"] },
            "diags" :   { "left"  : ["C", "G"],
                          "right" : ["V", "S"] } }
    aLocation = (1,4)
    assert(abcHelper(board,letters,constraints,aLocation) == None)
    print('Passed!')

def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = {
            "rows" :    { 0 : ["I", "L"],
                          1 : ["M", "F"],
                          2 : ["Y", "N"],
                          3 : ["D", "U"],
                          4 : ["Q", "R"] },
            "cols" :    { 0 : ["H", "T"],
                          1 : ["J", "W"],
                          2 : ["X", "K"],
                          3 : ["B", "E"],
                          4 : ["O", "P"] },
            "diags" :   { "left"  : ["C", "G"],
                          "right" : ["V", "S"] } }
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [ ['I', 'J', 'K', 'L', 'A'],
                 ['H', 'G', 'F', 'B', 'M'],
                 ['T', 'Y', 'C', 'E', 'N'],
                 ['U', 'S', 'X', 'D', 'O'],
                 ['V', 'W', 'R', 'Q', 'P'] ]
    assert(board == solution)
    constraints =   {
            "rows" :    { 0 : ["I", "L"],
                          1 : ["M", "F"],
                          2 : ["Y", "N"],
                          3 : ["D", "U"],
                          4 : ["Q", "R"] },
            "cols" :    { 0 : ["H", "T"],
                          1 : ["J", "W"],
                          2 : ["B", "K"],
                          3 : ["X", "E"],
                          4 : ["O", "P"] },
            "diags" :   { "left"  : ["C", "G"],
                          "right" : ["V", "S"] } }
    aLocation = (1,4)
    assert(solveABC(constraints,aLocation) == None)
    constraints =   {
            "rows" :    { 0 : ["V", "O"],
                          1 : ["R", "Q"],
                          2 : ["L", "C"],
                          3 : ["K", "H"],
                          4 : ["G", "I"] },
            "cols" :    { 0 : ["X", "W"],
                          1 : ["Y", "U"],
                          2 : ["N", "S"],
                          3 : ["F", "D"],
                          4 : ["E", "B"] },
            "diags" :   { "left"  : ["T", "M"],
                          "right" : ["J", "P"] } }
    aLocation = (2,4)
    board = solveABC(constraints, aLocation)
    solution = [ ['V', 'U', 'S', 'O', 'P'],
                 ['W', 'T', 'N', 'R', 'Q'],
                 ['X', 'L', 'M', 'C', 'A'],
                 ['K', 'Y', 'H', 'D', 'B'],
                 ['J', 'I', 'G', 'F', 'E'] ]
    assert(board == solution)
    print('Passed!')

def testDist():
    print('Testing dist()...', end='')
    assert(dist(1,2,3,4) == 2.8284271247461903)
    assert(dist(5,10,2,30) == 20.223748416156685)
    assert(dist(1,2,1,2) == 0.0)
    print('Passed!')

def testAll():
    testFriendsOfFriends()
    testIsComplete()
    testIsDiagLegal()
    testIsLegal()
    testAbcHelper()
    testSolveABC()
    testDist()

def main():
    testAll()

if __name__ == '__main__':
    main()