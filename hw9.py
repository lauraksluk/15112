#################################################
# 15-112-m19 hw9
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################

import math
import decimal

#################################################
# Helper functions
#################################################

#Takes in a list, L, start/stop indices, and v, a character
#Returns a list of tuples of values that binary search checks
def binarySearch(L,start,stop,v):
    mid = (start + stop)//2
    if start == stop: #base case 1
        return []
    elif L[mid] == v: #base case 2
        return [(mid,L[mid])]
    elif v < L[mid]:
        return [(mid,L[mid])] + binarySearch(L,start,mid,v)
    else:
        return [(mid,L[mid])] + binarySearch(L,mid+1,stop,v)

#Returns the tuple (row, column) of first empty square on given Sudoku board
def getEmptySquare(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

#Rounds decimal value based on regular math rounding rules
#from notes
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#Returns 2d list of empty 1d lists, with designated rows and columns
#from notes
def make2dList(rows, cols):
    a = []
    for row in range(rows): a += [[]*cols]
    return a

#Returns 1d list of the nth column in 2d list L
def getCol(L, n):
    result = []
    for i in range(len(L)):
        if len(L[i]) == 0: #edge cases
            return []
        elif n not in range(len(L[i])):
            return None
        else:
            #taking nth element in each row, for each row
            result += [L[i][n]]
    return result

#Returns Boolean value depending on if the elements in the list values are
#valid in a game of Sudoku
def areLegalValues(values):
    length = len(values)
    #length of list must be a postive perfect square
    if length <= 0:
        return False
    if (roundHalfUp(math.sqrt(length)))**2 != length:
        return False
    for c in values:
        #elements must be integers between 0-N^2 inclusive
        if type(c) != int:
            return False
        if c not in range(length + 1):
            return False
        #nonzero elements cannot repeat
        if c != 0:
            if values.count(c) > 1:
                return False
    return True

#Returns Boolean value depending on if given row in the board is
#valid in a game of Sudoku
def isLegalRow(board, row):
    lenB = len(board)
    if row not in range(lenB): #prevents out of bound crash
        return False
    givenRow = board[row]
    if len(givenRow) != lenB: #legal row if length equals N^2
        return False
    #check if elements in row are legal
    return areLegalValues(givenRow)

#Returns Boolean value depending on if given column in given board is
#valid in a game of Sudoku
def isLegalCol(board, col):
    for i in range(len(board)): #prevents out of bound crash
        if len(board[i]) != len(board):
            return False
    if col not in range(len(board)):
        return False
    givenCol = getCol(board,col)
    if len(givenCol) != len(board): #legal column if length equals N^2
        return False
    #check if elements in column are legal
    return areLegalValues(givenCol)

#Returns 1d list of the nth block in 2d list L
def getBlock(L,n):
    blocks = []
    result = make2dList(len(L), len(L)) #initialize 2d list
    N = int(math.sqrt(len(L)))
    for i in range(len(L)): #edge cases
        if len(L[i]) == 0:
            return []
        elif n not in range(len(L)):
            return None
    for rowB in range(0, len(L), N): #rows of blocks
        for colB in range(0, len(L), N): #columns of blocks
            for row in range(N): #rows in singular block
                for col in range(N): #columns in singular block
                    blocks += [L[row+rowB][col+colB]]
    for j in range(len(L)):
        #divide each block into 1d list inside 2d list
        result[j] = blocks[j*(len(L)):j*(len(L)) + len(L)]
    return result[n]

#Returns Boolean value depending on if given block in given board is
#valid in a game of Sudoku
def isLegalBlock(board, block):
    if block not in range(len(board)): #prevents out of bound crash
        return False
    givenBlock = getBlock(board, block)
    if len(givenBlock) != len(board):
        return False
    return areLegalValues(givenBlock) #check if elements in block are legal

#Returns Boolean value depending on if given Sudoku board is legal
def isLegalSudoku(board):
    for i in range(len(board)):
        if 0 in board[i]: return False #empty cells are not completed
        if isLegalRow(board,i) == False:
            return False
        if isLegalCol(board,i) == False:
            return False
        if isLegalBlock(board,i) == False:
            return False
    return True

######################################################################
# Problems
######################################################################

#Returns the alternating sum of list, lst
#Alternating- every other value is subtracted rather than added
def alternatingSum(lst):
    if len(lst) == 0: #base case
        return 0
    else:
        #factor of -1 to alternate sign
        return lst[0] + (-1)*alternatingSum(lst[1:])

#Returns a list of tuples of values that binary search checks
def binarySearchValues(L,v):
    if len(L) == 0: #edge case
        return []
    return binarySearch(L,0,len(L),v) #calls helper function

#Returns a new string
#New string contains all the letters between initial first and second letter
def generateLetterString(s):
    if len(s) != 2: #edge case
        return ''
    if s[0] == s[1]: #base case
        return s[0]
    if s[0] < s[1]:
        return s[0] + generateLetterString(chr(ord(s[0])+1) + s[1:])
    else:
        return s[0] + generateLetterString(chr(ord(s[0])-1) + s[1:])

#Returns a solved version of inputted partially completed board
def solveSudoku(board):
    N = int(math.sqrt(len(board)))
    if isLegalSudoku(board): #base case
        return board
    #get position of next empty cell
    newSquare = getEmptySquare(board)
    newRow, newCol = newSquare[0],newSquare[1]
    #get block number from position
    newBlock = N*(newRow//N) + (newCol//N)
    #list of possible input values
    values = list(range(1,N**2+1))
    for num in values:
        #try a number
        board[newRow][newCol] = num
        #check if tried value is legal
        if isLegalRow(board,newRow) and isLegalCol(board,newCol) \
                                    and isLegalBlock(board,newBlock):
            tempSol = solveSudoku(board)
            if tempSol != None:
                return tempSol
    #reset value if doesn't work
    board[newRow][newCol] = 0
    return None

#################################################
# hw9 test functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([]) == 0)
    assert(alternatingSum([1,1]) == 0)
    assert(alternatingSum([1,2,3,4,5]) == 3)
    assert(alternatingSum([1,-2,3,-4,5]) == 15)
    assert(alternatingSum([1,17,2,200]) == -214)
    print('Passed!')

def testBinarySearch():
    print('Testing binarySearch()...', end='')
    assert(binarySearch([],0,0,'c') == [])
    L = ['a','c','f','g','m','q']
    assert(binarySearch(L,0,6,'c') == [(3,'g'),(1,'c')])
    assert(binarySearch(L,0,6,'z') == [(3,'g'),(5,'q')])
    L = [1,3,10,15,200,370,500]
    assert(binarySearch(L,0,7,10) == [(3,15),(1,3),(2,10)])
    assert(binarySearch(L,0,7,0) == [(3,15),(1,3),(0,1)])
    print('Passed!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    assert(binarySearchValues([],'c') == [])
    L = ['a','c','f','g','m','q']
    assert(binarySearchValues(L,'c') == [(3,'g'),(1,'c')])
    assert(binarySearchValues(L,'z') == [(3,'g'),(5,'q')])
    L = [1,3,10,15,200,370,500]
    assert(binarySearchValues(L,10) == [(3,15),(1,3),(2,10)])
    assert(binarySearchValues(L,0) == [(3,15),(1,3),(0,1)])
    print('Passed!')

def testGenerateLetterString():
    print('Testing generateLetterString()...', end='')
    assert(generateLetterString('') == '')
    assert(generateLetterString('ajz') == '')
    assert(generateLetterString('ab') == 'ab')
    assert(generateLetterString('az') == 'abcdefghijklmnopqrstuvwxyz')
    assert(generateLetterString('ph') == 'ponmlkjih')
    print('Passed!')

def testGetEmptySquare():
    print('Testing getEmptySquare()...', end='')
    board = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 1, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 10, 8, 0, 0, 7, 9 ]
]
    assert(getEmptySquare(board) == (0,2))
    board = [
  [ 5, 3, 1, 2, 7, 8, 9, 4, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 1, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 1, 8, 0, 0, 7, 9 ]
]
    assert(getEmptySquare(board) == (0,8))
    board = [
  [ 5, 3, 1, 2, 7, 8, 9, 4, 6 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 1, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 1, 8, 0, 0, 7, 9 ]
]
    assert(getEmptySquare(board) == (1,1))
    print('Passed!')

def testAreLegalValues():
    print('Testing areLegalValues()...', end='')
    assert(areLegalValues([]) == False)
    assert(areLegalValues([5,3,0,0,7,0,0,0,0]) == True)
    assert(areLegalValues([5,3,10,0,7,0,0,-1,0]) == False)
    assert(areLegalValues([5,3,0,0,7,9,0,3,9.9]) == False)
    assert(areLegalValues([5,3,0,0,7,9,0,0]) == False)
    assert(areLegalValues([2,0,0,4]) == True)
    print('Passed!')

def testIsLegalRow():
    print('Testing isLegalRow()...', end='')
    assert(isLegalRow([[]], 9) == False)
    board = [
  [ 5, 3, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 11, 0, 0, 2, 0, 2, -1, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
  ]
    assert(isLegalRow(board, 3) == True)
    assert(isLegalRow(board, 9) == False)
    assert(isLegalRow(board, 0) == False)
    assert(isLegalRow(board, 5) == False)
    print('Passed!')

def testGetCol():
    print('Testing getCol()...', end='')
    assert(getCol([[]],0) == [])
    L = [
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ]
  ]
    assert(getCol(L,2) == [0,8,0,0])
    assert(getCol(L,8) == [0,0,3,1])
    assert(getCol(L,10) == None)
    print('Passed!')

def testIsLegalCol():
    print('Testing isLegalCol()...', end='')
    assert(isLegalCol([[]],0) == False)
    board = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 1, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 10, 8, 0, 0, 7, 9 ]
]
    assert(isLegalCol(board,0) == True)
    assert(isLegalCol(board,10) == False)
    assert(isLegalCol(board,3) == False)
    assert(isLegalCol(board,8) == True)
    print('Passed!')

