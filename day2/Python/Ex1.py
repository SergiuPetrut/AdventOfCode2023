
cubes = ["blue", "red", "green"] # List for pre-defined values for cubes
maxCubesAmount = [14,12,13] # List for maximum allowed cubes in each set
file = open("game.txt","r") # Open file in read-mode
sumID = 0 # Final sum of all IDs
Lines = file.readlines() # Read file by lines

indexes = [] # Hold indexes for each cube in each set
names = [] # Hold values for each cube in each set
id = 0 # Initialize id
for i,line in enumerate(Lines): # Going thru each line
    cubesSum = [0,0,0] # Set initial sum for each cube to be 0
    check = [True,True,True] # Set check for each bag
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
                if value > maxCubesAmount[i]: # Check if the value is bigger than allowed
                    check[i] = False # Mark false if is
                cubesSum[i] += value # Record the value for cube to the total sum for this line
                index = line.find(cubes[i],index+1) # Look for the next mention of cube color
        id += 1 # Increase the ID by 1
        print(f"id: {id} - {cubes[0]}: {cubesSum[0]}, {cubes[1]}: {cubesSum[1]}, {cubes[2]}: {cubesSum[2]}")

        passed = False # Initialize the variable for the final result for this line
        if all(i == True for i in check): # Check if all numbers are in limit
            sumID += id # Record ID of the possible game
            passed = True # Set the variable to true
        print(f"id: {id} - {passed}; Sum is {sumID}\n")
    except Exception as e:
        print(e)
print(f"Result: {sumID}") # Print the final sum of all IDs where the game is possible