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
    return seed
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
        else:
            print("Stopping scan")
            return lowValue
    return lowValue

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
    print(f"Quick scan for locations (range {start} to {end})")
    print(f"0% - {firstLocation} ({len(str(firstLocation))}) 25% - {get_seed_location(start+length//4)} ({len(str(get_seed_location(start+length//4)))}) 50% - {middleLocation} ({len(str(middleLocation))}) 75% - {get_seed_location(end-length//4)} ({len(str(get_seed_location(end-length//4)))}) 100% - {endLocation} ({len(str(endLocation))})")
    half = None
    if firstLocation < middleLocation:
        half = 1
        quarterLocation = get_seed_location(start+length//4)
        quarterSeed = start+length//4
    else:
        half = 2
        quarterLocation = get_seed_location(end-length//4)
        quarterSeed = end-length//4
    print(f"Chosing {half} half")
    if half == 1:
        if quarterLocation > firstLocation:
            startSeed = start
            endSeed = start+length//4
            startScan = "0%"
            endScan = "25%"
        else:
            startSeed = start+length//4
            endSeed = end-length//2
            startScan = "25%"
            endScan = "50%"
    else:
        if quarterLocation < endLocation:
            startSeed = end-length//4
            endSeed = end-length//2
            startScan = "50%"
            endScan = "75%"
        else:
            startSeed = end
            endSeed = end-length//4
            startScan = "75%"
            endScan = "100%"
    print(f"Chosing distance from {startScan} to {endScan} ({startSeed} to {endSeed})")
    scan_seeds(startSeed, endSeed, quarterLocation)

def get_map_values(index):
    destinationRangeStart = int(mapValues[index])
    sourceRangeStart = int(mapValues[index+1])
    rangeLength = int(mapValues[index+2])
    return

print(f"\nResult: {lowestLocationNum}")