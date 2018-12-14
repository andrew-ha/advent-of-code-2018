#! /usr/bin/python
# add input of integers together
def findCorrectBox(intArray):

    return checkSum

def main():

    assert(findCorrectBox(["abcdef", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == "fgij")

    fileInput = open('input1.txt','r')
    inputArray = []
    for line in fileInput:
        inputArray.append(line)
    checkSum = findCorrectBox(inputArray)
    print(checkSum)
  
if __name__== "__main__":
    main()