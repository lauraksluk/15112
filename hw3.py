#################################################
# 15-112-m19 hw3
# Your Name: Laura (Kai Sze) Luk
# Your Andrew ID: kluk
# Your Section: C
#################################################

import math
import string

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

#returns the average of the numbers in string s beginning with a name
def averageS (s):
    sum = 0
    grade = s.split(',')
    for i in range (1, len(grade)):
        sum += int(grade[i])
    average = roundHalfUp(sum/(len(grade) - 1))
    return average

#returns the name at beginning of string s
def getName (s):
    name = ''
    for i in range (len(s)):
        if s[i].isalpha():
            name += s[i]
    return name

#################################################
# hw3 problems
#################################################

#returns Boolean value depending on if s1 and s2 are anagrams
def areAnagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == len(s2):
        if s1 == s2 == '':
            return True
        else:
            for c in s1:
                if s1.count(c) != s2.count(c):
                    return False
            return True
    else:
        return False

#returns student with highest average (name: average) in gradebook
def bestStudentAndAvg(gradebook):
    best = -100000000000
    currAvg = 0
    bestName = ''
    for line in gradebook.splitlines():
        if line.startswith('#') or len(line) == 0:
            continue
        else:
            currAvg = averageS(line)
            if currAvg > best:
                best = currAvg
                bestName = getName(line)
    bestName += ':' + str(best)
    return bestName

#returns encoded string of message prepended with key
def encodeColumnShuffleCipher(message, key):
    lenM = len(message)
    lenK = len(key)
    col = ''
    if lenM % lenK == 0:
        for i in range(lenK):
            col += message[i::(lenK)] + '\n'
    else:
        for i in range(lenM % lenK):
            col += message[i::(lenK)] + '\n'
        for j in range(lenK - (lenM % lenK)):
            col += message[(j+i+1)::(lenK)] + '-\n'
    col = col.splitlines()
    temp = ''
    for k in range(len(key)):
        temp += col[int(key[k])]
    result = key + temp
    return result

#returns original message from encoded message
def decodeColumnShuffleCipher(message):
    key = ''
    for i in range(len(message)):
        if message[i].isdigit():
            key += message[i]
    code = message[len(key)::]
    lenC = len(code)
    lenK = len(key)
    temp = ''
    for j in range (0, lenC, lenC//lenK):
        temp += code[j:(j+lenC//lenK)] + '\n'
    temp = temp.splitlines()
    s = ''
    for j in range(lenK):
        index = key.find(str(j))
        s += temp[index]
    result = ''
    for k in range(len(s)//lenK):
        result += s[k::len(s)//lenK]
    result = result.replace('-','')
    return result

print(decodeColumnShuffleCipher('3195627804CNESETOTNSEOENNOTNEKIPCOSNMAFAEEIHOAOHEUNEERPNRLITOYONNOCEESDAESTTOAUOTWRWLLTRLURRANRBNKSDTTRHEGEGEKNOWPTSETUENIAHHESHDRWOHHYSHSNAWOTIASHWEB-WNYTSEHIEEIKWBPCOWSHECNSOINSRMLYWPMSLHFATWLBNL-AGTTIBANOHNHAUIONHEOWTVSNNDHTAVAHLAYDEGNHHYBKO-INVFHNDOOEPBTIDSAAHOLTRIAINLDDFEPTEDWTLGIIDEHAESTIISAVGRATESTCNSAOUIUEOSHAEHDENEEKCBTEDEEAIES-BORNTNITTDORRITVITFGTRRSIESCEERDTAIHERTPDNWTYE-AGEDBRAGDIEHIAHRRISBTOSAEEOEUOESTEUGIOUICIUIISYEIRIRHFHCHDORGORIDUTCIONCGISOYEPDEFIUTOPGSNAIC-'))

#################################################
# hw3 Test Functions
################################################

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    assert(areAnagrams("abc", "abcc") == False)
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")

def testEncodeColumnShuffleCipher():
    print("Testing encodeColumnShuffleCipher()...", end="")

    msg = "ILOVECMUSOMUCH"
    result = "021IVMOCOCSU-LEUMH"
    assert(encodeColumnShuffleCipher(msg, "021") == result)

    msg = "WEATTACKATDAWN"
    result = "0213WTAWACD-EATNTKA-"
    assert(encodeColumnShuffleCipher(msg, "0213") == result)

    msg = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    result = "210DNAIRBWHNYRCSYRUEYHEBTTIESNOBESDLWTAIIPKEALEH"
    assert(encodeColumnShuffleCipher(msg,"210") == result)

    print("Passed!")

def testDecodeColumnShuffleCipher():
    print("Testing decodeColumnShuffleCipher()...", end="")
    msg = "0213WTAWACD-EATNTKA-"
    result = "WEATTACKATDAWN"
    assert(decodeColumnShuffleCipher(msg) == result)

    msg = "210DNAIRBWHNYRCSYR-UEYHEBTTIESNOBE-SDLWTAIIPKEALEH-"
    result = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    assert(decodeColumnShuffleCipher(msg) == result)

    print("Passed!")

#################################################
# hw4 Main
################################################

def testAll():
    testAreAnagrams()
    testBestStudentAndAvg()
    testEncodeColumnShuffleCipher()
    testDecodeColumnShuffleCipher()

def main():
    testAll()

if __name__ == '__main__':
    main()
