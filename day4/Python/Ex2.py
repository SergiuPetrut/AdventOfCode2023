import re # Using regular expressions module

file = open("cards.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines
matchesSum = 0 # Final sum of all matches

cardScan = [] # A list in which the iterations amount for each card will be stored
for i in range(len(lines)): # Initialize the list with value "1" for each card
    cardScan.append(1)
for line in lines: # Going thru each line
    winningNums = re.sub("\\|.*", "", line) # Cut line until the "|" element (Winning numbers)
    winningNums = re.findall(r'\d+', winningNums) # Find each number for winning numbers side of line
    winningNums.pop(0) # Remove the first num (the number of card)
    nums = re.findall(r'\d+', line) # Find all numbers on line
    card = int(nums[0]) # Get the number of card
    nums.pop(0) # Remove it
    for i in range(len(winningNums)): # For loop for removing winning numbers from all numbers on line
        nums.pop(0)
    matches = 0 # matches counter
    for winNum in winningNums: # For loop for comparing each winning number to number we have
        for num in nums:
            if(winNum == num):
                matches += 1
    print(f"Card {card} - Got {matches} matches and {cardScan[card-1]} instances")
    for i in range(cardScan[card-1]): # For loop for adding iterations to cards
        try:
            for i in range(card, card+matches):
                cardScan[i] += 1
        except:
            pass
for value in cardScan: # Sum all matches into 1 variable
    matchesSum += value 
print(f"Result: {matchesSum}")