import random
import copy
import string
from tkinter import *

#################################################################
'''
def f(s1,s2,c):
    return s2[-(s1.find(c))]

def ct1(s1,s2):
    result = ''
    for c in s1:
        print ("%s : %s" % (c,f(s1,s2,c)))
        result = c + result
    return result
print(ct1('abcd','efgh'))

def ct2(n,m):
    for i in range(n,7):
        for j in range(m,-2,-1):
            i = abs(i)
            j = abs(j)
            if i %2 == 0:
                print('even',i)
            elif i >0 :
                print('foo',i)
            if j %2 == 1:
                print('odd',j)
            elif j >0:
                print('bar',j)
        print('amost done')
    print('done')
print(ct2(5,-1))

def ct3(L):
    a = L
    b = copy.copy(L)
    c=L[0:len(L)]
    d = copy.deepcopy(L)
    a[0] = 15
    b[0] = 26
    c[0] = 13
    b[1][0] = 18
    c[1][1] = 66
    d[0][0] = 7
    d[1].extend([9,4])
    a.insert(0,'hi')
    print('a-', a)
    print('b-', b)
    print('c-', c)
    print('d-', d)
m = [[2,0],[1,3]]
ct3(m)
print('m-',m)

def ct(s):
    if len(s) == 0:
        return ''
    index = string.ascii_lowercase.find(s[0])
    letter = string.ascii_uppercase[-index]
    return letter + ct(s[1:]) + ct(s[:-1])
print(ct('abf'))

#################################################################

def f(x):return x%1000
def g(x):return x//1000
def h(x,y):
    x,y=str(x),str(y)
    if x==y:
        return False
    return x==y[::-1]
def roc1(x):
    if not(type(x) == int):
        return False
    if len(str(x)) != 6:
        return False
    return h(f(x),g(x))
print(roc1(123321))

def roc(L):
    assert(len(L) == 3)
    count = 0
    for row in L:
        assert(len(row) == 3)
        for i in range(1,len(row)):
            if count%2 == 0:
                assert(sum(row) == 18)
                assert(row[i-1] < row[i])
            else:
                assert(sum(row) == 15)
                assert(row[i] < row[i-1])
        count += 1
    return True
print(roc([[2,6,10],[10,3,2],[2,6,10]]))

#################################################################

def isValidAndrewID(s):
    if len(s) < 3:
        return False
    for c in s:
        if s[:-1].islower() and s[:-1].isalpha() == False:
            return False
        if not(s[-1].isdigit() or s[-1].islower()):
            return False
    return True
print(isValidAndrewID('jsmith1'))
print(isValidAndrewID('jsmith'))
print(isValidAndrewID('Jsmith'))
print(isValidAndrewID('js'))
print(isValidAndrewID('j2smith'))

def hasOnlyOne(x,d):
    count = 0
    while x > 0:
        if x%10 == d:
            count += 1
        x //= 10
    if count != 1:
        return False
    else:
        return True
def is42ish(x):
    if hasOnlyOne(x,4) and hasOnlyOne(x,2):
        return True
    else:
        return False
def nth42ish(n):
    guess,count = 0,0
    while count <= n:
        guess += 1
        if is42ish(guess):
            count += 1
    return guess
print(nth42ish(0))
print(nth42ish(5))
print(nth42ish(9))

def init(data):
    data.rows = 10
    data.cols = 10
    data.cellW = data.width//data.cols
    data.cellH = data.height//data.rows
    data.ovalRow = 0
    data.ovalCol = 0
    data.win = False
def mousePressed(event,data):
    data.ovalRow = event.y//data.cellH
    data.ovalCol = event.x//data.cellW
    if data.ovalRow == 9 and data.ovalCol == 9:
        data.win = True

def keyPressed(event,data):
    if event.keysym == "Down":
        data.ovalRow += 1
        if data.ovalRow == 9 and data.ovalCol == 9:
            data.win = True
    if event.keysym == "Right":
        data.ovalCol += 1
        if data.ovalRow == 9 and data.ovalCol == 9:
            data.win = True
def drawOval(canvas,data):
    x0 = data.ovalCol*data.cellW
    y0 = data.ovalRow*data.cellH
    x1 = x0 + data.cellW
    y1 = y0 + data.cellH
    canvas.create_oval(x0,y0,x1,y1,fill='blue')


def redrawAll(canvas,data):
    if data.win == False:
        for i in range(data.rows):
            for j in range(data.cols):
                x0 = j*data.cellW
                y0 = i*data.cellH
                x1 = x0 + data.cellW
                y1 = y0 + data.cellH
                canvas.create_rectangle(x0,y0,x1,y1)
        drawOval(canvas,data)
    else:
        canvas.create_text(data.width//2,data.height//2,text='You won!')
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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)

def isComplete(L):
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == '':
                return False
    return True

def getNext(L):
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == '':
                return (i,j)

def fourColoring(grid):
    if isComplete(grid):
        return grid
    row = getNext(grid)[0]
    col = getNext(grid)[1]
    for color in ['R','G','Y','B']:
        grid[row][col] = color
        if isValid(grid,row,col):
            tmpSol = fourColoring(grid)
            if tmpSol != None:
                return tmpSol
    grid[row][col] = ''
    return None

def getDirections():
    return [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]

def isValid(grid,row,col):
    for moves in getDirections():
        newRow = row + moves[0]
        newCol = col + moves[1]
        if newRow in range(len(grid)) and newCol in range(len(grid[0])):
            if grid[newRow][newCol] != '':
                if grid[newRow][newCol] == grid[row][col]:
                    return False
    return True
L = [['','','',''],['','','',''],['','','',''],['','','','']]

print(fourColoring(L))

class Play(object):
    def __init__(self,title,numScenes):
        self.title = title
        self.numScenes = numScenes
        self.currScene = 1
    def __repr__(self):
        return 'Play<%s,%d>' % (self.title,self.numScenes)
    def getStatus(self):
        if self.currScene > self.numScenes:
            return 'Show is done'
        else:
            return 'On Scene %d' % (self.numScenes)
    def sceneChange(self):
        self.currScene += 1

    def __eq__(self,other):
        if (isinstance(other,Play) == False):
            return False
        else:
            return self.title == other.title and self.numScenes == other.numScenes

    def __hash__(self):
        return hash(self.title,self.numScenes)

class Musical(Play):
    def __init__(self,title,numScenes,songs):
        super().__init__(title,numScenes)
        self.songs = songs
        self.currScene = 1
    def getStatus(self):
        super().getStatus()
        if self.currScene in self.songs:
            return "On Scene %d, with music" % (self.currScene)
    def skipToSong(self):
        if self.currScene < self.songs[0]:
            self.currScene = self.songs[0]
        elif self.currScene == self.songs[-1]:
            self,currScene = self.songs[-1]
        else:
            for i in range(len(self.songs)):
                while self.songs[i] < self.currScene:
                    continue
                self.currScene = self.songs[i]

def getItemCounts(lst,d):
    if len(lst) == 0:
        return d
    if lst[0] not in d:
        d[lst[0]] = 1
    else:
        d[lst[0]] += 1
    return getItemCounts(lst[1:],d)


print(getItemCounts(['a','b','c','a','a','c'],{}))

def isComplete(bags,items):
    total = 0
    for i in range(len(bags)):
        total += sum(bags[i])
    return total == sum(items)

def packItems(items,bagSizes):
    bags = []
    for i in range(len(bagSizes)):
        bags.append([])
    return getBags(items,bagSizes,bags)

def getBags(items,bagSizes, bags):
    if isComplete(bags,items):
        return bags
    for i in range(len(bags)):
        for weight in items:
            bags[i].append(weight)
            items.remove(weight)
            if isValid(bagSizes,bags):
                tmpSol = getBags(items,bagSizes,bags)
                if tmpSol != None:
                    return tmpSol
            bags[i].pop()
            items.append(weight)
    return None

def isValid(bagSizes,bags):
    if len(bags) != len(bagSizes):
        return False
    for i in range(len(bagSizes)):
        if sum(bags[i]) > bagSizes[i]:
            return False
    return True

print(packItems([4,8,1,4,3],[12,9]))

def reduceToStrings(lst):
    return reduce(lst,[])

def reduce(lst,newLst):
    if len(lst) == 0:
        return newLst
    if isinstance(lst[0],str):
        newLst.append(lst[0])
    return reduce(lst[1:],newLst)

print(reduceToStrings([1,'ab',True,'car']))

def roc1(L):
    z = [0,0]
    n = rocHelp(L,z)
    return n == 12 and z[0] == 3 and z[1] == 6

def rocHelp(L,z):
    if L == []:
        z[0] += 1
        return 0
    if type(L[0]) == list:
        return rocHelp(L[0],z) + rocHelp(L[1:],z)
    if type(L[0]) == int:
        z[1] += 1
        return L[0] + rocHelp(L[1:],z)

L = [2,2,2,2,2,2,[],[],[]]
#print(roc1(L))

def undoSet(S):
    for elem in S:
        return elem

def mergeD(L):
    result = {}
    for dict in L:
        for key in dict:
            if key in result:
                result[key].add(dict[key])
            else:
                result[key] = set()
                result[key].add(dict[key])
    for letter in result:
        if len(result[letter]) == 1:
            result[letter] = undoSet(result[letter])
    return result

L = [{'a':1,'b':2},{'a':3,'c':4},{'e':5}]
print(mergeD(L))
#########################################################
class Circle(object):
    def __init__(self,cx,cy,r):
        self.cx = cx
        self.cy = cy
        self.r = 20
    def move(self,dx,dy):
        self.cx += dx
        self.cy += dy

    def onTimerFired(self,data):
        self.move(30,0)
        if self.cx > data.width:
            self.cx = 0

    def changeRad(self,dr):
        self.r += 10

    def getPosRad(self):
        return self.cx,self.cy,self.r

    def draw(self,canvas):
        x0, y0 = self.cx - self.r, self.cy - self.r
        x1, y1 = self.cx + self.r, self.cy + self.r
        canvas.create_oval(x0,y0,x1,y1,fill='black')

def init(data):
    data.circles = []

def dist(x0,y0,x1,y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5

def mousePressed(event, data):
    for circ in data.circles:
        cx,cy,r = circ.getPosRad()
        if dist(event.x,event.y,cx,cy) <= r:
            circ.changeRad(10)

def keyPressed(event, data):
    if event.keysym == 'Up':
        for circ in data.circles:
            circ.move(0,-30)
    if event.keysym == 'Down':
        for circ in data.circles:
            circ.move(0,30)

def getCirc(data):
    cx = random.randint(0,data.width)
    cy = random.randint(0,data.height)
    r = 20
    return Circle(cx,cy,r)


def timerFired(data):
    data.circles.append(getCirc(data))
    for circ in data.circles:
        circ.onTimerFired(data)

def redrawAll(canvas, data):
    for circ in data.circles:
        circ.draw(canvas)

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

def flatten(lst):
    result = []
    return flattenHelp(lst,result)

def flattenHelp(lst,result):
    if lst == []:
        return result
    if type(lst[0]) == list:
        flattenHelp(lst[0],result)
    if type(lst[0]) == str:
        result.append(lst[0])
    return flattenHelp(lst[1:],result)

L = ['a',['b'],['c',['d','e'],'f'],'g']
print(flatten(L))
L1 = ['wow',[2,[[]]],[True,'gosh']]
print(flatten(L1))

def powerSum(n,k):
    if n == 1:
        return 1
    return (n**k) + powerSum(n-1,k)
print(powerSum(4,2))*



def wordBreak(S,hashtag):
    result = ''

    return wordHelp(S,hashtag[1:],result)

def getLongest(S):
    longest = ''
    for elem in S:
        if len(elem) > len(longest):
            longest = elem
    return longest

def smallS(S,c):
    newS = set()
    for word in S:
        if word.startswith(c):
            newS.add(word)
    return newS


def wordHelp(S,hashtag,result):
    if isComplete(result):
        return result
    for c in hashtag:
        for word in smallS(S,c):
            result += c

class Box(object):
    def __init__(self,cx,cy,side,num):
        self.cx = cx
        self.cy = cy
        self.side = side
        self.num = num
        self.direc = -1

    def move(self):
        self.cy += self.direc*3

    def bounce(self):
        self.direc *= -1

    def onTimerNum(self):
        self.num -= 1
        if self.num < 0:
            self.num = 60

    def getPos(self):
        return self.cy

    def draw(self,canvas):
        x0 = self.cx - (self.side//2)
        y0 = self.cy - (self.side//2)
        x1 = self.cx + (self.side//2)
        y1 = self.cy + (self.side//2)
        canvas.create_rectangle(x0,y0,x1,y1,fill='pink')
        canvas.create_text(self.cx,self.cy,text=self.num)

def init(data):
    data.sq = Box(data.width//2,data.height//2,40,60)
    data.time = 0

def timerFired(data):
    data.time += 1
    if data.time % 10 == 0:
        data.sq.onTimerNum()
    data.sq.move()
    y = data.sq.getPos()
    if y-20 < 0 or y+20 > data.height:
        data.sq.bounce()

def mousePressed(event,data):
    pass
def keyPressed(event,data):
    pass

def redrawAll(canvas,data):
    data.sq.draw(canvas)

def distance(x0,y0,x1,y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5


class Planet(object):
    def __init__(self,cx,cy,r,color):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color

    def draw(self,canvas):
        x0 = self.cx-self.r
        y0 = self.cy-self.r
        x1 = self.cx+self.r
        y1 = self.cy+self.r
        canvas.create_oval(x0,y0,x1,y1,fill=self.color)

class Red(Planet):
    def __init__(self,cx,cy,r,color):
        super().__init__(cx,cy,r,color)
        self.color = 'red'

    def move(self,data,dy):
        self.cy += dy
        if self.cy - self.r < 0:
            self.cy = data.height - self.r
        if self.cy + self.r > data.height:
            self.cy = self.r

    def getPos(self):
        return self.cx, self.cy

    def makeMoon(self):
        cx = self.cx - self.r
        cy = self.cy - self.r
        r = 5
        return Moon(cx,cy,r,'white')

class Blue(Planet):
    def __init__(self,cx,cy,r,color,direction=1):
        super().__init__(cx,cy,r,color)
        self.color = 'blue'
        self.direction = direction

    def hitRedOrMoon(self,other):
        if isinstance(other,Red):
            if distance(self.cx,self.cy,other.cx,other.cy) <= self.r + other.r:
                return True
            else:
                return False
        if isinstance(other,Moon):
            if distance(self.cx,self.cy,other.cx,other.cy) <= self.r + other.r:
                return True
            else:
                return False

    def move(self,dx):
        self.cx += dx*self.direction

    def getPos(self):
        return self.cx,self.cy,self.r

    def changeDirection(self):
        self.direction *= -1

class Moon(object):
    def __init__(self,cx,cy,r,color):
        self.cx = cx
        self.cy = cy
        self.r = 5
        self.color = 'white'

    def orbit1(self):
        self.cx += 30
    def orbit2(self):
        self.cy += 30
    def orbit3(self):
        self.cx -= 30
    def orbit4(self):
        self.cy -= 30


    def draw(self,canvas):
        x0 = self.cx-self.r
        y0 = self.cy-self.r
        x1 = self.cx+self.r
        y1 = self.cy+self.r
        canvas.create_oval(x0,y0,x1,y1,fill=self.color)


def init(data):
    data.red = [Red(data.width//2,data.height//2,15,'red')]
    data.blue = []
    data.moon = []
    data.time = 0
    data.gameOver = False

def keyPressed(event,data):
    for redC in data.red:
        if event.keysym == 'Up':
            redC.move(data,-15)
        if event.keysym == 'Down':
            redC.move(data,15)

def mousePressed(event,data):
    for blueC in data.blue:
        cx,cy,r = blueC.getPos()
        if distance(event.x,event.y,cx,cy) <= r:
            blueC.changeDirection()

def getRed(data):
    cx = random.randint(0,data.width)
    cy = random.randint(0,data.height)
    r = 15
    return Red(cx,cy,r,'red')

def getBlue(data):
    cx = 0
    cy = random.randint(0,data.height)
    r = 10
    return Blue(cx,cy,r,'blue')


def timerFired(data):
    data.time += 1
    if data.time % 20 == 0:
        data.red.append(getRed(data))
        data.blue.append(getBlue(data))
    for redC in data.red:
        data.moon.append(redC.makeMoon())
        for moon in data.moon:
            moon.orbit1()
            moon.orbit2()
            moon.orbit3()
            moon.orbit4()
    for blueC in data.blue:
        blueC.move(10)
        for redC in data.red:
            if blueC.hitRedOrMoon(redC):
                data.gameOver = True
        for moon in data.moon:
            if blueC.hitRedOrMoon(moon):
                data.blue.remove(blueC)
                data.moon.remove(moon)

def redrawAll(canvas,data):
    if data.gameOver == False:
        for redC in data.red:
            redC.draw(canvas)
        for blueC in data.blue:
            blueC.draw(canvas)
        for moon in data.moon:
            moon.draw(canvas)
    else:
        canvas.create_text(data.width//2,data.height//2,text='Game Over!')



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

def wordBreak(S,hashtag):
    result = []
    word = ''
    return ' '.join(wordHelp(S,hashtag[1:],result,word))

def wordHelp(S,hashtag,result,word):
    if hashtag == '':
        return result
    for i in range(len(hashtag)):
        word += hashtag[i]
        if word in S:
            tmpSol = wordHelp(S,hashtag[i+1:],result+[word],'')
            if tmpSol != None:
                return tmpSol
    return None


S = {'ice','cream','for','i','scream','forever'}
print(wordBreak(S,'#iscreamforicecream'))


# def packItems(items,bagSizes):
#     result = []
#     bag = []
#     return packHelp(items,bagSizes,bag,result)
#
#
# def packHelp(items,bagSizes,bag,result):
#     if bagSizes == [] and items == []:
#         return result
#     for i in range(len(items)):
#         bag.append(items[i])
#         newItems = copy.copy(items)
#         newItems.remove(items[i])
#         if sum(bag) <= bagSizes[0]:
#             tmpSol = packHelp(newItems,bagSizes[1:],[],result+[bag])
#             if tmpSol != None:
#                 return tmpSol
#     return None
#
# print(packItems([4,8,1,4,3],[12,9]))

def getResult(guestPref):
    temp = set()
    result = {}
    for key in guestPref:
        for tab in guestPref[key]:
            temp.add(tab)
    for elem in temp:
        result[elem] = ''
    return result

def getSeatingPlan(guestPref):
    result = getResult(guestPref)
    return getPlan(guestPref,result)

def isComplete(guestPref,result):
    for key in result:
        if result[key] == '':
            return False
    return True

def isValid(guestPref,result):
    for key in result:
        if key not in guestPref[result[key]]:
            return False
    for tab1 in result:
        for tab2 in result:
            if tab1 != tab2:
                if result[tab1] == result[tab2]:
                    return False
    return True


def getPlan(guestPref,result):
    if isComplete(guestPref,result):
        return result
    for group in guestPref:
        for table in guestPref[group]:
            result[table] = group
            if isValid(guestPref,result):
                tmpSol = getPlan(guestPref,result)
                if tmpSol != None:
                    return tmpSol
    result[table] = ''
    return None

guestPref ={'g1': ['t1','t3'],'g2': ['t3'],'g3':['t1','t2','t3']}
print(getSeatingPlan(guestPref))'''

def getDirections():
    return [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1)]

def isComplete(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return False
    return True


def isKingsTour(board):
    if isComplete(board):
        return board
    row = getEmptyCell(board)[0]
    col = getEmptyCell(board)[1]
    for moves in getDirections():
        newRow = row + moves[0]
        newCol = col + moves[1]
        if newRow in range(len(board)) and newCol in range(len(board)):
            board[newRow][newCol] = getEmptyNum(board) + 1
            if isValid(board,newRow,newCol):
                tmpSol = isKingsTour(board)
                if tmpSol != None:
                    return tmpSol
            board[newRow][newCol] = 0
    return None















































