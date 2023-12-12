# W.I.P.
hands = ["High card","One pair","Two pair","Three of a kind","Full house","Four of a kind","Five of a kind"]
strengths = ["J","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
file = open("cards.txt","r") # Open file in read-mode
lines = file.readlines() # Read file by lines

cards = []
cardsBids = []
cardsRanks = []
totalWinningSum = 0

# 252383714 too high 

def replace_cards_data(card1,card2):
    tmp1 = cards[card1]
    tmp2 = cardsBids[card1]
    tmp3 = cardsRanks[card1]
    cards[card1] =  cards[card2]
    cardsBids[card1] =  cardsBids[card2]
    cardsRanks[card1] =  cardsRanks[card2]
    cards[card2] =  tmp1
    cardsBids[card2] = tmp2
    cardsRanks[card2] = tmp3  

def compare_cards_bigger(card1,card2):
    for elementIndexSecondCard,element in enumerate(card1):
        element2 = card2[elementIndexSecondCard]
        element1Strength = strengths.index(element)
        element2Strength = strengths.index(element2)
        if element1Strength > element2Strength:
            return True  
        elif element1Strength < element2Strength:
            return False

for line in lines:
    i = 0
    side = False
    card = ""
    bid = ""
    while i < len(line):
        if line[i] != " " and line[i] != "\n":
            if side:
                bid += line[i]
            else:
                card += line[i]
        else:
            side = not side
        i += 1
    cards.append(card)
    cardsBids.append(int(bid))

for card in cards: # Going thru each card
    handPos = 0
    checkedElements = []
    for i, element in enumerate(card): # Going thru each element in this card
        firstIndex, lastIndex = None, None
        handPosCurrent = 0
        for index in range(0,len(card)): # Going thru each element in this card after the selected element
            if (element == card[index] or card[index] == strengths[0]):
                handPosCurrent += 1
                print(element,index,i,handPosCurrent)
                if not firstIndex:
                    firstIndex = index
                lastIndex = index
            if handPosCurrent > handPos and firstIndex != lastIndex:
                handPos = handPosCurrent
    print(f"Card: {card}, Rank: {hands[handPos]} ({handPos})")
    
    cardsRanks.append(handPos)
    
for i in range(len(cards)):
    for index, card in enumerate(cards):
        if index+1 == len(cardsRanks):
            break
        if cardsRanks[index] > cardsRanks[index+1]:
            replace_cards_data(index,index+1)
        elif cardsRanks[index] == cardsRanks[index+1]:
            if compare_cards_bigger(cards[index], cards[index+1]):
                replace_cards_data(index,index+1)
for i, bid in enumerate(cardsBids):
    totalWinningSum += (i+1) * bid

print(f"Result: {totalWinningSum}")

