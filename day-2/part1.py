#! /usr/bin/python
# find checksum given input
def calculateCheckSum(intArray):

    checkDict = {}
    noDouble = 0;
    noTriple = 0;

    for i in range (0, len(intArray)):

        charArray = list(intArray[i])
        checkDict.clear()
        double = False
        triple = False

        for j in range (0, len(charArray)):
            if charArray[j] in checkDict:
                checkDict[charArray[j]] += 1
            else:
                checkDict[charArray[j]] = 1

        for key in checkDict:
            if checkDict[key] == 2:
                double = True
            elif checkDict[key] == 3:
                triple = True

        if double:
            noDouble += 1
        if triple:
            noTriple += 1

    checkSum = noDouble*noTriple

    return checkSum

def main():

    assert(calculateCheckSum(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]) == 12)

    fileInput = open('input1.txt','r')
    inputArray = []
    for line in fileInput:
        inputArray.append(line)
    checkSum = calculateCheckSum(inputArray)
    print(checkSum)
  
if __name__== "__main__":
    main()