file = open("pipes.txt","r") # Open file in read-mode
data = file.read() # Read file by lines


startingPos = data.find("S")
startingPos1,startingPos2 = [None,None],[None,None]

lineSize = data.find("\n") 

def getNewPos(pos,direction):
    element = data[pos]
    print(pos,direction,element)
    if element == "|":
        if direction == "up":
            return pos-lineSize-1,direction
        else:
            return pos+lineSize+1,direction
    elif element == "-":
        if direction == "left":
            return pos-1,direction
        else:
            return pos+1,direction
    elif element == "7":
        if direction == "right":
            return pos+lineSize+1,"down"
        else:
            return pos-1,"left"
    elif element == "J":
        if direction == "right":
            return pos-lineSize-1,"up"
        else:
            return pos-1,"left"
    elif element == "L":
        if direction == "left":
            return pos-lineSize-1,"up"
        else:
            return pos+1,"right"
    elif element == "F":
        if direction == "left":
            return pos+lineSize+1,"down"
        else:
            return pos+1,"right"
        
for i in range(1,-2,-2):
    element = data[startingPos+i]
    if element == "|" or element == ".":
        continue
    if not startingPos1[0]:
        startingPos1 = [startingPos+i,"right"]
    else:
        startingPos2 = [startingPos+i,"left"]
for i in range(0-lineSize-1,lineSize*2+2,lineSize*2+2):
    element = data[startingPos+i]
    if element == "." or element == "-":
        continue
    if not startingPos1[0]:
        startingPos1 = [startingPos+i,"up"]
    else:
        startingPos2 = [startingPos+i,"down"]
print(startingPos2,startingPos,startingPos1)
i = 0
while True:
    i += 1
    print("startpos1:")
    startingPos1 = getNewPos(startingPos1[0],startingPos1[1])
    print("startpos2:")
    startingPos2 = getNewPos(startingPos2[0],startingPos2[1])
    print(startingPos2[0],startingPos,startingPos1[0])
    if startingPos2[0] == startingPos1[0]:
        i += 1
        break


print(startingPos2,startingPos,startingPos1)
print(f"Result:{i}")