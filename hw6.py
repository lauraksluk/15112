#################################################
# 15-112-m19 hw6
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################

######################################################################
# Problems
######################################################################
import math

#returns Boolean value depending on if elements in board are valid
def inRange(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] not in range(1,N**2+1):
                return False
    return True

#returns location (row, col) of value 1 in board
def find1InBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                return (i,j)

#returns Boolean value depending on if given board is a legal Kings Tour
def isKingsTour(board):
    if inRange(board) == False: return False #values need to be in range
    N = len(board)
    (oldRow,oldCol) = find1InBoard(board)
    #8 possible directions to move to adjacent square
    moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(N**2-1):
        flag = False
        for j in range(len(moves)):
            #after moving to an adjacent square, break out of inner loop
            if flag == True: break
            newRow = oldRow + (moves[j][0])
            newCol = oldCol + (moves[j][1])
            if newRow in range(N) and newCol in range(N):
                if board[oldRow][oldCol] + 1 == board[newRow][newCol]:
                    oldRow = newRow
                    oldCol = newCol
                    flag = True
                else: flag = False
        #return false if cannot move to adjacent square by the 8 directions
        if flag == False: return flag
    return True

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################
from tkinter import *

#drawing outer Sudoku board
def drawBoard(canvas, board, margin, canvasSize):
    gridX1 = canvasSize - margin
    canvas.create_rectangle(margin,margin,gridX1,gridX1,width=5)

