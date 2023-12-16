# Works, but uses slower solution

file = open("report.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

extrapolatedValuesSum = 0

for line in lines:
    sequences = [int(i) for i in line.split()]
    amounts = [0,len(sequences)]
    amountsIndex = 0
    flag = True
    while flag:
        for i in range(amounts[amountsIndex],amounts[amountsIndex+1]-1):
            
            sequences.append(int(sequences[i+1])-(int(sequences[i])))
            
        amounts.append(len(sequences))
        amountsIndex += 1
        for i in range(amounts[amountsIndex-1],amounts[amountsIndex]):
            if sequences[i] != 0:
                flag = True
                break
            flag = False

    newHistory = 0
    for i in range(amountsIndex,0,-1):
        lineIndex = amounts[i] - 1
        newHistory += int(sequences[lineIndex])
    extrapolatedValuesSum += newHistory
    print(f"Got {newHistory} (Final sum: {extrapolatedValuesSum})")
print(f"Result: {extrapolatedValuesSum}")