digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # List for holding pre-defined strings
digitsNumbers = [1,2,3,4,5,6,7,8,9] # Representation of each string in digits
file = open("ex1-file.txt","r") # Open file in read-mode
endoutput = 0 # Variable for the final sum
Lines = file.readlines() # Read file by lines
for line in Lines: # Read thru each line
    try:
        endResult = 0 # Variable for holding the first digit and the last digit 
        end = len(line) - 1 # Get the size of string (line)
        i = 0
        indexes = [] # List for holding indexes for all digits-strings
        numbers = [] # List for holding values for all digits-strings
        for i in range(0,len(digits)): # Go thru each pre-defined string
            index = line.find(digits[i]) # Check if line contains the string
            while(index > -1): # find() will output -1 if it won't find anything
                indexes.append(index) # Append index of the string
                numbers.append(digitsNumbers[i]) # Append Equivalent number for it
                index = line.find(digits[i],index+1) # Check if line one more occurrence of the same string
        i = 0
        while i < end: # Almost the same code from ex1
            if(line[i].isnumeric()):
                indexes.append(i) # Append index to compare it later with all indexes
                numbers.append(int(line[i])) # Same for number
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
        startIndexValue = indexes[0] # Initialize values
        startIndex = 0
        lastIndexValue = indexes[0]
        lastIndexValue = -1
        for i in range(0,len(indexes)): # Find the smallest and biggest index in index list
            if startIndexValue > indexes[i]:
                startIndexValue = indexes[i]
                startIndex = i
            if lastIndexValue < indexes[i]:
                lastIndexValue = indexes[i]
                lastIndex = i
        
        print(f"The smallest index value : {startIndexValue} ({startIndex}) the biggest index: {lastIndexValue} ({lastIndex})")
        print(f"The smallest value: {numbers[startIndex]} ({startIndex}) the biggest value: {numbers[lastIndex]} ({lastIndex})")
        endResult += numbers[startIndex] * 10 + numbers[lastIndex] # Merge the left and right numbers
        endoutput += endResult # Add result to the final sum
        print(f"Sum: {endoutput} Num: {endResult}\n")
    except Exception as e:
        print(e)
        pass
print(f"Result: {endoutput}") # Print result