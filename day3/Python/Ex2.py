# Works only with example schematic, bug somewhere in lines 65 to 82

file = open("schematic.txt","r")
data = file.read()
sumNumbers = 0

lineSize = 0
symbolIndexes = []
numIndexes = []
fullValues = []
adjacentNumbersIndexes = []

def are_close(index1, index2):
    difference = index2 - index1
    row, col = divmod(difference, lineSize)
    return col <= 2 and difference != 0 and row < 3

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
    elif value == "*":
        symbolIndexes.append(i)
        fullValues.append("")
    else:
        fullValues.append("")

for i, value in enumerate(numIndexes):
    for index in symbolIndexes:
        if numIndexes[i] - index == lineSize or numIndexes[i] - index == lineSize+1 or numIndexes[i] - index == lineSize-1 :
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} for * (Up)")
            adjacentNumbersIndexes.append(numIndexes[i])
        if index - numIndexes[i] == lineSize or index - numIndexes[i] == lineSize+1 or index - numIndexes[i] == lineSize-1 :
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} for * (Down)")
            adjacentNumbersIndexes.append(numIndexes[i])
        if abs(index - numIndexes[i]) == 1:
            print(f"index {numIndexes[i]} (num {fullValues[numIndexes[i]]}) is close to index {index} for * (Vertical)")
            adjacentNumbersIndexes.append(numIndexes[i])

inRangeFirstIndexes = []
inRangeSecondIndexes = []
for i, index1 in enumerate(adjacentNumbersIndexes):
    for j in range(i+1,len(adjacentNumbersIndexes)):
        if i == len(adjacentNumbersIndexes)-1:
            pass
        else:
            try:
                if are_close(adjacentNumbersIndexes[i],adjacentNumbersIndexes[j]):
                    print("----------")
                    print(f"Checking index {index1} (num {fullValues[index1]}) and index {adjacentNumbersIndexes[j]} (num {fullValues[adjacentNumbersIndexes[j]]})")
                    print("pass")
                    print("----------")

                    inRangeFirstIndexes.append(index1)
                    inRangeSecondIndexes.append(adjacentNumbersIndexes[j])
                    adjacentNumbersIndexes.remove(index1)
                    adjacentNumbersIndexes.remove(adjacentNumbersIndexes[j])
            except Exception:
                pass
inRangeIndexes = inRangeFirstIndexes + inRangeSecondIndexes
inRangeIndexes.sort()

print(inRangeIndexes)

for i in range(0,2):
    for i, value in enumerate(inRangeIndexes):
        if i >= 0 and i < len(inRangeIndexes)-1:
            if inRangeIndexes[i+1] - value == 1 or inRangeIndexes[i+1] - value == 0:
                inRangeIndexes.pop(i+1)
            elif  inRangeIndexes[i+1] - value == 2 and fullValues[value] == fullValues[inRangeIndexes[i+1]]:
                inRangeIndexes.pop(i+1)
        elif i == len(inRangeIndexes):
            if value - inRangeIndexes[i-1] == 1:
                inRangeIndexes.pop(len(inRangeIndexes)) 

print(inRangeIndexes)


pastVal = -1
i = 0
while i < len(inRangeIndexes):
    sumNumbers += fullValues[inRangeIndexes[i]] * fullValues[inRangeIndexes[i+1]]
    i+= 2


print(f"Result: {sumNumbers}")