#drawing blocks on Sudoku board
def drawBlocks(canvas, board, margin, canvasSize):
    gridX1 = canvasSize - margin
    boardSide = canvasSize - 2*margin
    N = int(math.sqrt(len(board)))
    for i in range(1,N):
        horizX0 = margin
        horizY0 = margin + i*(boardSide//N)
        #drawing horizonal lines for blocks
        canvas.create_line(horizX0,horizY0,gridX1,horizY0,width=5)
        vertX0 = horizY0
        vertY0 = margin
        #drawing vertical lines for blocks
        canvas.create_line(vertX0,vertY0,vertX0,gridX1,width=5)

#drawing grid on Sudoku board
def drawGrid(canvas, board, margin, canvasSize):
    boardSide = canvasSize - 2*margin
    N = int(math.sqrt(len(board)))
    blockSide = boardSide//N
    for i in range(N):
        for j in range(1,N):
            horizX0 = margin
            horizY0 = margin + j*(blockSide//N) + i*blockSide
            horizX1 = horizX0 + boardSide
            #drawing horizontal grid lines
            canvas.create_line(horizX0,horizY0,horizX1,horizY0)
            vertY1 = horizX0 + boardSide
            #drawing vertical grid lines
            canvas.create_line(horizY0,horizX0,horizY0,vertY1)

#fill Sudoku grid with given 2d list of numbers
def fillGrid(canvas, board, margin, canvasSize):
    boardSide = canvasSize - 2*margin
    N = int(math.sqrt(len(board)))
    blockSide = boardSide//N
    cellSide = blockSide//N
    for i in range(len(board)):
        for j in range(len(board)):
            #finding center of each cell
            cellX = margin + (0.5*cellSide) + j*cellSide
            cellY = margin + (0.5*cellSide) + i*cellSide
            value = board[i][j]
            #filling each cell with number from 2dlist (board)
            canvas.create_text(cellX,cellY,text=value)

#draws Sudoku board with filled in values from given 2d list, board
def drawSudokuBoard(canvas, board, margin, canvasSize):
    if len(board) < 4: #will draw board with only at least 4 rows
        return None
    else:
        #calling helper functions to draw full Sudoku board
        drawBoard(canvas,board,margin,canvasSize)
        drawBlocks(canvas,board,margin,canvasSize)
        drawGrid(canvas,board,margin,canvasSize)
        fillGrid(canvas,board,margin,canvasSize)

#returns a list of (x,y) tuples for the outer points of star
def outerPoints(canvas, centerX, centerY, diameter, numPoints):
    outerR = diameter//2
    angle = math.radians(360/numPoints)
    #drawing outer circle to plot points
    canvas.create_oval(centerX-outerR, centerY-outerR,centerX+outerR,centerY
    +outerR,outline = 'white')
    lst = []
    for i in range(numPoints):
        pointX = centerX + math.sin(angle*i)*outerR
        pointY = centerY - math.cos(angle*i)*outerR
        lst.append((pointX,pointY))
    return lst

#returns a list of (x,y) tuples for the inner points of star
def innerPoints(canvas, centerX, centerY, diameter, numPoints):
    outerR = diameter//2
    angle = math.radians(360/numPoints)
    innerR = outerR*(3/8)
    #drawing inner circle to plot points
    canvas.create_oval(centerX-innerR,centerY-innerR,centerX+innerR,centerY
    +innerR,outline = 'white')
    lst = []
    for i in range(numPoints):
        #points don't start at 0 or 90 degrees (increment by 0.5*angle)
        pointX = centerX + math.sin(angle*(i+0.5))*innerR
        pointY = centerY - math.cos(angle*(i+0.5))*innerR
        lst.append((pointX, pointY))
    return lst

#draws star with given parameters
def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
    listPoints = []
    listOuter = outerPoints(canvas,centerX,centerY,diameter,numPoints)
    listInner = innerPoints(canvas,centerX,centerY,diameter,numPoints)
    #creates list of points of star; (x,y) tuples from outer and inner
    for i in range(numPoints):
        listPoints.append(listOuter[i])
        listPoints.append(listInner[i])
    for x,y in listPoints:
            canvas.create_polygon(listPoints, fill = color)

#################################################################
# hw6 tests
# Note: You must look at the output of these and confirm
# they work visually.
# Note: You must write your own test function for isKingsTour.
# You are not required to write tests for graphics functions.
#################################################################

def testInRange():
    print('Testing inRange()...', end='')
    assert(inRange([[3,2,1],[6,4,0],[5,7,8]]) == False)
    assert(inRange([[3,2,1],[6,4,10],[5,7,8]]) == False)
    assert(inRange([[3,2,1],[6,4,9],[5,7,8]]) == True)
    assert(inRange([[1,14,15,16],[13,2,7,6],[12,8,3,5],[11,10,9,4]]) == True)
    assert(inRange([[2,1],[0,4]]) == False)
    print('Passed!')

def testFind1InBoard():
    print('Testing find1InBoard()...', end='')
    assert(find1InBoard([[3,2,1],[6,4,9],[5,7,8]]) == (0,2))
    assert(find1InBoard([[1,14,15,16],[13,2,7,6],[12,8,3,5],[11,10,9,4]])
    == (0,0))
    assert(find1InBoard([[3,1],[2,4]]) == (0,1))
    assert(find1InBoard([[8,2,3],[7,4,1],[6,5,9]]) == (1,2))
    assert(find1InBoard([[10,2,3],[7,4,8],[6,5,1]]) == (2,2))
    print('Passed!')

def testIsKingsTour():
    print('Testing isKingsTour()...', end='')
    assert(isKingsTour([[3,2,1],[6,4,9],[5,7,8]]) == True)
    assert(isKingsTour([[1,2,3],[7,4,8],[6,5,9]]) == False)
    assert(isKingsTour([[3,2,1],[6,4,0],[5,7,8]]) == False)
    assert(isKingsTour([[1,14,15,16],[13,2,7,6],[12,8,3,5],[11,10,9,4]])
    == True)
    assert(isKingsTour([[3,1],[2,4]]) == True)
    print('Passed!')

def getBoard0():
    return [
      [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
      [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
      [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
      [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
      [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
      [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
      [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
      [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
    ]

def getBoard1():
    return [
        [1,2,3,4],
        [3,4,5,6],
        [7,8,9,10],
        [11,12,13,14]
    ]


def runSudoku(board, canvasSize=400):
    root = Tk()
    canvas = Canvas(root, width=canvasSize, height=canvasSize)
    canvas.pack()
    margin = 10
    drawSudokuBoard(canvas, board, margin, canvasSize)
    root.mainloop()

def testRunSudoku():
    print("Testing runSudoku()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    runSudoku(getBoard0(), 400)
    runSudoku(getBoard1(), 500)
    print("Done!")

def runDrawStar(centerX, centerY, diameter, numPoints, color,
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)

    root.mainloop()

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    runDrawStar(250, 250, 500, 5, "gold")
    runDrawStar(300, 400, 100, 4, "blue")
    runDrawStar(300, 200, 300, 9, "red")
    print("Done!")


def testAll():
    testInRange()
    testFind1InBoard()
    testIsKingsTour()
    testRunSudoku()
    testDrawStar()

def main():
    testAll()


if __name__ == '__main__':
    main()

