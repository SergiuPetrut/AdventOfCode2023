import re

file = open("report.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

extrapolatedValuesSum = 0

for line in lines:
    sequences = re.findall(r'\d+', line)
    amounts = [0,len(sequences)]
    amountsIndex = 0
    flag = True
    while flag:
        for i in range(amounts[amountsIndex],amounts[amountsIndex+1]-1):
            
            sequences.append(int(sequences[i+1])-(int(sequences[i])))
            
            print(sequences[len(sequences)-1],end=" ")
            #print(sequences[i],end=" ")
            #print(amounts)
            #print(amountsIndex,amounts[amountsIndex]-amounts[amountsIndex+1]-1)
        amounts.append(len(sequences))
        amountsIndex += 1
        for i in range(amounts[amountsIndex-1],amounts[amountsIndex]):
            print("")
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