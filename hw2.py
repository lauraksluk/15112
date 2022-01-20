#################################################
# 15-112-m19 hw2
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

def digitCount(n): #counts the number of digits in a given number
    counter = 0
    n = abs(n)
    if (n == 0):
        return 1
    while n > 0:
        counter += 1
        n = n//10
    return counter

def isPrime(n): #determines if n is prime or not
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n ** 0.5)
    for factor in range (3, maxFactor + 1, 2):
        if (n % factor == 0):
            return False
    return True

def isNotConsec (n): #determines if number does not have 2 consecutive digits
    s = str(n)
    for i in range (len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True

#################################################
# hw2 problems
#################################################


def rotateNumber(x):
    newD = (x % 10) * (10 ** (digitCount(x) - 1))
    newNum = newD + (x//10)
    return newNum

def isSteezyPrime(x):
    s = str(x)
    if len(s) == 1:
        if isPrime(x) == True:
            return True
        return False
    if isPrime(x) == True and isNotConsec(x) == True:
        for j in range (digitCount(x) - 1):
            x = rotateNumber(x)
            if isPrime(x) != True or isNotConsec(x) != True:
                    return False
        return True
    return False

def nthSteezyPrime(n):
    counter = 0
    guess = 0
    while counter <= n:
        guess += 1
        if isSteezyPrime (guess) == True:
            counter += 1
    return guess

def carrylessAdd(a, b):
    revN = ''
    if a == 0 and b == 0:
        return 0
    while a != 0 or b != 0:
        revN += str(((a % 10) + (b % 10)) % 10)
        a //= 10
        b //= 10
    return int(revN[::-1])

def vowelCount(s):
    counter = 0
    newS = s.lower()
    for i in range(len(newS)):
        if newS[i] == 'a' or newS[i] == 'e' or newS[i] == 'i' or newS[i] == 'o' or newS[i] == 'u':
            counter += 1
    return counter


#################################################
# hw2 Test Functions
################################################

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsSteezyPrime():
    print('Testing isSteezyPrime()... ', end='')
    assert(isSteezyPrime(2) == True)
    assert(isSteezyPrime(11) == False)
    assert(isSteezyPrime(13) == True)
    assert(isSteezyPrime(79) == True)
    assert(isSteezyPrime(313) == False)
    assert(isSteezyPrime(1553) == False)
    print('Passed!')

def testNthSteezyPrime():
    print('Testing nthSteezyPrime()... ', end='')
    assert(nthSteezyPrime(0) == 2)
    assert(nthSteezyPrime(4) == 13)
    assert(nthSteezyPrime(5) == 17)
    assert(nthSteezyPrime(7) == 37)
    assert(nthSteezyPrime(8) == 71)
    assert(nthSteezyPrime(13) == 719)
    print('Passed!')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(0, 0) == 0)
    assert(carrylessAdd(4, 5) == 9)
    assert(carrylessAdd(23, 57) == 70)
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(102, 108) == 200)
    assert(carrylessAdd(865, 23) == 888)
    print('Passed!')

def testVowelCount():
    print('Testing vowelCount()... ', end='')
    assert(vowelCount('abc') == 1)
    assert(vowelCount('123') == 0)
    assert(vowelCount('aw4T3') == 1)
    assert(vowelCount('sPoNgEcAsE') == 4)
    print('Passed!')

#################################################
# hw2 Main
################################################

def testAll():
    testRotateNumber()
    testIsSteezyPrime()
    testNthSteezyPrime()
    testCarrylessAdd()
    testVowelCount()

def main():
    testAll()

if __name__ == '__main__':
    main()
