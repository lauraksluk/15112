#################################################
# 15-112-m19 hw4
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

#returns the list a where each element is shifted to the right once
def rotateList(a):
    result = []
    if len(a) == 0:
        return result
    else:
        result += [a[len(a)-1]] + a[:len(a)-1]
        return result

#################################################
# hw4 problems
#################################################

#returns a list of tuples (count, character) of the number times the character occurs in list a
def lookAndSay(a):
    result = []
    prevNum = None
    if len(a) == 0: #edge case
        return result
    for c in a:
        currNum = c
        count = a.count(c)
        if prevNum == currNum: #removes duplicate tuples
            continue
        result.append((count, currNum))
        prevNum = currNum
    return result

#returns the list of a where each element is shifted to the right by n indices (nondestructive modification of a)
def nondestructiveRotateList(a, n):
    result = a
    if len (a) == 0: #edge case
        return []
    if n < 0: #converting negative rotations to positive
        n = len(a) - ((abs(n)) % (len(a)))
    else:
        n = n % (len(a))
    for i in range(n):
        result = rotateList(result) #repeating 1 rotation
    return result

#returns the list of a where each element is shifted to the right by n indices (destructive modification of a)
def destructiveRotateList(a, n):
    if len (a) == 0: #edge case
        a = []
    else:
        if n < 0: #converting negative rotations to positive
            n = len(a) - ((abs(n)) % (len(a)))
        else:
            n = n % (len(a))
        for i in range(n): #repeating rotations
            lastCharac = a.pop() #remove last character from a
            a.insert(0,lastCharac) #add in last character into beginning of a

#################################################
# hw4 problems
# Note:
#   There are less test cases than usual here.
#   You'll want to add your own!
#################################################
def testRotateList():
    print('Testing rotateList()...', end='')
    assert(rotateList([]) == [])
    assert(rotateList([1,2,3,4]) == [4,1,2,3])
    assert(rotateList([1]) == [1])
    assert(rotateList([2,1,1]) == [1,2,1])
    print('Passed!')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) == [(3,1)])
    assert(lookAndSay([1,2,2,3,3,3,4,4,4,4]) == [(1,1),(2,2),(3,3),(4,4)])
    assert(lookAndSay([-10,-10,5,5]) == [(2,-10),(2,5)])
    print("Passed!")

def _verifynondestructiveRotateListIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    nondestructiveRotateList(a,1) # ignore result, just checking for destructiveness here
    return (a == b)

def testNondestructiveRotateList():
    print("Testing nondestructiveRotateList()...", end="")
    _verifynondestructiveRotateListIsNondestructive()
    assert(nondestructiveRotateList([], -1) == [])
    assert(nondestructiveRotateList([1,2,3,4], 13) == [4,1,2,3])
    assert(nondestructiveRotateList([4,3,2,6,5], 2) == [6,5,4,3,2])
    assert(nondestructiveRotateList([1,2,3], 0) == [1,2,3])
    assert(nondestructiveRotateList([1, 2, 3], -1) == [2, 3, 1])
    assert(nondestructiveRotateList([1, 2, 3], -9) == [1, 2, 3])
    assert(nondestructiveRotateList([1, 2, 3], -7) == [2, 3, 1])
    print("Passed!")

def testDestructiveRotateList():
    print("Testing destructiveRotateList()...", end="")

    L = []
    r = destructiveRotateList(L,1)
    assert(r == None)
    assert(L == [])

    L = [1,2,3,4]
    r = destructiveRotateList(L,0)
    assert(r == None)
    assert(L == [1,2,3,4])

    L = [1,2,3,4]
    r = destructiveRotateList(L,1)
    assert(r == None)
    assert(L == [4,1,2,3])

    L = [1,2,3,4]
    r = destructiveRotateList(L,9)
    assert(r == None)
    assert(L == [4,1,2,3])

    L = [1,2,3,4]
    r = destructiveRotateList(L,-1)
    assert(r == None)
    assert(L == [2,3,4,1])

    L = [1,2,3,4]
    r = destructiveRotateList(L,-14)
    assert(r == None)
    assert(L == [3,4,1,2])


    print("Passed!")

#################################################
# hw4 Main
################################################

def testAll():
    testRotateList()
    testLookAndSay()
    testNondestructiveRotateList()
    testDestructiveRotateList()

def main():
    testAll()

if __name__ == '__main__':
    main()
