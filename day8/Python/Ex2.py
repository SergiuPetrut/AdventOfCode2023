# W.I.P.
file = open("network.txt","r") # Open file in read-mode
lines = file.read() # Read file by lines

i = 0
navigation = []
while lines[i] != "\n":
    navigation.append(lines[i])
    i+=1

steps = 0
currentPos = []

index = 0
while index < len(lines):
    index = lines.find("A = (",index+1)
    if index == -1:
        break
    currentPos.append("A")
    for i in range(1,3):
        currentPos[len(currentPos)-1] = lines[index-i] + currentPos[len(currentPos)-1]
    if currentPos[len(currentPos)-1] == "AAA":
        currentPos.pop()
    print(index)

print(currentPos)
stopFlag = True
while stopFlag:
    skip = None
    for direction in navigation:
        steps += 1
        for currentPosIndex, position in enumerate(currentPos):
            pos = 0
            if direction == "L":
                index = lines.find(f"{position} = (")
                pos = index + 7
            else:
                index = lines.find(f"{position} = (")
                pos = index + 12            
            nextCurrentPos = ""
            for i in range(0,3):
                nextCurrentPos += f"{lines[pos+i]}"
            print(f"{direction} - {position} --> {nextCurrentPos} (step: {steps})",end=", ")
            position = nextCurrentPos
            currentPos[currentPosIndex] = nextCurrentPos
        print("")
    for check in currentPos:
        if check[2] != "Z":
            stopFlag = True
            break
        stopFlag = False
print(f"Result: {steps}")