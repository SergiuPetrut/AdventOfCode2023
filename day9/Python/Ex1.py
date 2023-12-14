import re

file = open("report.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

extrapolatedValuesSum = 0
# 3493406708 too high
for line in lines:
    sequences = [int(num) for num in re.findall(r'\d+', line)]
    flag = True
    newHistory = 0
    print(sequences)
    while flag:
        for i in range(len(sequences)-1):
            sequences[i] = sequences[i+1]-sequences[i]
        #print(sequences)
           

        if len(sequences) > 0:
            newHistory += sequences[-1]
            sequences.pop()
        else:
            flag = False
            break

        print(sequences)
        if all(element == 0 for element in sequences):
                flag = False
                break

    
    
    extrapolatedValuesSum += newHistory
    print(f"Got {newHistory} (Final sum: {extrapolatedValuesSum})")
print(f"Result: {extrapolatedValuesSum}")