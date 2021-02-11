n = int(input())
dists = list(map(int, input().split(" ")))
oils = list(map(int, input().split(" ")))

cost = 0
changes = [0]
now = oils[0]
length = len(oils)

for i in range(1,length-1):
    if now > oils[i]:
        changes.append(i)
        now = oils[i]

changes.append(length)

for i in range(len(changes)-1):
    cost += sum(dists[changes[i]:changes[i+1]])*oils[changes[i]]

print(cost)