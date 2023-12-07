import re

file = open("cards.txt","r")
lines = file.readlines()

pointsSum = 0

for line in lines:
    winningNums = re.sub("\\|.*", "", line)
    winningNums = re.findall(r'\d+', winningNums)
    winningNums.pop(0)
    nums = re.findall(r'\d+', line)
    card = nums[0]
    nums.pop(0)
    for i in range(len(winningNums)):
        nums.pop(0)
    points = 0
    for winNum in winningNums:
        for num in nums:
            if(winNum == num):
                if points == 0:
                    points += 1
                else:
                    points += points
    pointsSum += points
    print(f"Card {card} - Got {points} point(s), sum is {pointsSum}")

print(f"Result: {pointsSum}")