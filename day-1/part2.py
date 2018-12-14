#! /usr/bin/python
# find the first double occurance when adding the line to the total
def firstDouble(intArray):

    total = 0
    lineNo = 0
    totalDict = {
        0: 0
    }

    while True:
        total += intArray[lineNo]
        if total in totalDict:
            break
        else:
            totalDict[total] = lineNo
        lineNo = (lineNo + 1) % len(intArray)

    return total

def main():

    assert(firstDouble([1, -1]) == 0)
    assert(firstDouble([3, 3, 4, -2, -4]) == 10)
    assert(firstDouble([1, -2, 3, 1, 1, -2]) == 2)
    assert(firstDouble([-6, 3, 8, 5, -6]) == 5)
    assert(firstDouble([7, 7, -2, -7, -4]) == 14)

    fileInput = open('input1.txt','r')
    inputArray = []
    for line in fileInput:
        inputArray.append(int(line))
    fileTotal = firstDouble(inputArray)
    print(fileTotal)

if __name__== "__main__":
    main()