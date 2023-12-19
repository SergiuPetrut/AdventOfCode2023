import re

file = open("seeds.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

maps = ["seeds:","seed-to-soil map:", "soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:","end"] # List of pre-defined maps labels
# Initialize position, holdValues list, and lowestLocationNum variable
position = 0
holdValues = []
lowestLocationNum = None

for line in lines: # Going thru each line
    if line.find(maps[position]) != -1: # Check if the line contains the current map name
        if position < len(maps): # Check if it is not the last element in the maps list
            position += 1 # Increment position by one
            holdValues.append("") # Initialize an empty string for the current map
    nums = re.findall(r'\d+', line) # Find all numeric values in the current line
    for num in nums:
        holdValues[position-1] += f"{num};" # Append the numeric values to the corresponding map in holdValues
# Extract seeds from the first map in holdValues
seeds = re.findall(r'\d+', holdValues[0]) 
newSeeds = re.findall(r'\d+', holdValues[0])

for i, values in enumerate(holdValues): # Going thru each value
    mapValues = re.findall(r'\d+', values)  # Extract numeric values from the current map
    if seeds != mapValues: # Compare seeds with the current mapValues
        j = 0 # Initialize j value that will be used to limit extraction from mapValues
        while j < len(mapValues): # Check if j is less than mapValues
            # Extract destination range start, source range start, and range length
            destinationRangeStart = int(mapValues[j])
            sourceRangeStart = int(mapValues[j+1])
            rangeLength = int(mapValues[j+2])
            j += 3 # Increment j by the amount of items that were scanned
            print(f"{maps[i]} - Destination: {destinationRangeStart}, Source: {sourceRangeStart}, Range: {rangeLength}")
            # Update seeds based on the conversion rules
            for k, seed in enumerate(seeds):
                seed = int(seed)
                if seed >= sourceRangeStart and seed < sourceRangeStart + rangeLength:
                    difference = sourceRangeStart - destinationRangeStart
                    newSeeds[k] = seed - difference
                    print(f"Seed {seed}- New value: {newSeeds[k]}")
    seeds = newSeeds.copy() # Copy values, dont make a pointer
print("Locations:")
for seed in seeds: # Find the lowest location number
    print(int(seed),end=", ")
    if lowestLocationNum == None:
        lowestLocationNum = seed
    elif lowestLocationNum > seed:
        lowestLocationNum = seed
print(f"\nResult: {lowestLocationNum}")