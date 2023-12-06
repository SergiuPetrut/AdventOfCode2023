file = open("schematic.txt","r")
data = file.read()
sumNumbers = 0

lineSize = 0
symbolIndexes = []
numIndexes = []
fullValues = []
adjacentNumbersIndexes = []

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
    else:
        symbolIndexes.append(i)
        fullValues.append("")

for i, value in enumerate(numIndexes):
    for index in symbolIndexes:
        if numIndexes[i] - index == lineSize or numIndexes[i] - index == lineSize+1 or numIndexes[i] - index == lineSize-1 :
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} (Up)")
            adjacentNumbersIndexes.append(numIndexes[i])
        if index - numIndexes[i] == lineSize or index - numIndexes[i] == lineSize+1 or index - numIndexes[i] == lineSize-1 :
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} (Down)")
            adjacentNumbersIndexes.append(numIndexes[i])
        if abs(index - numIndexes[i]) == 1:
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} (Vertical)")
            adjacentNumbersIndexes.append(numIndexes[i])
for i in range(0,2):
    for i, value in enumerate(adjacentNumbersIndexes):
        if i >= 0 and i < len(adjacentNumbersIndexes)-1:
            if adjacentNumbersIndexes[i+1] - value == 1:
                adjacentNumbersIndexes.pop(i+1)
            elif  adjacentNumbersIndexes[i+1] - value == 2 and fullValues[value] == fullValues[adjacentNumbersIndexes[i+1]]:
                adjacentNumbersIndexes.pop(i+1)
        elif i == len(adjacentNumbersIndexes):
            if value - adjacentNumbersIndexes[i-1] == 1:
                adjacentNumbersIndexes.pop(len(adjacentNumbersIndexes)) 

for value in adjacentNumbersIndexes:
    if fullValues[value]:
        sumNumbers += fullValues[value]
print(f"Result: {sumNumbers}")

