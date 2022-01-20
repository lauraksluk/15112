#################################################
# 15-112-m19 hw5
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################

import math
import string
import copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#returns 1d list of the nth column in 2d list L
def getCol(L, n):
    result = []
    for i in range(len(L)):
        if len(L[i]) == 0: #edge cases
            return []
        elif n not in range(len(L[i])):
            return None
        else:
            result += [L[i][n]] #taking nth element in each row, for each row
    return result

#returns 2d list of empty 1d lists, with designated rows and columns (from notes)
def make2dList(rows, cols):
    a = []
    for row in range(rows): a += [[]*cols]
    return a

#returns 1d list of the nth block in 2d list L
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
        result[j] = blocks[j*(len(L)):j*(len(L)) + len(L)] #divide each block into 1d list inside 2d list
    return result[n]

#################################################
# hw4 problems
#################################################

#returns Boolean value depending on if the elements in the list values are valid in a game of Sudoku
def areLegalValues(values):
    length = len(values)
    if length <= 0: #length of list must be a postive perfect square
        return False
    if (roundHalfUp(math.sqrt(length)))**2 != length:
        return False
    for c in values: #elements must be integers between 0-N^2 inclusive
        if type(c) != int:
            return False
        if c not in range(length + 1):
            return False
        if c != 0: #nonzero elements cannot repeat
            if values.count(c) > 1:
                return False
    return True

#returns Boolean value depending on if given row in the board is valid in a game of Sudoku
def isLegalRow(board, row):
    lenB = len(board)
    if row not in range(lenB): #prevents out of bound crash
        return False
    givenRow = board[row]
    if len(givenRow) != lenB: #legal row if length equals N^2
        return False
    return areLegalValues(givenRow) #check if elements in row are legal

#returns Boolean value depending on if given column in given board is valid in a game of Sudoku
def isLegalCol(board, col):
    for i in range(len(board)): #prevents out of bound crash
        if len(board[i]) != len(board):
            return False
    if col not in range(len(board)):
        return False
    givenCol = getCol(board,col)
    if len(givenCol) != len(board): #legal column if length equals N^2
        return False
    return areLegalValues(givenCol) #check if elements in column are legal

#returns Boolean value depending on if given block in given board is valid in a game of Sudoku
def isLegalBlock(board, block):
    if block not in range(len(board)): #prevents out of bound crash
        return False
    givenBlock = getBlock(board, block)
    if len(givenBlock) != len(board):
        return False
    return areLegalValues(givenBlock) #check if elements in block are legal

#returns Boolean value depending on if given Sudoku board is legal
def isLegalSudoku(board):
    for i in range(len(board)):
        if isLegalRow(board,i) == False:
            return False
        if isLegalCol(board,i) == False:
            return False
        if isLegalBlock(board,i) == False:
            return False
    return True

#################################################
# hw5 test functions - write your own test functions down here!
#################################################

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
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, -4, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 10, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 5, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]
    assert(isLegalSudoku(board) == False)

    board = [
  [ 2, 3, 0, 0 ],
  [ 1, 0, 0, 4 ],
  [ 0, 1, 3, 0 ],
  [ 4, 0, 0, 0 ],
]
    assert(isLegalSudoku(board) == True)

    board = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 6, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 6, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]
    assert(isLegalSudoku(board) == False)

    board = [
  [ 0, 3, 0, 0, 7, 0, 0, 1, 0 ],
  [ 6, 0, 2, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 0, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 5, 8, 0, 3, 0, 9, 1 ],
  [ 7, 1, 0, 0, 2, 0, 0, 0, 6 ],
  [ 9, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 8, 4, 1, 9, 0, 0, 5 ],
  [ 1, 5, 0, 0, 8, 0, 0, 7, 9 ]
]
    assert(isLegalSudoku(board) == True)

    board =[
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
    assert(isLegalSudoku(board) == True)
    print('Passed!')


#################################################
# hw4 Main
################################################

def testAll():
    testAreLegalValues()
    testIsLegalRow()
    testGetCol()
    testIsLegalCol()
    testGetBlock()
    testIsLegalBlock()
    testIsLegalSudoku()

def main():
    testAll()

if __name__ == '__main__':
    main()
