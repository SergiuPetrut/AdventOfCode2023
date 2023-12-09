# W.I.P.
import re

file = open("seeds.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

maps = ["seeds:","seed-to-soil map:", "soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:","end"]
position = 0

holdValues = []

lowestLocationNum = None
mapValues = []

def get_seed_location(seed):
    for position in range(len(holdValues)):
        mapValues = get_mapValues(position)
        if seedsRanges != mapValues:
            j = 0
            while j < len(mapValues): # Go thru each ranges
                destinationRangeStart = int(mapValues[j])
                sourceRangeStart = int(mapValues[j+1])
                rangeLength = int(mapValues[j+2])
                j += 3
                if seed >= sourceRangeStart and seed < sourceRangeStart + rangeLength:
                    difference = sourceRangeStart - destinationRangeStart
                    seed = seed - difference
                    break
    return int(seed)
def get_mapValues(position):
    mapValues = re.findall(r'\d+', holdValues[position]) # Get values from map
    return mapValues

def scan_seeds(start,stop, lowValue):
    print(f"Scanning seeds from {start} to {stop}")
    if stop - start > 0:
        step = 1
    else:
        step = -1
    for seed in range(start,stop,step): # Go thru each seed
        location = int(get_seed_location(seed))
        if (lowValue == None):
            lowValue = location
            print(f"Found new shortest location: {location} (seed: {seed})")
        elif lowValue > location:
            print(f"Found new shortest location: {location}")
            lowValue = location

    return lowValue
# 7911904 // 7875970 // 7873367 (to high)
def find_best_distance(start, length,end):
    seedsLocations = []
    seedsNums = []
    k = 0.0
    fragments = 1000
    procent = 1 / (fragments-1)
    for i in range(0,fragments):
        if k > 0.98:
            k = 1
        seedsLocations.append(get_seed_location(start + int(length * k)))
        seedsNums.append(start + int(length * k))
        k += procent
        
    lowestLocationIndex = seedsLocations.index(min(seedsLocations))
    if lowestLocationIndex > 0 and lowestLocationIndex < 9:
        if seedsLocations[lowestLocationIndex-1] > seedsLocations[lowestLocationIndex+1]:
            endSeed = seedsNums[lowestLocationIndex+1]
        else:
            endSeed = seedsNums[lowestLocationIndex-1]
    elif lowestLocationIndex == 0:
        endSeed = seedsNums[1] # 10%
    else:
        endSeed = seedsNums[8] # 20%

    print(f"Quick scan for locations (range {start} to {end} ({length} length))")
    print("Seeds:",end="")
    for i in range(0,fragments):
        print(f" {i*100/(fragments-1)}% - {seedsNums[i]} ",end="|")
    print("\nLocations:",end="")
    for i in range(0,fragments):
        print(f" {i*100/(fragments-1)}% - {seedsLocations[i]} ",end="|")    

    print(f"\nChosing distance from {seedsNums[lowestLocationIndex]} to {endSeed} (Locations {get_seed_location(seedsNums[lowestLocationIndex])} to {get_seed_location(endSeed)})")
    return seedsNums[lowestLocationIndex], endSeed, seedsLocations[lowestLocationIndex]


for line in lines:
    if line.find(maps[position]) != -1:
        if position < len(maps):
            position += 1
            holdValues.append("")
    nums = re.findall(r'\d+', line)
    for num in nums:
        holdValues[position-1] += f"{num};"

seedsRanges = re.findall(r'\d+', holdValues[0])
newSeeds = []
for i in range(0,len(seedsRanges),2):
    newSeeds.append(seedsRanges[i])
pos = 0
while pos < len(seedsRanges):
    start = int(seedsRanges[pos])
    length = int(seedsRanges[pos+1])
    end = start + length
    percent = int(0.01 * length)
    pos+= 2
    amountToScan = 1000
    i = 0
    oldLowest = lowestLocationNum

    firstLocation = get_seed_location(start)
    middleLocation = get_seed_location(end-length//2)
    endLocation = get_seed_location(end)
    startSeed, endSeed, lowestLocation =  find_best_distance(start,length,end)
    while abs(startSeed - endSeed) > 500 :
        print("Trying to find shorter range")
        startSeed, endSeed, lowestLocation =  find_best_distance(start,length,end)
        start = startSeed
        end = endSeed
        length = abs(end-start)
    lowestLocation = scan_seeds(startSeed, endSeed, lowestLocation)
    if lowestLocationNum == None:
        lowestLocationNum = lowestLocation
    elif lowestLocationNum > lowestLocation:
        lowestLocationNum = lowestLocation

def get_map_values(index):
    destinationRangeStart = int(mapValues[index])
    sourceRangeStart = int(mapValues[index+1])
    rangeLength = int(mapValues[index+2])
    return

print(f"\nResult: {lowestLocationNum}")