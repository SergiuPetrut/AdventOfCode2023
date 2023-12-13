file = open("network.txt","r") # Open file in read-mode
lines = file.read() # Read file by lines

i = 0
navigation = []
while lines[i] != "\n":
    navigation.append(lines[i])
    i+=1

steps = 0
currentPos = "AAA"
while currentPos != "ZZZ":
    for direction in navigation:
        pos = 0
        if direction == "L":
            index = lines.find(f"{currentPos} = (")
            pos = index + 7
        else:
            index = lines.find(f"{currentPos} = (")
            pos = index + 12            
        currentPos = ""
        steps += 1
        for i in range(0,3):
            currentPos += f"{lines[pos+i]}"
        print(f"Going to {direction} - {currentPos}")


print(f"Result: {steps}")