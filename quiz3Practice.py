import string
def ct1(s):
    if len(s) == 0:
        return ''
    index = string.ascii_lowercase.find(s[0])
    letter = string.ascii_uppercase[-index]
    return letter + ct1(s[1:]) + ct1(s[:-1])

print(ct1('abf'))

def ct(x,y,depth=0):
    print('%d in: %d, %d' % (depth,x,y))
    if x <10:
        result = x
    elif y <10:
        result = y
    elif abs(x-y) <10:
        tmp = ct(x//10,y//10,depth+1)
        result = x%10 + y%10 + tmp
    else:
        a = x%10 + ct(x//10,y,depth+1)
        b = y%10 + ct(x,y//10,depth+1)
        result = a+b
    print('%d out: %d' % (depth,result))
    return result
ct(112,15)

def ct2(s,d=0):
    print(d,s)
    if len(s) > 1 and s[0] != 'b':
        ct2(s[1:],d+1)
        ct2(s[:-1],d+1)
    print(d,'done')
ct2('abc')

def sortCT(L,d=0):
    print(d,':',L)
    if len(L) < 2:
        result = L
    else:
        first = L[0]
        lo, hi = [], []
        for x in L[1:]:
            if x < first:
                lo += [x]
            else:
                hi += [x]
        loNums = sortCT(lo,d+1)
        hiNums = sortCT(hi,d+1)
        result = loNums + [first] + hiNums
    return result
print('result:',sortCT([2,7,6,9,3,0]))

def highestPopulation(d):
    result = set()
    populations = []
    for city in d:
        populations.append(d[city])
    maxPop = max(populations)
    for city in d:
        if populations.count(maxPop) > 1:
            if d[city] == maxPop:
                result.add(city)
        else:
            if d[city] == maxPop:
                result = city
    return result

d = {"seattle":300000, 'pittsburgh': 100000}
print(highestPopulation(d))
d1 = {'seattle':300000,'pittsburgh':300000,'casper':300}
print(highestPopulation(d1))

def getDirections():
    return [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]

def isComplete(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '':
                return False
    return True

def getEmptyCell(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '':
                return (i,j)

def isLegal(grid,row,col):
    for move in getDirections():
        newRow = row + move[0]
        newCol = col + move[1]
        if newRow in range(len(grid)) and newCol in range(len(grid)):
            if grid[newRow][newCol] != '':
                if grid[row][col] == grid[newRow][newCol]:
                    return False
    return True

def fourColoring(grid):
    if isComplete(grid):
        return grid
    row,col = (getEmptyCell(grid))[0],(getEmptyCell(grid))[1]
    for color in ['G','R','Y','B']:
        grid[row][col] = color
        if isLegal(grid,row,col):
            tempSol = fourColoring(grid)
            if tempSol != None:
                return tempSol
    grid[row][col] = ''
    return None

grid = [['','','',''],['','','',''],['','','',''],['','','','']]
print(fourColoring(grid))

def powerSum(n,k):
    if n == 1:
        return 1
    else:
        return n**k + powerSum(n-1,k)
print(powerSum(4,2))

#################################################################

def getHoursLogged(logs):
    result = dict()
    for tuple in logs:
        name = tuple[1]
        if name not in result:
            result[tuple[1]] = tuple[0]
        else:
            result[tuple[1]] -= tuple[0]
    for key in result:
        result[key] = abs(result[key])
    return result

logs = [(0,'spongebob'),(10,'krabs'),(30,'squidward'),(55,'krabs'),(250,'squidward'),(300,'spongebob')]
print(getHoursLogged(logs))

def maxOccur(L):
    result = set()
    bestCount = 0
    currCount = 0
    for elem in L:
        currCount = L.count(elem)
        if currCount > bestCount:
            bestCount = currCount
            result.clear()
            result.add(elem)
        elif currCount == bestCount:
            result.add(elem)
    return result

def mostAppearances(chapter):
    lst = []
    for c in chapter:
        lst.extend(chapter[c])
    return maxOccur(lst)

chapters = {'3':['ender','peter','val','stilson'],'giant':['graff','ender','bernard','alai'],'locke':['graff','peter','val','ender','petra'],'val':['val','ender','graff']}
print(mostAppearances(chapters))

def hasEven(L):
    if len(L) == 0:
        return False
    else:
        if isinstance(L[0],int) and (abs(L[0]) % 2 == 0):
                return True
        else:
            return hasEven(L[1:])

print(hasEven([1,'a',2,set()]))

def sumSquareEvenDigits(n):
    if n == 0:
        return 0
    else:
        if (n%10) % 2 == 0:
            return (n%10)**2 + sumSquareEvenDigits(n//10)
        else:
            return sumSquareEvenDigits(n//10)
print(sumSquareEvenDigits(58474))

###########################################################################

def isLegal(L,n):
    if len(L) != n:
        return False
    for elem in L:
        if elem != 0:
            if L.count(elem) > 1:
                return False
    for i in range(len(L) - 1):
        if L[i] != 0:
            if L[i] % 2 == 0 and L[i+1] != 0 and L[i+1] % 2 == 0:
                return False
            elif L[i] % 2 == 1 and L[i+1] % 2 == 1:
                return False
            elif L[i+1] != 0 and abs(L[i] - L[i+1]) == 1:
                return False
    return True


def validHelper(result,n):
    if 0 not in result:
        return result
    choices = list(range(1, n+1))
    for i in range(len(result)):
        for num in choices:
            result[i] = num
            if isLegal(result,n):
                tempSol = validHelper(result,n)
                if tempSol != None:
                    return tempSol
        result[i] = 0
    return None

def getValidList(n):
    result = [0]*n
    return validHelper(result,n)

print(getValidList(1))
print(getValidList(4))

def hasSquarePairs(lst):
    s = set(lst)
    for n in s:
        if n**2 in s:
            return True
    return False
print(hasSquarePairs([4,3,6,12,9]))
print(hasSquarePairs([4,7,5,22,30]))

def digitCount(n):
    count = 0
    if n < 10:
        return 1
    while n > 0:
        count += 1
        n //= 10
    return count

def rtpHelper(digits,n):
    if digitCount(n) == digits:
        return n


def findRTP(digits):

































