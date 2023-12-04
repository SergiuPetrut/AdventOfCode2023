
cubes = ["blue", "red", "green"]
file = open("game.txt","r")
powerSum = 0
Lines = file.readlines()

indexes = []
names = []
id = 0
for i,line in enumerate(Lines):
    check = [True,True,True]
    minimalCubesNeeded = [0,0,0]
    try:
        for i in range(0,len(cubes)):
            index = line.find(cubes[i])
            while index > 0:
                indexes.append(index)
                names.append(cubes[i])
                num_index = index - 2
                k = 1
                value = 0
                while line[num_index].isnumeric():
                    value += int(line[num_index]) * k
                    num_index -= 1
                    k = k * 10
                if(value > minimalCubesNeeded[i]):
                    minimalCubesNeeded[i] = value
                index = line.find(cubes[i],index+1)
        id += 1
        power = 1
        for value in minimalCubesNeeded:
            power = power * value
        powerSum += power 
        print(f"id: {id} - Minimal Cubes Needed: {cubes[0]}: {minimalCubesNeeded[0]}, {cubes[1]}: {minimalCubesNeeded[1]}, {cubes[2]}: {minimalCubesNeeded[2]}")
        print(f"if: {id} - Power = {power}; Sum: {powerSum}\n")
    except Exception as e:
        print(e)
print(f"Result: {powerSum}")