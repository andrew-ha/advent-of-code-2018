#! /usr/bin/python
# find the correct box as stated in advent calendar
def findCorrectBox(intArray):

    noMaxMatches = 0
    correctBox1 = 0
    correctBox2 = 0

    # finding which pair has the most matches
    for x in range(0, len(intArray)):
        word1 = list(intArray[x])
        for y in range(x+1, len(intArray)):
            word2 = list(intArray[y])
            matches = 0
            # for lines of unequal length
            if len(word1) < len(word2):
                maxRange = len(word1)
            else:
                maxRange = len(word2)
            for z in range (0, maxRange):
                if word1[z] == word2[z]:
                    matches += 1
            if matches > noMaxMatches:
                correctBox1 = x
                correctBox2 = y
                noMaxMatches = matches

    # displaying matches in nice fore
    finalWord = []

    word1 = list(intArray[correctBox1])
    word2 = list(intArray[correctBox2])
    for z in range (0, len(word1)):
        if word1[z] == word2[z]:
            finalWord.append(word1[z])

    finalString = ''.join(finalWord)

    return finalString

def main():

    assert(findCorrectBox(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == "fgij")

    fileInput = open('input1.txt','r')
    inputArray = []
    for line in fileInput:
        inputArray.append(line)
    checkSum = findCorrectBox(inputArray)
    print(checkSum)
  
if __name__== "__main__":
    main()