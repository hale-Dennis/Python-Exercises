
def makeConsecutive(inputArray):
    inputArray.sort()
    statues = 0
    for i in range(1,len(inputArray)):
        if inputArray[i] - inputArray[i-1] > 1:
            statues += (inputArray[i] - inputArray[i-1]) - 1
    return statues

statues = makeConsecutive([6,2,3,8])
print(statues)
        