def testGetBlock():
    print('Testing getBlock()...', end='')
    assert(getBlock([[]],0) == [])
    L = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]
    assert(getBlock(L,3) == [8,0,0,4,0,0,7,0,0])
    assert(getBlock(L,8) == [2,8,0,0,0,5,0,7,9])
    assert(getBlock(L,10) == None)
    print('Passed!')

def testIsLegalBlock():
    print('Testing isLegalBlock()...', end='')
    assert(isLegalBlock([[]],0) == False)
    board = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, -2 ],
  [ 0, 0, 0, 4, 1, 9, 9, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]
    assert(isLegalBlock(board,0) == True)
    assert(isLegalBlock(board,15) == False)
    assert(isLegalBlock(board,8) == False)
    assert(isLegalBlock(board,3) == True)
    print('Passed!')

def testIsLegalSudoku():
    print('Testing isLegalSudoku()...', end='')
    board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    assert(isLegalSudoku(board) == True)

    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    assert(isLegalSudoku(board) == False)

    board = [
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [1, 3, 2, 4],
    [4, 2, 3, 1]]
    assert(isLegalSudoku(board) == True)
    print('Passed!')

def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    assert(solveSudoku(board) == solution)

    board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]
    solution = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]]
    assert(solveSudoku(board) == solution)

    board = [
    [2, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 1, 0, 7, 9, 0, 9, 0],
    [1, 9, 0, 0, 8, 4, 5, 0, 0],
    [8, 2, 3, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 1, 0, 0, 3, 0, 2, 8],
    [0, 1, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 9, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]
    assert (solveSudoku(board) == None)

    board = [
    [0, 0, 0, 0],
    [0, 0, 4, 3],
    [1, 3, 0, 0],
    [0, 0, 0, 0]]
    solution = [
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [1, 3, 2, 4],
    [4, 2, 3, 1]]
    assert(solveSudoku(board) == solution)
    print('Passed!')


def testAll():
    testAlternatingSum()
    testBinarySearch()
    testBinarySearchValues()
    testGenerateLetterString()
    testGetEmptySquare()
    testAreLegalValues()
    testIsLegalRow()
    testGetCol()
    testIsLegalCol()
    testGetBlock()
    testIsLegalBlock()
    testIsLegalSudoku()
    testSolveSudoku()

def main():
    testAll()

if __name__ == '__main__':
    main()