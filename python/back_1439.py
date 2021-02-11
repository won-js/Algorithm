cards = input()

groups = 1
now = cards[0]

for i in range(1,len(cards)):
    if now != cards[i]:
        now = cards[i]
        groups+=1

print(groups//2)