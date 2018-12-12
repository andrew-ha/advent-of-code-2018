#! /usr/bin/python
# add input of integers together
def sumTotal(intArray):
    total = 0
    for element in intArray:
        total += element
    return total

def main():

    assert(sumTotal([1, -2, 3, 1]) == 3)
    assert(sumTotal([1, 1, 1]) == 3)
    assert(sumTotal([1, 1, -2]) == 0)
    assert(sumTotal([-1, -2, -3]) == -6)

    fileInput = open('input1.txt','r')
    inputArray = []
    for line in fileInput:
        inputArray.append(int(line))
    fileTotal = sumTotal(inputArray)
    print(fileTotal)
  
if __name__== "__main__":
    main()