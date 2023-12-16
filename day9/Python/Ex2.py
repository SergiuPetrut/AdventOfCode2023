import numpy as np

file = open("report.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

extrapolatedValuesSum = 0
for line in lines:
    sequence = [int(i) for i in line.split()]
    sequence.reverse()
    degree = len(sequence)-1
    result = np.polynomial.polynomial.Polynomial.fit(np.arange(len(sequence)), sequence, deg=degree)
    newHistory = round(result(len(sequence)))
    extrapolatedValuesSum += round(newHistory)
    print(f"Got {newHistory} (Final sum: {extrapolatedValuesSum})")
print(f"Result: {extrapolatedValuesSum}")