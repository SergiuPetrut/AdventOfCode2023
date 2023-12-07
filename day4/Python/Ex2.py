import re

file = open("cards.txt","r")
lines = file.readlines()

matchesSum = 0

cardScan = []
for i in range(len(lines)):
    cardScan.append(1)
for line in lines:
    winningNums = re.sub("\\|.*", "", line)
    winningNums = re.findall(r'\d+', winningNums)
    winningNums.pop(0)
    nums = re.findall(r'\d+', line)
    card = int(nums[0])
    nums.pop(0)
    for i in range(len(winningNums)):
        nums.pop(0)
    matches = 0
    for winNum in winningNums:
        for num in nums:
            if(winNum == num):
                matches += 1
    print(f"Card {card} - Got {matches} matches and {cardScan[card-1]} instances")
    for i in range(cardScan[card-1]):
        try:
            for i in range(card, card+matches):
                cardScan[i] += 1
        except:
            pass
for value in cardScan:
    matchesSum += value 
print(f"Result: {matchesSum}")