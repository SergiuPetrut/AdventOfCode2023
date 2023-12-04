
cubes = ["blue", "red", "green"] # List for pre-defined values for cubes
file = open("game.txt","r") # Open file in read-mode
powerSum = 0 # Final sum of all powers
Lines = file.readlines() # Read file by lines

indexes = [] # Hold indexes for each cube in each set
names = [] # Hold values for each cube in each set
id = 0 # Initialize id
for i,line in enumerate(Lines): # Going thru each line
    minimalCubesNeeded = [0,0,0] # List for holding maximum values for cubes in a line
    try:
        for i in range(0,len(cubes)):
            index = line.find(cubes[i]) # Looking for cuber in cubes[3] order
            while index > 0: # If the cube is present
                indexes.append(index) # Record the index of the first mention 
                names.append(cubes[i]) # Record the name of the cube for this index
                num_index = index - 2 # Go back in line and look for the value
                k = 1
                value = 0
                while line[num_index].isnumeric(): # While the value is a number
                    value += int(line[num_index]) * k # Get the value
                    num_index -= 1 # Go one place back to see if is also a number
                    k = k * 10 # Increase k for the next number
                if(value > minimalCubesNeeded[i]): # Check if the value is bigger than the one in previous set
                    minimalCubesNeeded[i] = value # Record the value for cube if it is
                index = line.find(cubes[i],index+1) # Look for the next mention of cube color
        id += 1 # Increase the ID by 1
        power = 1 # Initialize variable for power of all cubes
        for value in minimalCubesNeeded: # Go thru each value in the list
            power = power * value
        powerSum += power # Add power value of a line to the final result
        print(f"id: {id} - Minimal Cubes Needed: {cubes[0]}: {minimalCubesNeeded[0]}, {cubes[1]}: {minimalCubesNeeded[1]}, {cubes[2]}: {minimalCubesNeeded[2]}")
        print(f"if: {id} - Power: {power}, Sum: {powerSum}\n")
    except Exception as e:
        print(e)
print(f"Result: {powerSum}") # Print the final sum of all powers