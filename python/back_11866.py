from collections import deque

m , n = list(map(int, input().split(" ")))

people = deque()
answer = "<"

for i in range(m):
    people.append(i+1)

count = 1
while len(people) != 1:
    if count == n:
        answer += str(people.popleft()) + ", "
        count = 0
    else:
        people.append(people.popleft())

    count += 1

print(answer + str(people[0]) + ">")
