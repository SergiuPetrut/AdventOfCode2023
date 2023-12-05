file = open("schematic.txt","r")
lines = file.readlines()
sumNumbers = 0

adjacentNumbers = []

for i, line in enumerate(lines):
    distanceFromSymbol = 0
    symbolIndexes = []
    symbolValues = []
    print(f"Line {i+1} - ",end="")
    for j, element in enumerate(line):
        if element == "." or element == '\n':
            pass
        else:
            symbolIndexes.append(j)
            symbolValues.append(element)
    print(f"Amount of Symbols found: {len(symbolIndexes)}")
    print(symbolValues)
    print(symbolIndexes)
    numValue = ""
    extractedNumbers = []
    symbolValues.append(0)
    symbolIndexes.append(0)
    for j in range(0,len(symbolValues)-1):
        numEnd = False
        if symbolIndexes[j]-1 == symbolIndexes[j-1] and symbolIndexes[j]+1 != symbolIndexes[j+1]:
            numEnd = True
            print(f"{numValue}{symbolValues[j]} - Reach last element")
        if symbolValues[j].isnumeric() and (symbolIndexes[j]+1 == symbolIndexes[j+1] or numEnd):
            numValue += symbolValues[j]
        if numEnd or not symbolValues[j].isnumeric():
            while numValue:
                passed = False
                initialNumIndex = j-len(numValue)+1
                print(f"Number: {numValue} on index {initialNumIndex} ",end="")
                if initialNumIndex > 0:
                    differenceBetweenIndexes = symbolIndexes[initialNumIndex] - symbolIndexes[initialNumIndex-1]
                    if differenceBetweenIndexes < 3:
                       extractedNumbers.append(numValue)
                       print(f"- Found Symbol nearby to the left ({differenceBetweenIndexes})")
                       numValue = ""
                       break
                differenceBetweenIndexes = symbolIndexes[j+1] - symbolIndexes[j]
                if differenceBetweenIndexes < 3 and differenceBetweenIndexes > 0:
                    extractedNumbers.append(numValue)
                    print(f"- Found Symbol nearby to the right ({differenceBetweenIndexes})")  
                numValue = ""
    print(f"Numbers extracted: {len(extractedNumbers)}, sum: {sumNumbers}\n")
    for value in extractedNumbers:
        sumNumbers += int(value)

for value in adjacentNumbers:
    sumNumbers += int(value)
    
print(f"Result: {sumNumbers}")

