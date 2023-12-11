import re

file = open("races.txt","r") # Open file in read-mode
lines = file.read() # Read file

data = re.findall(r'\d+', lines) # Find all digits
racesTime = [] # Lists for holding times and distances
racesDistance = []
result = 1 # Final result
for i in range(len(data)//2): # Append first half of the list to racesTime
    racesTime.append(int(data[i]))
for i in range(len(data)//2, len(data)): # Append second half of the list to racesDistance
    racesDistance.append(int(data[i]))

for i, time in enumerate(racesTime): # For each time
    distance = racesDistance[i] # Get minimal distance needed from list for this time
    print(f"Time: {time}, distance: {distance}")
    beatRecord = 0 # Variable for storing amount of ways the record can be beaten
    for buttonHold in range(1,time): # Test each button hold
        speed = buttonHold # Speed will equal an amount of time the button was pressed
        distanceTraveled = speed * abs(time-buttonHold) # Calculate distance traveled for speed and time left
        if distanceTraveled > distance: # Check if this distance beats record
            beatRecord += 1 # Increment variable if is
    result *= beatRecord # Record to the final result
    print(f"Record could be beaten in {beatRecord} different ways")

print(f"Result: {result}")
