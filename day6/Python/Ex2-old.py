# Works, but unoptimized for big values
import re

file = open("races.txt","r") # Open file in read-mode
lines = file.read() # Read file by lines

data = re.findall(r'\d+', lines)
raceTime = ""
raceDistance = ""
result = 1
for i in range(len(data)//2):
    raceTime += data[i]
for i in range(len(data)//2, len(data)):
    raceDistance += data[i]

raceTime = int(raceTime)
raceDistance = int(raceDistance)


print(f"Time: {raceTime}, distance:{raceDistance}")
beatRecord = 0
for buttonHold in range(1,raceTime):
    speed = 0
    distanceTraveled = 0
    for acceleration in range(buttonHold):
        speed += 1
    for Travel in range(abs(raceTime-buttonHold)):
        distanceTraveled += speed
        if distanceTraveled > raceDistance:
            beatRecord += 1
            break
result *= beatRecord
print(f"Record could be beated in {beatRecord} different ways")

print(f"Result: {result}")
