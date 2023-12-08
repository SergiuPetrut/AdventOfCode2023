import re

file = open("seeds.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

maps = ["seeds:","seed-to-soil map:", "soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:","end"]
position = 0

holdValues = []

lowestLocationNum = None

for line in lines:
    if line.find(maps[position]) != -1:
        if position < len(maps):
            position += 1
            holdValues.append("")
    nums = re.findall(r'\d+', line)
    for num in nums:
        holdValues[position-1] += f"{num};"

seeds = re.findall(r'\d+', holdValues[0])
newSeeds = re.findall(r'\d+', holdValues[0])

for i, values in enumerate(holdValues):
    mapValues = re.findall(r'\d+', values)
    if seeds != mapValues:
        j = 0
        while j < len(mapValues):
            destinationRangeStart = int(mapValues[j])
            sourceRangeStart = int(mapValues[j+1])
            rangeLength = int(mapValues[j+2])
            j += 3
            print(f"{maps[i]} - Destination: {destinationRangeStart}, Source: {sourceRangeStart}, Range: {rangeLength}")
            for k, seed in enumerate(seeds):
                seed = int(seed)
                if seed >= sourceRangeStart and seed < sourceRangeStart + rangeLength:
                    difference = sourceRangeStart - destinationRangeStart
                    newSeeds[k] = seed - difference
                    print(f"Seed {seed}- New value: {newSeeds[k]}")
    seeds = newSeeds.copy() # Copy values, dont make a pointer
print("Locations:")
for seed in seeds:
    print(int(seed),end=", ")
    if lowestLocationNum == None:
        lowestLocationNum = seed
    elif lowestLocationNum > seed:
        lowestLocationNum = seed
print(f"\nResult: {lowestLocationNum}")