#################################################
# 15-112-m19 hw1
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################

import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

#################################################
# hw1 problems
#################################################

def isEquilateralTriangle(side1,side2,side3):
    if almostEqual(side1, side2) == True and almostEqual(side1, side3) == True and almostEqual(side2, side3) == True:
        return True
    return False

def getKthDigit(n, k):
    if n >= 0:
        return (n//10**k) % 10
    else:
        return ((n/-1)//10**k) % 10

def isPerfectSquare(n):
    if type (n) == int:
        if n >= 0:
            if math.sqrt(n) == int(math.sqrt(n)):
                return True
            return False
        return False
    return False

#################################################
# hw1 Test Functions
################################################

def testIsEquilateralTriangle():
    print('Testing isEquilateralTriangle()... ', end='')
    assert(isEquilateralTriangle(1,2,3) == False)
    assert(isEquilateralTriangle(1,2.0,3) == False)
    assert(isEquilateralTriangle(1.00000000000000001,1.0,1) == True)
    assert(isEquilateralTriangle(.1 + .1 + .1,.3,.3) == True)
    assert(isEquilateralTriangle(11,11,11) == True)
    assert(isEquilateralTriangle(1,1,3) == False)
    assert(isEquilateralTriangle(1,3,3) == False)
    assert(isEquilateralTriangle(1,3,1) == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

#################################################
# hw1 Main
################################################

def testAll():
    testIsEquilateralTriangle()
    testGetKthDigit()
    testIsPerfectSquare()

def main():
    testAll()

if __name__ == '__main__':
    main()
