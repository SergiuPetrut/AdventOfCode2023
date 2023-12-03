digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitsNumbers = [1,2,3,4,5,6,7,8,9]
file = open("ex1-file.txt","r")
endoutput = 0
Lines = file.readlines()
for line in Lines:
    try:
        endResult = 0
        start = 0
        end = len(line) - 1
        i = 0
        indexes = []
        numbers = []
        for i in range(0,len(digits)):
            index = line.find(digits[i])
            while(index > -1):
                indexes.append(index)
                numbers.append(digitsNumbers[i])
                index = line.find(digits[i],index+1)
        i = 0
        while i < end:
            if(line[i].isnumeric()):
                indexes.append(i)
                numbers.append(int(line[i]))
                break
            i += 1
        i = end
        while i >= 0:
            if(line[i].isnumeric()):
                indexes.append(i)
                numbers.append(int(line[i]))
                break
            i -= 1
        print(f"index = {indexes}, numbers = {numbers}")
        startIndexValue = indexes[0]
        startIndex = 0
        lastIndexValue = indexes[0]
        lastIndexValue = -1
        for i in range(0,len(indexes)):
            if startIndexValue > indexes[i]:
                startIndexValue = indexes[i]
                startIndex = i
            if lastIndexValue < indexes[i]:
                lastIndexValue = indexes[i]
                lastIndex = i
        
        print(f"The smallest index value : {startIndexValue} ({startIndex}) the biggest index: {lastIndexValue} ({lastIndex})")
        print(f"The smallest value: {numbers[startIndex]} ({startIndex}) the biggest value: {numbers[lastIndex]} ({lastIndex})")
        endResult += numbers[startIndex] * 10 + numbers[lastIndex]
        endoutput += endResult
        print(f"Sum: {endoutput} Num: {endResult}\n")
    except Exception as e:
        print(e)
        pass
print(endoutput)