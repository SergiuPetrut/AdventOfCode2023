import re

file = open("races.txt","r") # Open file in read-mode
lines = file.read() # Read file by lines

data = re.findall(r'\d+', lines)
racesTime = []
racesDistance = []
result = 1
for i in range(len(data)//2):
    racesTime.append(int(data[i]))
for i in range(len(data)//2, len(data)):
    racesDistance.append(int(data[i]))

for i, time in enumerate(racesTime):
    distance = racesDistance[i]
    print(f"Time: {time}, distance:{distance}")
    beatRecord = 0
    for buttonHold in range(1,time):
        speed = 0
        distanceTraveled = 0
        for acceleration in range(buttonHold):
            speed += 1
        for Travel in range(abs(time-buttonHold)):
            distanceTraveled += speed
        if distanceTraveled > distance:
            beatRecord += 1
    result *= beatRecord
    print(f"Record could be beated in {beatRecord} different ways")

print(f"Result: {result}")
