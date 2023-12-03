file = open("ex1-file.txt","r") # Open file in read-mode
endoutput = 0 # Variable for the final sum
Lines = file.readlines() # Read file by lines
for line in Lines: # Going thru each line
    try:
        endResult = "" # Variable for holding the first digit and the last digit
        end = len(line) - 1 # Get the size of string (line)
        i = 0 # Start from left to right (for the first digit)
        while i < end:
            if(line[i].isnumeric()):
                endResult += line[i]
                break
            i += 1
        i = end # Start for right to left (for the last digit)
        while i >= 0:
            if(line[i].isnumeric()):
                endResult += line[i]
                break
            i -= 1
        endoutput += int(endResult) # Add result to the final sum
    except Exception as e:
        pass
print(f"Result: {endoutput}") # Print result