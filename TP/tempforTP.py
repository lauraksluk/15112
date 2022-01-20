from tkinter import *
#from PIL import ImageTk, Image

def init(data):
    data.image = loadImage()

def mousePressed(event,data):
    pass

def keyPressed(event,data):
    pass

def timerFired(data):
    pass


def loadImage():
    img = PhotoImage(file='tilesSmall/tong8.gif')
    return img


def redrawAll(canvas,data):
    smallW,smallH = 15,25
    canvas.create_rectangle(180,200,420,300,fill='black')
    canvas.create_text(300,225,text="CP3 WON!",font = "BrushScriptMT 20", fill = "white")
    for i in range(14):
        img = data.image
        x0 = 195 + smallW*i
        y0 = 265
        x1 = x0 + smallW
        y1 = y0 + smallH
        xw3,yw3 = (x0+x1)//2,(y0+y1)//2
        canvas.create_image(xw3,yw3,image=data.image)



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

run(600,500)
#################################
'''

       1 tiles = ['w1','w2','w3','w4','w5','w6','w7','w8','w9','t1','t2','t3', \
        't4','t5','t6','t7','t8','t9','b1','b2','b3','b4','b5','b6','b7','b8', \
        'b9','east','south','west','north','red','green','blank']
        for j in tiles:
            if j == tile:

    2 def displayTile(canvas,s,x,y):
    tiles = ['w1','w2','w3','w4','w5','w6','w7','w8','w9','t1','t2','t3', \
    # 't4','t5','t6','t7','t8','t9','b1','b2','b3','b4','b5','b6','b7','b8', \
    # 'b9','east','south','west','north','red','green','blank']
    #for s in tiles:
    file = s + '.png'
    img = Image.open(file)
    #img = img.resize((35,50),Image.ANTIALIAS)
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(x,y,image=canvas.image)
        # label = Label(image=photo)
        # label.image = photo
        # label.pack()

def drawPlayer(canvas,data):
    result = []
    tileWidth = 35
    tileHeight = 50
    for i in range(len(data.player)):
        x0 = 60 + tileWidth*i
        y0 = 425
        x1 = x0 + tileWidth
        y1 = y0 + tileHeight
        canvas.create_rectangle(x0,y0,x1,y1,outline='white',fill='lime green')
        tile = data.player[i]
        print(tile)
        img = Image.open(tile +'.png')
        canvas.image = ImageTk.PhotoImage(img)
        result.append(canvas.image)

def getTiles(num):
    tiles = ['w1','w2','w3','w4','w5','w6','w7','w8','w9','t1','t2','t3', \
    't4','t5','t6','t7','t8','t9','b1','b2','b3','b4','b5','b6','b7','b8', \
    'b9','east','south','west','north','red','green','blank']
    result = []
    for i in range(num):
        card = random.choice(tiles)
        result.append(card)
        tiles.remove(card)
    return result


def drawHand(canvas,data,L1,L2,x,y):
    L1 = data.tiles
    canvas.image1 = ImageTk.PhotoImage(L[0])
    canvas.create_image(x,y,image=canvas.image1)

    canvas.image2 = ImageTk.PhotoImage(L[1])
    canvas.create_image(x+35,y,image=canvas.image2)

    canvas.image3 = ImageTk.PhotoImage(L[2])
    canvas.create_image(x+2*35,y,image=canvas.image3)

def drawHand(data):
    data.tilePics = {'w1': PhotoImage(file='w1.gif'),'w2': PhotoImage(file='w2.gif'),'w3': PhotoImage(file='w3.gif'),'w3': Ph}

def openTile():
    result = []
    tiles = ['w1','w2','w3','w4','w5','w6','w7','w8','w9','t1','t2','t3', \
    't4','t5','t6','t7','t8','t9','b1','b2','b3','b4','b5','b6','b7','b8', \
    'b9','east','south','west','north','red','green','blank']
    for s in tiles:
        file = s + '.png'
        img = Image.open(file)
        result.append([file,img])
    return result


def isPong(L,givenTile):
    wanGroup = groupSets(L)[0]
    tongGroup = groupSets(L)[1]
    bambooGroup = groupSets(L)[2]
    wordGroup = groupSets(L)[3]
    if 'wan' in givenTile:
        if wanGroup.count(givenTile) == 2:
            return True
    elif 'tong' in givenTile:
        if tongGroup.count(givenTile) == 2:
            return True
    elif 'bam' in givenTile:
        if bambooGroup.count(givenTile) == 2:
            return True
    else:
        if wordGroup.count(givenTile) == 2:
            return True

    canvas.image4 = ImageTk.PhotoImage(L[3])
    canvas.create_image(x+3*35,y,image=canvas.image4)

    canvas.image5 = ImageTk.PhotoImage(L[4])
    canvas.create_image(x+4*35,y,image=canvas.image5)

    canvas.image6 = ImageTk.PhotoImage(L[5])
    canvas.create_image(x+5*35,y,image=canvas.image6)

    canvas.image7 = ImageTk.PhotoImage(L[6])
    canvas.create_image(x+6*35,y,image=canvas.image7)


def isPong(L,givenTile):
    wanTiles, bambTiles, tongTiles, wordTiles = [],[],[],[]
    for tile in L:
        if 'wan' in tile:
            wanTiles.append(tile)
        elif 'bam' in tile:
            bambTiles.append(tile)
        elif 'tong' in tile:
            tongTiles.append(tile)
        else:
            wordTiles.append(tile)
    if givenTile != None:
        if len(wanTiles) > 2:
            seenWan = set()
            for wan in wanTiles:
                if wan not in seenWan:
                    seenWan.add(wan)
                for i in seenWan:
                    if wanTiles.count(i) == 2:
                        if 'wan' in givenTile:
                            if givenTile == i:
                                return True
        if len(bambTiles) > 2:
            seenBamb = set()
            for bamb in bambTiles:
                if bamb not in seenBamb:
                    seenBamb.add(bamb)
                for i in seenBamb:
                    if bambTiles.count(i) == 2:
                        if 'bam' in givenTile:
                            if givenTile == i:
                                return True
        if len(tongTiles) > 2:
            seenTong = set()
            for tong in tongTiles:
                if tong not in seenTong:
                    seenTong.add(tong)
                for i in seeTong:
                    if tongTiles.count(i) == 2:
                        if 'tong' in givenTile:
                            if givenTile == i:
                                if tongTiles.count(i) == 2:
                                    return True
        if len(wordTiles) > 2:
            seenWord = set()
            for word in wordTiles:
                if word not in seeWord:
                    seenWord.add(word)
                for i in seenWord:
                    if wordTiles.count(i) == 2:
                        if givenTile == i:
                            return True
    return False


    ###CHI

        else:
            wanValues.append(valuesWan[givenTile])

        else:
            tongValues.append(valuesTong[givenTile])

def isChi(L,givenTile):
    valuesWan = {'wan1':1,'wan2':2,'wan3':3,'wan4':4,'wan5':5,'wan6':6,\
    'wan7':7,'wan8':8,'wan9':9}
    valuesTong = {'tong1':1,'tong2':2,'tong3':3,'tong4':4,'tong5':5,\
    'tong6':6,'tong7':7,'tong8':8,'tong9':9}
    valuesBamboo ={'bam1':1,'bam2':2,'bam3':3,'bam4':4,'bam5':5,'bam6':6, \
    'bam7':7,'bam8':8,'bam9':9}
    wanGroup,tongGroup,bambooGroup,wordGroup = groupSets(L)
    wanValues, tongValues, bambooValues = [],[],[]
    if 'wan' in givenTile:
        for wan in wanGroup:
            wanValues.append(valuesWan[wan])
        if hasConsecutive(wanValues) == False:
            wanValues.append(valuesWan[givenTile])
            if hasConsecutive(wanValues):
                return True
        if hasAlmostConsecutive(wanValues):
            print(valuesWan[givenTile])
            if completedAlmostConsecutive(wanValues,valuesWan[givenTile]):
                return True
    elif 'tong' in givenTile:
        for tong in tongGroup:
            tongValues.append(valuesTong[tong])
        if hasConsecutive(tongValues) == False:
            tongValues.append(valuesTong[givenTile])
            if hasConsecutive(tongValues):
                return True
        if hasAlmostConsecutive(tongValues):
            if completedAlmostConsecutive(tongValues,valuesTong[givenTile]):
                return True
    elif 'bam' in givenTile:
        for bamboo in bambooGroup:
            bambooValues.append(valuesBamboo[bamboo])
        if hasConsecutive(bambooValues) == False:
            bambooValues.append(valuesBamboo[givenTile])
            if hasConsecutive(bambooValues):
                return True
        if hasAlmostConsecutive(bambooValues):
            if completedAlmostConsecutive(bambooValues,valuesBamboo[givenTile]):
                return True
    else:
        return False

def isChi(L,givenTile):
    valuesWan = {'wan1':1,'wan2':2,'wan3':3,'wan4':4,'wan5':5,'wan6':6,\
    'wan7':7,'wan8':8,'wan9':9}
    valuesTong = {'tong1':1,'tong2':2,'tong3':3,'tong4':4,'tong5':5,\
    'tong6':6,'tong7':7,'tong8':8,'tong9':9}
    valuesBamboo ={'bam1':1,'bam2':2,'bam3':3,'bam4':4,'bam5':5,'bam6':6, \
    'bam7':7,'bam8':8,'bam9':9}
    wanGroup,tongGroup,bambooGroup,wordGroup = groupSets(L)
    wanValues, tongValues, bambooValues = [],[],[]
    if 'wan' in givenTile:
        for wan in wanGroup:
            wanValues.append(valuesWan[wan])
        if hasConsecutive(wanValues) == False:
            wanValues.append(valuesWan[givenTile])
            if hasConsecutive(wanValues):
                return True

    elif 'tong' in givenTile:
        for tong in tongGroup:
            tongValues.append(valuesTong[tong])
        if hasConsecutive(tongValues) == False:
            tongValues.append(valuesTong[givenTile])
            if hasConsecutive(tongValues):
                return True

    elif 'bam' in givenTile:
        for bamboo in bambooGroup:
            bambooValues.append(valuesBamboo[bamboo])
        if hasConsecutive(bambooValues) == False:
            bambooValues.append(valuesBamboo[givenTile])
            if hasConsecutive(bambooValues):
                return True

    else:
        return False

def hasConsecutive(L):
    L.sort()
    if len(L) > 2:
        for i in range(len(L)-2):
            if L[i] + 1 == L[i+1] and L[i+1] + 1 == L[i+2]:
                return True
    return False

def getKey(d,value):
    for key in d:
        if d[key] == value:
            return key

def hasAlmostConsecutive(L):
    L.sort()
    if len(L) > 2:
        for i in range(len(L)-2):
            #print(L[i],L[i+1])
            if L[i] + 2 == L[i+1]:
                return True
            elif L[i] + 1 == L[i+1] and L[i+2] != L[i] + 2:
                return True
        return False
    else:
        return False

def completedAlmostConsecutive(L,tile):
    L.sort()
    if hasAlmostConsecutive(L):
        for i in range(len(L)-2):
            if L[i] + 2 == L[i+1]:
                if L[i] + tile == L[i+1]:
                    return True
            elif L[i] + 1 == L[i+1] and L[i+2] != L[i] + 2:
                if L[i+1] + 1 == tile or L[i] - 1 == tile:
                    return True
        return False
    else:
        return False

def f(L):
    for c in L:
        print (c)
tiles = ['wan1','wan2','wan3','wan4','wan5','wan6','wan7','wan8','wan9',\
'wan1']
f(tiles)


done = ['bam6', 'bam7', 'bam8']
copyL = ['wan5', 'wan8', 'wan9', 'bam1', 'bam1', 'bam1','bam1', 'north', 'red', 'west']
print(markPongSets(done,copyL))




def multiplePongs(data):
    if isCp1Pong == True and isCp2Pong == True:
        return not(isCp1Pong)
    elif isCp2Pong == True and isCp3Pong == True:
        return not (isCp2Pong)
    elif isCp1Pong == True and isCp3Pong == True:
        return not (isCp3Pong)
    elif isCp1Pong == True and isCp2Pong == True and isCp3Pong == True:
        return not(isCp1Pong) and not(isCp2Pong)

def hasPongSet(L):
    for c in L:
        if L.count(c) == 3:
            return True

def pongSetCount(L):
    pongSets = set()
    L.sort()
    for c in L:
        if L.count(c) >= 3:
            pongSets.add(c)
    if len(pongSets) != 0:
        for elem in pongSets:
            L.remove(elem)
            L.remove(elem)
            L.remove(elem)
    return len(pongSets),L

def chiSetCount(L):
    count = 0
    wanCards,tongCards,bamCards,wordCards = [],[],[],[]
    for c in L:
        if c != None:
            if 'wan' in c:
                wanCards.append(c)
            elif 'tong' in c:
                tongCards.append(c)
            elif 'bam' in c:
                bamCards.append(c)
            else:
                wordCards.append(c)
    wanCards.sort()
    for card1 in wanCards:
        consec1 = 'wan' + str(int(card1[-1]) + 1)
        consec2 = 'wan' + str(int(consec1[-1]) + 1)
        if consec1 in wanCards and consec2 in wanCards:
            count += 1
            wanCards.remove(card1)
            wanCards.remove(consec1)
            wanCards.remove(consec2)
    tongCards.sort()
    for card2 in tongCards:
        consec3 = 'tong' + str(int(card2[-1]) + 1)
        consec4 = 'tong' + str(int(consec3[-1]) + 1)
        if consec3 in tongCards and consec4 in tongCards:
            count += 1
            tongCards.remove(card2)
            tongCards.remove(consec3)
            tongCards.remove(consec4)
    bamCards.sort()
    for card3 in bamCards:
        consec5 = 'bam' + str(int(card3[-1]) + 1)
        consec6 = 'bam' + str(int(consec5[-1]) + 1)
        if consec5 in bamCards and consec6 in bamCards:
            count += 1
            bamCards.remove(card3)
            bamCards.remove(consec5)
            bamCards.remove(consec6)
    leftover = wanCards + tongCards + bamCards + wordCards
    return count,leftover

def isWin(L,tile):
    if len(L) == 13:
        done = []
        testL = copy.deepcopy(L)
        testL.append(tile)
        test2 = copy.deepcopy(testL)
        test2.append(tile)
        pairs = pairCount(testL)
        for p in pairs:
            testL.remove(p)
            testL.remove(p)
            done += [p,p]
            done,testL = markChiSets(testL,done)
            done,testL = markPongSets(done,testL)
            if testL != []:
                done = [p,p]
                testL = copy.deepcopy(L)
                testL.append(tile)
                testL.remove(p)
                testL.remove(p)
                done,testL = markPongSets(done,testL)
                done,testL = markChiSets(testL,done)
                if testL == []:

                    return True
                else:
                    testL = copy.deepcopy(L)
                    testL.append(tile)
                    done = []
            else:
                return True
        return False
    else:
        return False


def isWin(L,tile):

    if len(L) == 13:
        testL = copy.deepcopy(L)
        testL.append(tile)
        test2 = copy.deepcopy(testL)
        test2.append(tile)
        pairs = pairCount(testL)
        for p in pairs:
            testL.remove(p)
            testL.remove(p)
            countC1,testL = chiSetCount(testL)
            countP1,testL = pongSetCount(testL)
            if testL != []:
                testL = copy.deepcopy(L)
                testL.append(tile)
                testL.remove(p)
                testL.remove(p)
                countP2,testL = pongSetCount(testL)
                countC2,testL = chiSetCount(testL)
                if testL == []:
                    if countP2 + countC2 == 4:
                        return True
                else:
                    testL = copy.deepcopy(L)
                    testL.append(tile)
            else:
                if countC1 + countP1 == 4:
                    return True
        return False
    else:
        return False

#################################################################################

    def checkWin(self, player):
        symbolList = []
        for tile in player:
            symbolList.append(tile.symbol)
        sortedList = self.sortTiles(symbolList)
        currentHand = []
        for tile in sortedList:
            index = self.tileList.index(tile)
            currentHand.append(self.tileList2[index])
        return self.checkWinHelper(currentHand)

    def checkWinHelper(self, currentHand, depth=0):
        if len(currentHand) == 2:
            return currentHand[0] == currentHand[1]
        else:
            for i in range(len(currentHand)):
                tile1 = currentHand[i]
                if (tile1[0] + 1, tile1[1]) in currentHand and (tile1[0] + 2, tile1[1]) in currentHand:
                    tile2Index = currentHand.index((tile1[0] + 1, tile1[1]))
                    tile3Index = currentHand.index((tile1[0] + 2, tile1[1]))
                    currentHand.pop(i)
                    currentHand.pop(tile2Index - 1)
                    currentHand.pop(tile3Index - 2)
                    solution = self.checkWinHelper(currentHand)
                    if solution:
                        return solution
                    currentHand.insert(i, tile1)
                    currentHand.insert(tile2Index, (tile1[0] + 1, tile1[1]))
                    currentHand.insert(tile3Index, (tile1[0] + 2, tile1[1]))
                elif i <= (len(currentHand) - 3) and tile1 == currentHand[i + 1] and tile1 == currentHand[i + 2]:
                    currentHand.pop(i)
                    currentHand.pop(i)
                    currentHand.pop(i)
                    solution = self.checkWinHelper(currentHand)
                    if solution:
                        return solution
                    currentHand.insert(i, tile1)
                    currentHand.insert(i + 1, tile1)
                    currentHand.insert(i + 2, tile1)
            return False


'''

