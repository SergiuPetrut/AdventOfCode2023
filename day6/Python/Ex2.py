import re

file = open("races.txt","r") # Open file in read-mode
lines = file.read() # Read file

data = re.findall(r'\d+', lines) # Find all digits
racesTime = "" # Strings for holding time and distance
raceDistance = ""
result = 1
for i in range(len(data)//2): # Unite all values for time into one big one
    raceTime += data[i]
for i in range(len(data)//2, len(data)): # Unite all values for distance into one big one
    raceDistance += data[i]

raceTime = int(raceTime) # Make them integers
raceDistance = int(raceDistance)


print(f"Time: {raceTime}, distance: {raceDistance}")
beatRecord = 0 # Variable for storing amount of ways the record can be beaten
for buttonHold in range(1,raceTime):  # Test each button hold
    speed = buttonHold # Speed will equal an amount of time the button was pressed
    distanceTraveled = speed * abs(raceTime-buttonHold) # Calculate distance traveled for speed and time left
    if distanceTraveled > raceDistance: # Check if this distance beats record
        beatRecord += 1 1 # Increment variable if is
result *= beatRecord # Record to the final result
print(f"Record could be beaten in {beatRecord} different ways")

print(f"Result: {result}")
