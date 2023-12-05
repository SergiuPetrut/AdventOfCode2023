# Works only with the example schematic, something is wrong on lines from 45 to 70

file = open("schematic.txt","r")
data = file.read()
sumNumbers = 0

adjacentNumbers = []

lineSize = 0
symbolIndexes = []
numIndexes = []
numValues = []
fullValues = []
fullValuesIndexes = []
for i, value in enumerate(data):
    if value == "." or value == "\n":
        if lineSize == 0 and value == "\n":
            lineSize = i+1
        fullValues.append("")
    elif value.isnumeric():
        numIndexes.append(i)
        numIndexStart = 0
        numIndexEnd = 0
        index = i
        while data[index].isnumeric():
            numIndexStart = index
            index -= 1
        index = i
        while data[index].isnumeric():
            numIndexEnd = index
            index += 1 
        num = ""
        for j in range(numIndexStart,numIndexEnd+1):
            num += data[j]
        fullValues.append(int(num))
        numValues.append(int(value))
    else:
        symbolIndexes.append(i)
        fullValues.append("")
adjacentNumbersIndexes = []
indexesUsedUp = []
indexesUsedDown = []
indexesRepeatUp = 0
indexesRepeatDown = 0
for i, value in enumerate(numIndexes):
    for index in symbolIndexes:
        if numIndexes[i] - index == lineSize or numIndexes[i] - index == lineSize+1 or numIndexes[i] - index == lineSize-1 :
            if index not in indexesUsedUp:
                print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} (Up)")
                adjacentNumbersIndexes.append(numIndexes[i])
                if indexesRepeatUp > 1:
                    indexesRepeatUp = []
                    indexesRepeatUp = 0
                else:
                    indexesRepeatUp += 1
                indexesUsedUp.append(index)
                    
        if index - numIndexes[i] == lineSize or index - numIndexes[i] == lineSize+1 or index - numIndexes[i] == lineSize-1 :
            if index not in indexesUsedDown:
                adjacentNumbersIndexes.append(numIndexes[i])
                print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} (Down)")
                if indexesRepeatDown > 1:
                    indexesRepeatDown = []
                    indexesRepeatDown = 0
                else:
                    indexesRepeatDown += 1
                indexesUsedDown.append(index)
        if abs(index - numIndexes[i]) == 1:
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} (Vertical)")
            adjacentNumbersIndexes.append(numIndexes[i])

print(adjacentNumbersIndexes)

pastIndex = -1
for value in adjacentNumbersIndexes:
    if fullValues[value] != pastIndex:
        sumNumbers += fullValues[value]
        pastVal = fullValues[value]
        print(f"|Number: {fullValues[value]}, sum: {sumNumbers}|",end=" ")

print(fullValues)

print(f"Result: {sumNumbers}")

