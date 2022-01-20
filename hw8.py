#################################################
# 15-112-m19 hw8
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################
# question 1
#################################################

def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2) # O(1)
    a = lst.pop() # O(1)
    b = lst.pop(0) # O(N)
    lst.insert(0, a) # O(N)
    lst.append(b) # O(1)
'''
A. For a list, lst, of length 2 or greater, it swaps the first and last element.

B. O(N)

C.
'''
def betterSlow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2) # O(1)
    lst[0],lst[len(lst) - 1] = lst[len(lst) - 1],lst[0] # O(1)
'''
D. O(1)
'''
#################################################

def slow2(lst): # N is the length of the list lst
    counter = 0 # O(1)
    for i in range(len(lst)): # O(N)
        if lst[i] not in lst[:i]: # O(N)
            counter += 1 # O(1)
    return counter # O(1)
'''
A. Returns the number of distinct elements in list, lst.

B. O(N**2)

C.
'''
def betterSlow2(lst): # N is the length of the list lst
    sList = set(lst) #O(1)
    return len(sList) # O(1)
'''
D. O(1)
'''
#################################################

import string
def slow3(s): # N is the length of the string s
    maxLetter = "" # O(1)
    maxCount = 0 # O(1)
    for c in s: # O(N)
        for letter in string.ascii_lowercase: # O(1)
            if c == letter: # O(1)
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and c < maxLetter: # O(N)
                    maxCount = s.count(c) # O(N)
                    maxLetter = c # O(1)
    return maxLetter # O(1)
'''
A. Returns the lowercase letter in string, s, with the highest frequency of 
occurrence. Does not treat lowercase the same as uppercase letters. If there 
is a tie, function returns the letter that occurs first in the alphabet.

B. O(N**3)

C.
'''
import string
def betterSlow3(s): # N is the length of the string s
    numOccur = dict() # O(1)
    for c in s: # O(N)
        if c in numOccur: # O(N)
            numOccur[c] += 1 # O(1)
        else: # O(1)
            numOccur[c] = 1 # O(1)
    maxLetter = "" # O(1)
    maxCount = 0 # O(1)
    for c in numOccur: # O(N)
        if numOccur[c] > maxCount or \
        numOccur[c] == maxCount and c < maxLetter: # O(1)
            maxLetter = c # O(1)
            maxCount = numOccur[c] # O(1)
    return maxLetter # O(1)
'''
D. O(N**2)
'''
#################################################
# hw8 problems
#################################################

#returns new dictionary that is inverse of original dictionary
#inverse - original values are mapped to set of original keys
def invertDictionary(d):
    newD = {}
    keys = []
    if len(d) == 0: #edge case
        return {}
    for key in d:
        oldValue = d[key]
        for key in d: #duplicate values
            newValue = d[key]
            if oldValue == newValue:
                keys += [key]
        newD[oldValue] = set(keys)
        keys = [] #reset list for other values
    return newD

#returns largest sum between any 2 pairs in list a; runs in O(n) time
def largestSumOfPairs(a):
    if len(a) <= 1: #edge case
        return None
    sum = max(a)
    a.remove(max(a))
    sum += max(a) #adds largest element and second largest element
    return sum

#################################################
# hw8 test functions 
#################################################

def testInvertDictionary():
    assert(invertDictionary({}) == {})
    assert(invertDictionary({1:3}) == {3:set([1])})
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) ==
       {2:set([1]), 3:set([2,5]), 4:set([3])})
    assert(invertDictionary({1:2, 1:2, 1:2}) == {2:set([1])})
    assert(invertDictionary({2:3, 1:4, 17:17, 8:17, 17:17}) ==
        {3:set([2]),4:set([1]),17:set([8,17])})
    print('Passed!')

def testLargestSumOfPairs():
    assert(largestSumOfPairs([]) == None)
    assert(largestSumOfPairs([8]) == None)
    assert(largestSumOfPairs([10,10,10]) == 20)
    assert(largestSumOfPairs([8,4,2,8]) == 16)
    assert(largestSumOfPairs([1,4,3,2]) == 7)
    print('Passed!')

#################################################
# hw4 Main
################################################

def testAll():
    testInvertDictionary()
    testLargestSumOfPairs()

def main():
    testAll()

if __name__ == '__main__':
    main()