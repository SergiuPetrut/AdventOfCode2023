
cubes = ["blue", "red", "green"]
maxCubesAmount = [14,12,13]
file = open("game.txt","r")
sumID = 0
Lines = file.readlines()

indexes = []
names = []
id = 0
for i,line in enumerate(Lines):
    cubesSum = [0,0,0]
    check = [True,True,True]
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
                if value > maxCubesAmount[i]:
                    check[i] = False
                cubesSum[i] += value
                index = line.find(cubes[i],index+1)
        id += 1
        print(f"id: {id} - {cubes[0]}: {cubesSum[0]}, {cubes[1]}: {cubesSum[1]}, {cubes[2]}: {cubesSum[2]}")

        passed = False
        if all(i == True for i in check):
            sumID += id
            passed = True
        print(f"id: {id} - {passed}; Sum is {sumID}\n")
    except Exception as e:
        print(e)
print(f"Result: {sumID}")