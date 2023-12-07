import re # Using regular expressions module

file = open("cards.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines
pointsSum = 0 # Final sum of all points

for line in lines: # Going thru each line
    winningNums = re.sub("\\|.*", "", line) # Cut line until the "|" element (Winning numbers)
    winningNums = re.findall(r'\d+', winningNums) # Find each number for winning numbers side of line
    winningNums.pop(0) # Remove the first num (the number of card)
    nums = re.findall(r'\d+', line) # Find all numbers on line
    card = nums[0] # Get the number of card
    nums.pop(0) # Remove it
    for i in range(len(winningNums)): # For loop for removing winning numbers from all numbers on line
        nums.pop(0)
    points = 0 # Points counter
    for winNum in winningNums: # For loop for comparing each winning number to number we have
        for num in nums:
            if(winNum == num):
                if points == 0:
                    points += 1
                else:
                    points += points
    pointsSum += points # Add points to the final sum
    print(f"Card {card} - Got {points} point(s), sum is {pointsSum}")

print(f"Result: {pointsSum}")